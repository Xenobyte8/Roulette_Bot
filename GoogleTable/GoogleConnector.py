import pygsheets

def GetTexts():
    auth = pygsheets.authorize('/home/mberezovskiy/Creds/CredentialsGoogle.json')
    Sheet=auth.open('PidorTexts')
    PidorTextsSheet=Sheet.worksheet_by_title('Pidor')
    ChampionsSheet=Sheet.worksheet_by_title('Champions')
    PidorTexts=PidorTextsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    PidorTexts=PidorTextsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    Champions=ChampionsSheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
    for i in PidorTexts:
        for j in i:
            print(j)
    return(PidorTexts, Champions)

a=GetTexts()
print(a[1])
if a[1]==null:
    print ("Empty")