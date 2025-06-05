import pandas as pd
import re
import shutil
import os
from glob import glob
import fire
import obsidian_import

rundir = os.getcwd()
LAUNCHDIR = os.getcwd()

def _delete_folder(path):
    os.chdir(path)
    fs = [x for x in os.listdir() if 'photography' not in x]
    for f in fs:
        print(f'rm -r {f}')
        os.system(f'rm -r {f}')
    print()

def clean_repo():
    _delete_folder('/Users/bill/Code/wordsofwillow/_obsidian')
    _delete_folder('/Users/bill/Code/wordsofwillow/assets/uploads')
    _delete_folder('/Users/bill/Code/wordsofwillow/_posts/imported')
    os.chdir(LAUNCHDIR)

def build(rm=False):
    
    if rm: _delete_folder('/Volumes/web/wordsofwillow')
    
    os.chdir('/Users/bill/Code/wordsofwillow')
    os.system('JEKYLL_ENV=production bundler exec jekyll build')
    print("COPY STARTING...")
    os.system('cp -r _site/* /Volumes/web/wordsofwillow/')
    print("COPY FINISHED.")

def update(rm=False, clean=False):
    if clean: clean_repo()
    obsidian_import.import_obsidian()
    build(rm)

if __name__ == '__main__':
  fire.Fire()