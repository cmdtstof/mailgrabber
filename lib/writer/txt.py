#!/usr/bin/env python3
from cmdtutil import prnwo as cupw
cupw("here")


class Exporter:

    def __init__(self, cfg):
        self.cfg = cfg
        self.exporttype = "txt"
        
    def add(self, filename, mail):
        str1 = mail['date'] + self.cfg['septitle']
        str1 += mail['subject'] + self.cfg['nl'][self.exporttype]
        str1 += mail['body'] + self.cfg['nl'][self.exporttype]
        str1 += self.cfg['mailend'][self.exporttype]
        
        #TODO check if file exist
        #TODO check if NOT append (should not be needed?)
        with open(filename, "a") as fh:
            fh.write(str1)
        
        
