# -*- coding: utf-8 -*-
import pygsheets

def GetTexts():
    auth = pygsheets.authorize('/home/mberezovskiy/Creds/CredentialsGoogle.json')
    Sheet=auth.open('PidorTexts')
    PidorTextsSheet=Sheet.worksheet_by_title('Pidor')
    ChampionsSheet=Sheet.worksheet_by_title('Champions')
    PidorTexts=PidorTextsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    PidorTexts=PidorTextsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    if not PidorTexts[0]:
        PidorTexts=["Я хуй знает, кто поудалял все смехуечки, но пусть пидор будет "]
    Champions=ChampionsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    if not Champions[0]:
        Champions=["Я хуй знает, кто поудалял все смехуечки, но сегодня пидор "]

    return(PidorTexts, Champions)

a=GetTexts()
for i in a:
    print(i)