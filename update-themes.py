#!/usr/bin/env python2

import os
import shutil

COLORS = ['Mint-X/gtk-3.0',
          'Mint-X-Aqua/gtk-3.0',
          'Mint-X-Blue/gtk-3.0',
          'Mint-X-Brown/gtk-3.0',
          'Mint-X-Grey/gtk-3.0',
          'Mint-X-Orange/gtk-3.0',
          'Mint-X-Pink/gtk-3.0',
          'Mint-X-Purple/gtk-3.0',
          'Mint-X-Red/gtk-3.0',
          'Mint-X-Sand/gtk-3.0',
          'Mint-X-Teal/gtk-3.0']

SRC = 'src'
DEST = 'usr/share/themes'

src_files = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(SRC)
    for f in files]

for color in COLORS:
    for src_file in src_files:
        dest_file = src_file.replace(SRC, os.path.join(DEST, color), 1)
        shutil.copy2(src_file, dest_file)
