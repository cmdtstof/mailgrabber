#!/usr/bin/env python3
from cmdtutil import prnwo as cupw
cupw("here")

# ~ import csv

class Mappingfile:
    
    '''
    - sucht gemäss "to" nach entsprechendem file for append mail body
    - 
    TODO: add not found email adresse with ???
    
    '''

    def __init__(self, cfg):
        self.cfg = cfg
        self.mapfile = self.loadMapFile()
        
    
    def loadMapFile(self):
        mapfile = {}
        with open(self.cfg['mappingfile'], 'r') as fh:
            data = fh.read()
            
        for line in data.split(self.cfg['nl']):
            if line != "":
            # ~ if line.find(self.cfg['delimiter']): #take only lines contain ,
                l1 = line.split(self.cfg['delimiter'])
                if l1[0].find(self.cfg['klammeraff']): #take only contain @
                    # ~ if l1[1] != self.cfg['noentry']: #take everything except ???
                    mapfile[l1[0]] = l1[1]
            
        return mapfile
    
    
    def getExportFilename(self, to): #<str1@str2 >(filename, exporter)
        #TODO check for unwandet chars (eg <asdjlfasd>)
        
        to = to.lower() #TODO use only lowercase
        
        
        filename = self.cfg['exportdir'] + self.splitTo(to) + ".txt"  #default filename
        
        if to in self.mapfile:
            if self.mapfile[to] != self.cfg['noentry']:
                filename = self.mapfile[to]
            else:
                cupw("??? already in mapfile for TO=", to)
        
        else:
            self.addToMapfile(to)
            
        exporter = self.getFileSuffix(filename)
        
        return filename, exporter
        
    def addToMapfile(self, to):
        str1 = to + self.cfg['delimiter'] + self.cfg['noentry'] + self.cfg['nl']
        with open(self.cfg['mappingfile'], "a") as fh:
            fh.write(str1)
            
        cupw("added to mapfile=", str1.rstrip())
        self.mapfile = self.loadMapFile() # reload self.mapfile!!! TODO not working????
    
    
    
    def splitTo(self, to):
        l1 = to.split(self.cfg['klammeraff'])
        return l1[0] + self.cfg['sepfilename'] + l1[1]
        
    def getFileSuffix(self, filename):
        '''
        easy pisy: gibt einfach den letzten teil zurück
        '''
        l1 = filename.split(".")
        return l1[len(l1)-1]
        
        
        

        
        
        
        
        
