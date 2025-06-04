import yaml
import re
import shutil
import os
from glob import glob
import json

class Article:
    
    # Providing Namespace is an override for this file. 
    def __init__(self, path):
        print("Creating Article for: ", path)
        self.path = path 
        
        if os.path.isdir(self.path): 
            self.isdir, self.isfile = True, False
            self.text = None
            self.yaml = None
        else:
            self.isdir, self.isfile = False, True
            self._file_metadata()
        
    def _file_metadata(self):
        self.filename = os.path.basename(self.path)
        self.basename, self.extension = '.'.join(self.filename.split('.')[:-1]), self.filename.split('.')[-1:][0]
        
        # We don't try and load text from non markdown files. 
        if self.extension != 'md':
            self.text = None
            self.yaml = None
            return None # This function returns None either way, this just ends early.
        
        self.text = open(self.path).read()
        yamltext = re.match('^---\n(.+?)---\n?', self.text, flags=re.S)
        self.yaml = yaml.safe_load(yamltext.group(1)) if yamltext else {}
        
    def _deployable_fields(self):
        ret = {}
        for key in ['doku', 'postdate', 'categories', 'tags']:
            value = self.yaml.get(key, '')
            if value: ret[key] = value
        return ret
            

CONFIG = json.load(open('tools/obsidian-import-config.json'))
OBSIDIAN = CONFIG['obsidian-path']

# Picks up files that have yaml metadata to deploy.
# ---
# doku: <namespace>
# ---
#
# Can also drop a "dokudeploy.md" file in a folder that will apply the doku and dokuflag
# properties of that file to all files and folders in that folder. Template in Obsidian.


# Normal operation is this interates through the vault, looks for files with the yaml metadata 
# set to deploy, then it deploys them. When Namespace is set, it iterates through and updates 
# the namespace in the metadata/adds yaml metadata, but doesn't deploy anything. The namespace 
# being set is used with a dokudeploy recursion to setup a folder for deployment.
def import_obsidian(src=None, overwrite={}):
    if not src: 
        src = CONFIG['obsidian-path']
    
    # All the obsidian file paths under src.
    src = os.path.join(src, '**')
    glob_list = glob(src, recursive=True)
    glob_list = [path for path in glob_list if not any([True for x in CONFIG['ignore'] if x in path])]
    for path in glob_list:
        
        art = Article(path)
        # Dirs don't get processed.
        if art.isdir: continue
        # Only markdown files get handled.
        if art.extension != 'md': continue 
        # If there's no doku key in the yaml, it's not a page to put on the website.
        if not art.yaml.get('doku') and not overwrite: continue
        
        # When we find a Dokudeploy, we recur this function with the namespace 
        # parameters set, which allows us to override that directory tree with the dokudeploy
        # variables. We then remove the dokudeploy so we don't do that everytime. 
        if art.basename == 'dokudeploy' and not overwrite:
            print("Recurring:", _relative_path(os.path.dirname(art.path)), art._deployable_fields())
            import_obsidian(os.path.dirname(path), overwrite=art._deployable_fields())
            os.remove(path)
            continue
        
        # If a namespace is set, we're force deploying any file in this path with the namespace
        # parameter. We don't want to deploy the dokudeploy file, since it's a trigger file.
        elif overwrite and art.basename != 'dokudeploy':
            if art.yaml:
                art.yaml.update(overwrite)
                text = re.sub('(?<=^---\n)(.*?)(?=---\n)', yaml.dump(art.yaml), art.text, flags=re.S)
            else:
                art.yaml.update(overwrite)
                text = f"---\n{yaml.dump(art.yaml)}---\n{art.text}"
            with open(art.path, 'w') as f:
                f.write(text)
            print("Updated:", _relative_path(art.path), 'WITH', art._deployable_fields())
            continue
        
        _filetowiki(art)
        # _transfer(art, art.yaml)
   

# Transfer can take a folder and run on all files in the folder. This isn't used by automated flows.
def _transfer(article, namespace=None):
    
    if article.isfile:
        _filetowiki(article)
    else: # The non standard folder flow. 
        for folder, sfolders, files in os.walk(article.path):
            for f in [x for x in files if os.path.splitext(x)[-1] == '.md']:
                _filetowiki(os.path.join(folder, f))
      
