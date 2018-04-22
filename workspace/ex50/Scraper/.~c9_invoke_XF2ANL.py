import csv
import json

def scrape(textFile):
    text_file = open(textFile, "r")
    lines = text_file.read().split('\n')
    for text in lines:
        if 
            lines.remove(text)
    
    dataTable = []
    for text in lines:
       dataTable.append(text.split('\t'))
       
       
    print(dataTable)
    
def load(textFile):
    array = scrape(textFile)
    for dataLine in array:
        C
    


class Course(object):
    def __init__(self, dataLine):
        self.num = dataLine[0]
        self.name = dataLine[1]
        self.credits = dataLine[2]
        self.reqs = dataLine[3].split(',').trim()
        self.num_reqs = len(self.reqs)



scrape("CC.txt")