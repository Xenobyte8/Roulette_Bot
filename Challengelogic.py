# -*- coding: utf-8 -*-
import datetime
import sys
import random
sys.path.append('/home/mberezovskiy/project/DB')
import dblogic

class Challenge:
    
    def __init__(self, IdChat, IdPerson, NamePerson):
        self.ID=IdChat
        self.challengers=[[IdPerson, NamePerson]]
        self.results=[[IdPerson, 0]]
        time = datetime.datetime.now()
        self.ChallengeTime = time.replace(day=(datetime.datetime.now().day-1))

    def GetId(self):
        return self.ID


    def Register(self, IdPerson, Name):
        for each in self.challengers:
            if each[0]==IdPerson: return "Этот петух уже есть в нашем уголке"
        self.challengers.append([IdPerson, Name])
        self.results.append([IdPerson, 0])
        return "Милости прошу к нашему шалашу"

    def ReturnChallengers(self):
        spisok=[]
        i=0
        if not self.challengers:
            return 0
        for each in self.challengers:
            spisok.append([each[0], each[1], self.results[i][1]])
            i+=1
        return spisok

    def FindPidor(self):
        if self.ChallengeTime.day==datetime.datetime.now().day:
            return "Потерпи до завтра, петушок"
        try: 
            pidor = random.randint(0, len(self.challengers)-1)
            self.results[pidor][1]+=1
            self.ChallengeTime=datetime.datetime.now()
            return [str(self.challengers[pidor][1]) + str(self.results[pidor][1])]
        except: return ["Дерьмо случается"]
    
    def SetChallengeTime(self):
        self.ChallengeTime=datetime.datetime.now()
