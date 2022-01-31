# -*- coding: utf-8 -*-
import pygsheets
import random

def GetPidorTexts():
    auth = pygsheets.authorize('/home/mberezovskiy/Creds/CredentialsGoogle.json')
    Sheet=auth.open('PidorTexts')
    PidorTextsSheet=Sheet.worksheet_by_title('Pidor')
    PidorTexts=PidorTextsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    if not PidorTexts[0]:
        PidorTexts=["Я хуй знает, кто поудалял все смехуечки", "Но пусть пидор будет "]
    Answer = PidorTexts[random.randint(0, len(PidorTexts)-1)]
    LastString=Answer.pop()
    return(Answer, LastString)

def GetChampions():
    auth = pygsheets.authorize('/home/mberezovskiy/Creds/CredentialsGoogle.json')
    Sheet=auth.open('PidorTexts')
    ChampionsSheet=Sheet.worksheet_by_title('Champions')
    Champions=ChampionsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    if not Champions[0]:
        Champions=["Я хуй знает, кто поудалял все смехуечки, но сегодня пидор "]
    Answer = Champions[random.randint(0, len(Champions)-1)]
    LastString=Answer.pop()
    return(Answer, LastString)

#print(GetChampions()[1])


