#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import codecs
import glob
from PIL import Image

path = sys.argv[1]
filename = os.path.basename(path)
filename_title, filename_ext = os.path.splitext(filename)
resource_files = glob.glob(os.path.join(sys.argv[1].replace(filename_ext, '_files'), '*'))
resize_width = int(sys.argv[2])

for rf in resource_files:
  try:
    img = Image.open(rf)
    if img.height > resize_width:
      ratio = img.height / resize_width
      img_new_height = int(img.height / ratio)
      img_new_width = int(img.width / ratio)
      img_name = os.path.basename(rf)
      with codecs.open(path, 'r', 'utf-8') as html:
        text = html.read()
        after = text.replace(img_name + '"', img_name + '" width=' + str(img_new_width) + ' height=' + str(img_new_height))
      with codecs.open(path, 'w', 'utf-8') as html:
        html.write(after)
  except OSError as e:
    pass