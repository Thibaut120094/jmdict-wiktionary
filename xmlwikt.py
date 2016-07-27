#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import xml.etree.ElementTree as ET
import io
import pywikibot

script, jmdictdump, wiktdump = argv

wikttxt = io.open(wiktdump, 'r', encoding='utf-8')
outputfile = io.open('output.txt', 'w+', encoding='utf-8')

tree = ET.parse(jmdictdump)

for entry in tree.iter('keb'):
  if entry not in wikttxt.readlines():
   outputfile.write(entry.text+"\n")
