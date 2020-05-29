import pyodbc
import datetime

driver = ""
server = ""
database = ""
user = ""
password = ""

todayraw = datetime.datetime.today()
firstdayraw = todayraw - datetime.timedelta(days=30)
today = todayraw.strftime("%Y%m%d")
firstday =firstdayraw.strftime("%Y%m%d")

def satinalmaOnaysizGetir(ilkTarih=firstday, sonTarih=today):
    cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=user, password=password)
    cursor = cnxn.cursor()
    try:
        cursor.execute("SET NOCOUNT ON; exec dbo.sp_SiparisOperasyonlari 1,?,?,0,0,0,0,0,0,N'',1,N'',1,1,2,1,0", (ilkTarih, sonTarih))
        result = cursor.fetchall()        
        return result    

    except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            return sqlstate


def satinalmaOnayliGetir(ilkTarih=firstday, sonTarih=today):
    cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=user, password=password)
    cursor = cnxn.cursor()
    try:
        cursor.execute("SET NOCOUNT ON; exec dbo.sp_SiparisOperasyonlari 1,?,?,0,0,1,0,0,0,N'',1,N'',0,1,2,1,0", (ilkTarih, sonTarih))
        result = cursor.fetchall()        
        return result    

    except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            return sqlstate 


def satinalmaReddedilenGetir(ilkTarih=firstday, sonTarih=today):
    cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=user, password=password)
    cursor = cnxn.cursor()
    try:
        cursor.execute("SET NOCOUNT ON; exec dbo.sp_SiparisOperasyonlari 1,?,?,1,0,0,0,0,0,N'',1,N'',1,1,2,1,0", (ilkTarih, sonTarih))
        result = cursor.fetchall()        
        return result    

    except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            return sqlstate

def satinalmaOnayla(id, userid):
    cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=user, password=password)
    cursor = cnxn.cursor()
    try:
        cursor.execute("UPDATE SIPARISLER SET sip_lastup_date=?,sip_OnaylayanKulNo=?,sip_cagrilabilir_fl=1 Where sip_RECno = ?", (datetime.datetime.now(),userid, id))
        cnxn.commit()
        
    except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            return sqlstate 


def satinalmaOnayIptal(id):
    cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=user, password=password)
    cursor = cnxn.cursor()
    try:
        cursor.execute("UPDATE SIPARISLER SET sip_lastup_date=?,sip_OnaylayanKulNo=0,sip_cagrilabilir_fl=0 Where sip_RECno = ?", (datetime.datetime.now(),id))
        cnxn.commit()
        
    except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            return sqlstate 