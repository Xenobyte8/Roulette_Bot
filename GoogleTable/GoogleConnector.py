import pygsheets

def GetTexts():
    auth = pygsheets.authorize()
    Sheet=auth.open('PidorTexts')
    PidorTexts=Sheet.worksheet_by_title('Pidor')
    Champions=Sheet.worksheet_by_title('Champions')
    print (PidorTexts.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False))[0][0]
    print ("ty pidor")

GetTexts()