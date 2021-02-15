#!/usr/bin/env python3
from cmdtutil import prnwo as cupw
cupw("here")

import datetime
import email
import imaplib

class Mailserver:

    def __init__(self, cfg):
        self.cfg = cfg
        self.mailTest = [
            {
                "to": "test1@news",
                "subject": "subject1",
                "date": "20210101",
                "body": "body1 body body body"
            },
            {
                "to": "test2@news",
                "subject": "subject2",
                "date": "20210102",
                "body": "body2 body body body"
            },
            {
                "to": "",
                "subject": "subject3",
                "date": "20210103",
                "body": "body3 body body body"
            },
            {
                "subject": "subject4",
                "date": "20210104",
                "body": "body4 body body body"
            },
        ]

        
    def closer(self):
        self.server.close()
        self.server.logout()
    
    def connect(self):
        cupw("connect to mailserver=", self.cfg)
        self.server = imaplib.IMAP4_SSL(self.cfg['server'])
        self.server.login(self.cfg['user'], self.cfg['pwd'])

        # ~ self.server.select('Drafts')
        # ~ typ, data = self.server.search(None, 'ALL')
        # ~ for num in data[0].split():
            # ~ cupw("******num=", num)
            # ~ typ, data = self.server.fetch(num, '(RFC822)')
            # ~ cupw("data=", data)
        
        
    def getDraftsNums(self): #>nums (list))
        self.server.select('Drafts')
        typ, data = self.server.search(None, 'ALL')
        # ~ cupw("data[0].split()=", data[0].split())
        # ~ cupw(type(data[0].split()))
                
        return data[0].split()

            
    def getMailNum(self, num, part):
        typ, data = self.server.fetch(num, '(RFC822)')
        cupw(typ)
        cupw(data)
        return typ, data
        
        
    
    def nextMail(self):
        if self.cfg['server'] == 'test':
            return self.mailTest
        else:
            cupw("TODO load mails from=", self.cfg['server'])
            
            
            
            
            return []

    def delMail(self, mail):
        if self.cfg['server'] != 'test':
            cupw("#TODO del mail in mailserver")
