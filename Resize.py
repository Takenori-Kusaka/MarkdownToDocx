#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import codecs
import glob
from PIL import Image

def usage():
  print("\nUsage: python Resize.py $Filepath $ResizeValue\n")
  print('  Biref: This program resize images in "_files" folder. Set target file and resize value with follow arguments.\n')
  print("  - Filepath: Set the absolute or relative path of the html file.")
  print('  - ResizeValue: Set any Int value. The images resize to this value if it larger than this value.')

def resize(filepath, resize_value):
  print("\nTarget path: " + filepath)
  print("ResizeValue: " + str(resize_value))
  print("Start to resize images")
  filename = os.path.basename(filepath)
  filename_title, filename_ext = os.path.splitext(filename)
  resource_files = glob.glob(os.path.join(filepath.replace(filename_ext, '_files'), '*'))

  for rf in resource_files:
    try:
      img = Image.open(rf)
      img_name = os.path.basename(rf)
      print("Detect image file: " + img_name)
      if img.height > resize_value or img.width > resize_value:
        print(img_name + " is need to resize.")
        print(img_name + "'s height is " + str(img.height) " and new width is " + str(img.width))
        if img.height > img.width:
          print(img_name + "'s height is larger than " + str(resize_value))
          ratio = img.height / resize_value
        else:
          print(img_name + "'s width is larger than " + str(resize_value))
          ratio = img.width / resize_value
        print(img_name + " is resized by a factor of " + str(ratio))
        img_new_height = int(img.height / ratio)
        img_new_width = int(img.width / ratio)
        print(img_name + "'s new height is " + str(img_new_height) " and new width is " + str(img_new_width))
        print("Update " + filename + " by new size")
        with codecs.open(filepath, 'r', 'utf-8') as html:
          text = html.read()
          after = text.replace(img_name + '"', img_name + '" width=' + str(img_new_width) + ' height=' + str(img_new_height))
        with codecs.open(filepath, 'w', 'utf-8') as html:
          html.write(after)
      else:
        print(img_name + " is not need to resize.")
    except OSError as e:
      pass
  print("All done. Success!")


def main():
  if len(sys.argv) != 3 or not os.path.exists(sys.argv[1]) :
    usage()
  else:
    resize(sys.argv[1], int(sys.argv[2]))

if __name__ == "__main__":
  main()