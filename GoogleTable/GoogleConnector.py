import pygsheets

def GetTexts():
    auth = pygsheets.authorize()
    Sheet=auth.open('PidorTexts')
    PidorTextsSheet=Sheet.worksheet_by_title('Pidor')
    ChampionsSheet=Sheet.worksheet_by_title('Champions')
    PidorTexts=PidorTextsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    for i in PidorTexts:
        for j in i:
            print(j)
    #print (PidorTexts)

GetTexts()