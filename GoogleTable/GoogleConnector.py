import pygsheets

def GetTexts():
    auth = pygsheets.authorize()
    Sheet=auth.open('PidorTexts')
    PidorTexts=Sheet.worksheet_by_title('Pidor')
    Champions=Sheet.worksheet_by_title('Champions')
    print (PidorTexts.get_all_records())
    print ("ty pidor")
    print (PidorTexts.cell('A1'))

GetTexts()