def _filetowiki(article):
    
    collection_path = os.path.join('_obsidian', article.yaml.get('doku'))
    os.makedirs(collection_path,exist_ok=True)
    if 'postdate' in article.yaml:
        ispost = True
        outname = str(article.yaml['postdate'])+'-'+slugify(article.filename)
        post_output_path = os.path.join('_posts', outname)
    else: ispost = False
    output_path = os.path.join(collection_path, article.filename)
    
    # Change callouts to match formatting for Static site.
    formatted = re.sub("\\n> \\[!\\w+\\] (.*?\\n)(?!>)", "\n> \\g<1>{: .prompt-tip }", 
                       article.text, 
                       flags=re.S|re.M)
    
    # Upload attachments 
    formatted = _upload_attachments(article, formatted)
    
    # Change internal links to hard links to the website version of the files. 
    # formatted = re.sub("(?<!!)\\[\\[(.*?)\\]\\]", internal_link_fix, formatted)
    formatted = re.sub("(?<!!)\\[\\[(.*?)\\]\\]", jekyll_link_fix(collection_path), formatted)
    
    # Output the formatted file
    with open(output_path, 'w') as output:
        output.write(formatted)
    if ispost: 
        with open(post_output_path, 'w') as output:
            output.write(formatted)
    

def _upload_attachments(article, convertedtxt):
    attachments = re.findall('(\\[\\[(?!http)(.*?\\.\\w{3,4})\\|?(.*)?\\]\\])', convertedtxt)
    os.makedirs(os.path.join('assets', 'uploads'), exist_ok=True)
    if not attachments:
        return convertedtxt
    
    for attachment in attachments:
        size = '100' if 'small' in attachment[2] else '300'
        position = next((x for x in ['right', 'left', 'center'] if x in attachment[2]), '')
        
        size = f'w="{size}"' if size else ""
        position = f'.{position}' if position else ""
        classes = f'''{{: {size} {position}}}''' if size or position else ''
        
        convertedtxt = convertedtxt.replace("!"+attachment[0], f'![{attachment[1]}]({attachment[1]}){classes}')
        
        img_roots = [
            f'{OBSIDIAN}/@assets/Images',
            f'{OBSIDIAN}/@assets/',
            os.path.dirname(article.path)
            ]
        for root in img_roots:
            p = os.path.join(root, attachment[1])
            if os.path.isfile(p):
                shutil.copy(p,os.path.join('assets', 'uploads', attachment[1]))
                break
        else: print("Didn't find file:", attachment[1])
    return convertedtxt

# Regex Fix Functions

def internal_link_fix(match):
    link = match.group(1)
    if '|' in link:
        link, text = link.split('|')
    else:
        link, text = link, link
    return f"""[{text}]({link})"""

def jekyll_link_fix(collection_path):
    #  {% link _obsidian/Pokexplorers/Becky.md %}
    def inner(match):
        link = match.group(1)
        if '|' in link:
            link, text = link.split('|')
        else:
            link, text = link, link
        details = link.split('#')
        if len(details)>1 and not details[0]: # Heading, same page.
            jekyll_link = '#'+slugify(details[1])
        else: 
            jekyll_link = '{% link '+ os.path.join(collection_path, details[0])+'.md %}'
        # Assumes that the extension is markdown. Kinda have to since extension isn't in markdown.
        return f"""[{text}]({jekyll_link})"""
    return inner

# Util
def slugify(text):
    return text.lower().replace(' ', '-')

def _relative_path(path):
    for one, two, in zip(path, CONFIG['obsidian-path']):
        if one != two:
            return path[path.index(one):]
    return path[len(CONFIG['obsidian-path']):]


if __name__ == '__main__':
    
    # import_obsidian('''/Users/bill/Obsidian/Writer's Room/Roleplaying Games/Worlds & Adventures/Pokerole Modules/Pokexplorers Summer Camp!''')
    # import_obsidian('''/Users/bill/Obsidian/Writer's Room/Roleplaying Games/Words of Willow''')
    # import_obsidian('''/Users/bill/Obsidian/Writer's Room/Roleplaying Games/Finished Games/Galar Journeys/Story''')
    import_obsidian()