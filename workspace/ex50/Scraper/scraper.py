from sqlitedict import SqliteDict
import sqlite3
import json

courses = {}

def scrape(textFile):
    text_file = open(textFile, "r")
    lines = text_file.read().split('\n')
            
    dataTable = []
    for text in lines:
        if text[0].isdigit():
            dataTable.append(text.split('\t'))
    return dataTable   
       
def load(textFile):
    array = scrape(textFile)
    for dataLine in array:
        if dataLine[0] in list(courses.keys()):
            continue
        courses[dataLine[0]] = Course(dataLine)
        
    


class Course(object):
    def __init__(self, dataLine):
        self.num = dataLine[0]
        self.name = dataLine[1]
        self.credits = dataLine[2]
        print(dataLine[1])
        self.reqsFull = dataLine[3]
        self.reqs = dataLine[3].split(',')
        for req in self.reqs:
            req.split()
        self.num_reqs = len(self.reqs)
        
    def __str__(self):
        return "Course Num: "+self.num+"\tName: "+self.name+"\tCredits: "+self.credits+"\tRequirements: "+self.reqsFull
        
    def __repr__(self):
        return self.__str__()



def loadAll():
    load("CC.txt")
    load("NS.txt")
    load("HST.txt")
    load("SCL.txt")
    load("AHo.txt")
    load("AHp.txt")
    load("AHq.txt")
    load("AHr.txt")
    load("WC.txt")
    load("WCr.txt")
    load("WCd.txt")
    load("QQ.txt")
    load("QR.txt")
    load("ITR.txt")
    print("loaded successfully")
    return courses

    
def loadDB():
    coursesDB = SqliteDict('./coursesDB.sqlite', autocommit=True)
    for key in courses:
        coursesDB[key] = courses[key]
# loadDB()

