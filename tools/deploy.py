import pandas as pd
import re
import shutil
import os
from glob import glob
import fire
import obsidian_import

rundir = os.getcwd()
    
def build(rm=False):
    
    if rm:
        os.chdir('/Volumes/web/wordsofwillow')
        fs = [x for x in os.listdir() if 'photography' not in x]
        for f in fs:
            print(f'rm -r {f}')
            os.system(f'rm -r {f}')
    
    os.chdir('/Users/bill/Code/wordsofwillow')
    os.system('JEKYLL_ENV=production bundler exec jekyll build')
    print("COPY STARTING...")
    os.system('cp -r _site/* /Volumes/web/wordsofwillow/')
    print("COPY FINISHED.")

def update(rm=False):
    obsidian_import.import_obsidian()
    build(rm)

if __name__ == '__main__':
  fire.Fire()