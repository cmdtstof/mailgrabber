#!/usr/bin/env python3
from cmdtutil import prnwo as cupw
cupw("here")


class Maily:

    def __init__(self, cfg):
        self.cfg = cfg
        
    def setMail(self, mail): #<mail data >0/1 if grabber mail
        self.mail = mail
        return self.checkGrabberMail()
        
    def checkGrabberMail(self): #checks only for klammeraff!!!
        ok = 0
        if 'to' in self.mail:
            if self.mail['to'] != "":
                if self.mail['to'].find(self.cfg['klammeraff']):
                    ok = 1
        
        return ok
    
    
    def getMail(self):
        return self.mail
        
    def getMailTxt(self):
        return "TODO blablablabla text"
    
    def getTo(self):
        return self.mail['to']
        
    def getFilename(self): #>draft_TOstr1_TOstr2.txt
        l1 = self.getTo().split(self.cfg['klammeraff'])
        filename = self.cfg['archive']
        filename += "draft_" + l1[0] + "-" + l1[1] + ".txt" #TODO add date!!!???
        return filename
    
    
    def saveMail(self):
        #>>>>>>> mailren!!!!!! >>> email.parser
        filename = self.getFilename() 
        with open(filename, "w") as fh:
            fh.write(self.getMailTxt())
        
        return filename
        
    
