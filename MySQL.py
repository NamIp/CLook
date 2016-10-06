import mysql.connector
from mysql.connector import errorcode

def create_connection():
    try:
        cnx = mysql.connector.connect(user='root', password='Namrata1', host = 'localhost',port='3306',
                                database='coursera')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return cnx  

def create_table():
    cursor = cnx.cursor()
    sql = """CREATE TABLE Courses (
         id  varchar(1000) PRIMARY KEY,
         name  varchar(1000) NOT NULL,
         partnerLogo varchar(1000),  
         photoUrl varchar(1000),
         description varchar(5000) NOT NULL,
         startDate DateTime,
         -- domainID varchar(1000) NOT NULL,
         -- subdomainID varchar(1000)
     )"""
    cursor.execute(sql)

def drop_column(cnx):
    cursor = cnx.cursor()
    cursor.execute(" ALTER TABLE Courses DROP COLUMN subdomainID")
    

cnx=create_connection()
#create_table()
drop_column(cnx)
cnx.close()