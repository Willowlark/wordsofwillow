import pandas as pd
import re
import shutil
import os
from glob import glob
import fire

"""
Album upload process
0. Put the Album in the correct header folder (100% X)
1. Flag the album cover with Green
2. Select all the files in the album and use the "Write Data Field..." plugim to write "{CollectionFullNames}" to Source
3. Export using the "Site 2k" and "Site Original" to the Photography folder in the thelittlethingswemiss web root
4. Run `ipython -i manager.py`
5. Run photo move to sort the files in the root of the Photography folder into the collection structure found there
6. Run index to update the index for the jekyll dataset
7. Run build to rebuild the website 
"""


rundir = os.getcwd()
    
def build(rm=False):
    
    if rm:
        os.chdir('/Volumes/web/wordsofwillow')
        fs = [x for x in os.listdir() if 'photography' not in x]
        for f in fs:
            print(f'rm -r {f}')
            # os.system(f'rm -r {f}')
    
    os.chdir('/Users/bill/Code/wordsofwillow')
    os.system('JEKYLL_ENV=production bundler exec jekyll build')
    print("COPY STARTING...")
    os.system('cp -r _site/* /Volumes/web/wordsofwillow/')
    print("COPY FINISHED.")
    
# if __name__ == '__main__':
#     build(False)

if __name__ == '__main__':
  fire.Fire()