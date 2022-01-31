# -*- coding: utf-8 -*-
import mysql.connector
import datetime
import json

#Шальной коммент

def ConnectDB(NameDB=0):
    filejs = open('/home/mberezovskiy/Creds/CredentialsDB.json')
    Creds = json.loads(filejs.read())
    filejs.close()
    if NameDB==0:
        PidorDB=mysql.connector.connect(
            host = Creds["host"],
            user=Creds["user"],
            passwd=Creds["password"])
    else:
        PidorDB=mysql.connector.connect(
        host = Creds["host"],
        user=Creds["user"],
        passwd=Creds["password"],
        database=NameDB)
    
    return PidorDB

def CreateDB(Connector):
    mycursor = Connector.cursor()
    mycursor.execute("drop database db_Pidor")
    mycursor.execute("create database db_Pidor")
    Connector=ConnectDB("db_Pidor")
    mycursor = Connector.cursor()
    mycursor.execute("create table Challenge( "+
    "ChallengeId INT AUTO_INCREMENT PRIMARY KEY not null, " +
    "ChatId bigint not null, " + "Last_time datetime);")
    mycursor.execute("create table Challenger ("+ "ChallengerId INT AUTO_INCREMENT PRIMARY KEY, "
    +"ChallengeId int not null, TelegaId bigint not null, PersonName varchar(255) not null, Score int not null default 0, "+
    " constraint fk_challenge foreign key (ChallengeId) references Challenge(ChallengeId))"
    )

def AddChallenge(DB_Connector, ChatId, TelegaId, PersonName):
    mycursor = DB_Connector.cursor()
    mycursor.execute("select ChatId from Challenge where ChatId="+ str(ChatId))
    IsCreated = mycursor.fetchone()
    if IsCreated: return 0
    sql = "insert into Challenge (ChatId) values (%d)"
    value = (ChatId)
    mycursor.execute(sql % value)
    DB_Connector.commit()
    mycursor.execute("select max(ChallengeId) from Challenge")
    ChallengeId=mycursor.fetchone()
    print(type(ChallengeId[0]))
    sql = "insert into Challenger (ChallengeID, TelegaId, PersonName) values (%d, %d, %r)"
    value=(ChallengeId[0], TelegaId, PersonName)
    mycursor.execute(sql % value)
    DB_Connector.commit()
    return 1


def ShowMeTheDB(DB_Connector):
    mycursor = DB_Connector.cursor()
    mycursor.execute("select * from Challenge")
    text = mycursor.fetchall()
    print (text)
    mycursor.execute("select * from Challenger")
    text = mycursor.fetchall()
    print (text)


def AddChallenger(DB_Connector, ChatId, TelegaId, PersonName):
    mycursor = DB_Connector.cursor()
    mycursor.execute("select ChallengeId from Challenge where ChatId=" + str(ChatId))
    IsExist = mycursor.fetchone()
    print(IsExist)
    if not IsExist: return 0 
    ChallengeId=IsExist[0]
    sql = "select ChallengerId from Challenger  where ChallengeId = %d and TelegaId = %d"
    value = (ChallengeId, TelegaId)
    mycursor.execute(sql % value)
    IsExist= mycursor.fetchone()
    if IsExist: return 0
    sql = "insert into Challenger (ChallengeID, TelegaId, PersonName) values (%d, %d, \"%s\")"
    value=(ChallengeId, TelegaId, str(PersonName))
    mycursor.execute(sql % value)
    DB_Connector.commit()
    return 1

def PushScore(DB_Connector, ChatId, TelegaId):
    mycursor = DB_Connector.cursor()
    mycursor.execute("select * from Challenge where ChatId=" + str(ChatId))
    IsExist = mycursor.fetchone()
    if not IsExist: return 0
    now = datetime.datetime.today()
    if IsExist[2]:
        if IsExist[2].day == now.day: return 2
    ChallengeId=IsExist[0]
    sql = "update Challenger set Score = Score+1 where ChallengeId = %d and TelegaId = %d"
    value = (ChallengeId, TelegaId)
    mycursor.execute(sql % value)
    sql = "update Challenge set Last_time=\"%s\" where ChallengeId=%d"
    today = datetime.datetime.today()
    value = ( str(today), ChallengeId)
    mycursor.execute(sql % value)
    sql = "update Challenge set CurrentPidor=\"%s\" where ChallengeId=%d"
    value = (TelegaId, ChallengeId)
    mycursor.execute(sql % value)
    DB_Connector.commit()
    ShowMeTheDB(DB_Connector)
    return 1

def GetResult(DB_Connector, ChatId):
    mycursor = DB_Connector.cursor()
    mycursor.execute("select ChallengeId from Challenge where ChatId=" + str(ChatId))
    IsExist = mycursor.fetchone()
    if not IsExist: return 0
    ChallengeId=IsExist[0]
    mycursor.execute("select PersonName, Score, TelegaId from Challenger where ChallengeId=" + str(ChallengeId))
    ChallengeInfo = mycursor.fetchall()
    CurrentPidor=str(mycursor.execute("select CurrentPidor from Challenge where ChatId=" + str(ChatId)))
    Result=(ChallengeInfo, CurrentPidor)
    return Result
    

#CreateDB(ConnectDB("db_Pidor"))    
ShowMeTheDB(ConnectDB("db_Pidor"))
