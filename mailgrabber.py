#!/usr/bin/env python3
from cmdtutil import prnwo as cupw
cupw("here")

'''
>>> readme.txt
'''

import sys
import lib.mailserver
import lib.writer.txt
import lib.mappingfile
import lib.maily

class App:

    def __init__(self, larg):
        self.larg = larg
        self.opt = self.setDefaultOpt() #1: default options
        self.parseArg(self.larg) #2: parse arg and overwrite options <list >dict 
        self.cfg = self.setCfg() #3: set configs according to options

    
    def setCfg(self):
        cfg = {
            'mailserver': {
                'server': self.opt['--mailserver'],
                'user': self.opt['--mailuser'],
                'pwd': self.opt['--mailpwd'],
                'maildel': self.opt['--maildel']
            },
            'mail': {
                'klammeraff': '@',
                'archive': self.opt['--mailarchiv']
            },
            'mapper': {
                'mappingfile': self.opt['--mapfile'],
                'nl': '\n',
                'delimiter': ',',
                'sepfilename': '_',
                'klammeraff': '@',
                'noentry': '???',
                'exportdir': self.opt['--exportdir']
            },
            
            'export': {
                'exportappend': self.opt['--exportappend'],
                'septitle': ': ',
                'nl': {'txt': '\n'},
                'mailend': {'txt': '*************'}
                }
            }
        return cfg
    
    def setDefaultOpt(self):
        opt = {
            '--mailserver': 'test',
            '--mailuser': 'test@localhost',
            '--mailpwd': 'testpwd',
            '--mapfile': 'data/mapfile.csv',
            '--export': 'txt',
            '--exportdir': 'data/export/txt/',
            '--exportappend': 1,
            '--mailarchiv': 'data/archiv/',
            '--maildel': 1
            }
        return opt
    
    def parseArg(self, larg): #<list >opt-dict, word-list
        larg = larg[1:] #remove 1. arg (=caller name)
        for a in larg:
            if a.startswith("--"):
                l1 = a.split("=")
                self.opt[l1[0]] = l1[1]
                
            else:
                cupw("TODO: what to do with opt=", a)
                

        
#######################################3
if __name__ == '__main__':
    
    larg = sys.argv
    # ~ if len(larg) < 2:
        # ~ larg = ["app", "--mailserver=???", "--mailuser=s18@stof999.ch", "--mailpwd=???", \
            # ~ "--export=txt", "--exportdir=???"]
        # ~ larg = []
    app = App(larg)

    mf = lib.mappingfile.Mappingfile(app.cfg['mapper'])
    
    ms = lib.mailserver.Mailserver(app.cfg['mailserver'])
    ms.connect()
    nums = ms.getDraftsNums()
    cupw("nums=", nums)
    
    for num in nums:
        cupw("******num=", num)
        # ~ typ, data = self.server.fetch(num, '(RFC822)')
        typ, data = ms.getMailNum(num, '(RFC822)')
        cupw("data=", data)
        m = lib.maily.Maily(app.cfg['mail'])
        if m.setMail(data):
            cupw("******** processing mail=", m.getTo())
            
    
    
    
    
    # ~ m = lib.maily.Maily(app.cfg['mail'])
    
    # ~ for mail in ms.nextMail(): #TODO should be a mail object
        # ~ if m.setMail(mail): #check and set
            # ~ cupw("******** processing mail=", m.getTo())
            # ~ (exportFilename,exporter) = mf.getExportFilename(m.getTo())
            
            # ~ if exporter == "txt":
                # ~ wr = lib.writer.txt.Exporter(app.cfg['export'])
                # ~ wr.add(exportFilename, m.getMail())
                # ~ cupw("mail written into=", exportFilename)
                
            # ~ else:
                # ~ cupw("not supported exporter=", exporter)
                
            # ~ #save mail to archive
            # ~ filename = m.saveMail()
            # ~ cupw("mail saved to=", filename)
            
            # ~ #deleted mail on server
            # ~ if app.opt['--maildel']:
                # ~ ms.delMail(m.getMail())
                # ~ cupw("mail deleted=", m.getMail())
                
        # ~ else:
            # ~ cupw("******** NOT processing=", mail)

    ms.closer()        
        
        
        
