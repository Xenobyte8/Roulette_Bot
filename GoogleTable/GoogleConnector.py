import pygsheets

def GetTexts():
    auth = pygsheets.authorize()
    Sheet=auth.open('PidorTexts')
    PidorTexts=Sheet.worksheet_by_title('Pidor')
    Champions=Sheet.worksheet_by_title('Champions')
    print (PidorTexts.get_all_values(include_tailing_empty=False))
    print ("ty pidor")
    print (str(PidorTexts.cell('A1')))

GetTexts()