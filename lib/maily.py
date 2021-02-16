#!/usr/bin/env python3
from cmdtutil import prnwo as cupw
cupw("here")

import datetime
import email
import re

class Maily:

    def __init__(self, cfg):
        self.cfg = cfg
        #self.mail = # email.message_from_string(raw_email_string)
        #self.maildict['from'] = #
        #self.maildict['to'] = #
        #self.maildict['local_date'] = # datetime object
        #self.maildict['local_message_date'] = #Wed, 10 Feb 2021 07:50:59
        #self.maildict['date'] = str(self.maildict'local_date') #2021-02-10 08:53:18
        #self.maildict['subject'] = subject
        #self.maildict['body'] = body
        
        
    def setMail(self, mail): #<mail data
        raw_email = mail[0][1]
        raw_email_string = raw_email.decode('utf-8')
        self.mail = email.message_from_string(raw_email_string)
        cupw("self.mail=", self.mail)
        
        self.maildict = {}
        
        # Header Details
        self.maildict['date'] = "empty date" #TODO from cfg
        date_tuple = email.utils.parsedate_tz(self.mail['Date'])
        if date_tuple:
            self.maildict['local_date'] = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            self.maildict['local_message_date'] = "%s" %(str(self.maildict['local_date'].strftime("%a, %d %b %Y %H:%M:%S")))
            self.maildict['date'] = str(self.maildict['local_date'])
        
        if 'From' in self.mail:
            self.maildict['from'] = str(email.header.make_header(email.header.decode_header(self.mail['From'])))
        else:
            self.maildict['from'] = "empty From" #TODO from cfg
        
        if 'To' in self.mail:
            self.maildict['to'] = str(email.header.make_header(email.header.decode_header(self.mail['To'])))
        else:
            self.maildict['to'] = "empty To" #TODO from cfg
            
        if 'Subject' in self.mail:    
            self.maildict['subject'] = str(email.header.make_header(email.header.decode_header(self.mail['Subject'])))
        else:
            self.maildict['subject'] = "empty Subject!!!" #TODO from cfg
        
        # Body details
        self.maildict['body'] = "empty body" #TODO
        for part in self.mail.walk():
            if part.get_content_type() == "text/plain":
                self.maildict['body'] = part.get_payload(decode=True).decode('utf-8')
                


        
    def checkGrabberMail(self): #TODO more checks. checks only for klammeraff until now!!!
        ok = 0
        if self.maildict['to'].find(self.cfg['klammeraff']) > 0:
            ok = 1
            
        return ok
    
    
    def getMailDict(self):
        return self.maildict
        
    def getTo(self):
        return self.maildict['to']
        
        
    def getArchivFilename(self): #>2021-02-10_085318_subject.txt
        filename = self.cfg['archive']
        filename += self.getFormatedDateStr() + "-" #2021-02-10 08:53:18
        filename += self.getFormatedSubjectStr()
        filename += ".txt"
        return filename
    
    def getFormatedSubjectStr(self):
        return re.sub('[^a-zA-Z0-9]', '', self.maildict['subject'])
    
    def getFormatedDateStr(self):
        return str(self.maildict['local_date'].strftime("%Y%m%d_%H%M%S"))
    
    
    
    def saveMail(self):
        #>>>>>>> mailren!!!!!! >>> email.parser
        str1 = self.maildict['date'] + "\n"
        str1 += self.maildict['subject'] + "\n"
        str1 += self.maildict['to']  + "\n"
        str1 += self.maildict['body'] + "\n"
        
        filename = self.getArchivFilename() 
        with open(filename, "w") as fh:
            fh.write(str1)
        
        return filename
        
    
