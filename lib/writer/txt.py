#!/usr/bin/env python3
from cmdtutil import prnwo as cupw
cupw("here")


class Exporter:

    def __init__(self, cfg):
        self.cfg = cfg
        self.exporttype = "txt"
        
    def add(self, filename, mail): #<filename, maildict
        '''
        formes mail for append in filename
        <filename, maildict
        >null
        '''
        #TODO check if file exist
        #TODO check if NOT append (should not be needed?)
        with open(filename, "a") as fh:
            fh.write(self.formStr(mail))
        
        
    def formStr(self, mail):
        str1 = mail['date'] + self.cfg['nl'][self.exporttype]
        str1 += mail['subject'] + self.cfg['nl'][self.exporttype]
        str1 += mail['to'] + self.cfg['nl'][self.exporttype]
        str1 += mail['body'] + self.cfg['nl'][self.exporttype]
        str1 += self.cfg['mailend'][self.exporttype]
        return str1
        
