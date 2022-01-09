#PasswordValut

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='PasswordValut'
)
myCursor = db.cursor()

#myCursor.execute("CREATE TABLE Vault(name varchar(50), userName varchar(50) NOT NULL, pass varchar(50)NOT NULL)")
'''myCursor.execute("INSERT INTO Vault(name, userName, pass) VALUES(%s, %s, %s)", ('Rashmi', 'moti_atma', 'test1432'))
        db.commit()
    myCursor.execute("select * from Vault")
    for x in myCursor:
        print(x)'''

def getPass(uid):
    try:
        uid = f"'{uid}'"  #Just adding '' around the name so it goes as 'userName' in the query
        myCursor.execute(f"SELECT pass FROM Vault WHERE userName={uid}")
        return str(myCursor.fetchone())[2:-3]
    except:
        print('error')

def authenticate(uname, password):
    pword = getPass(uname)
    if password == '':
        return('False')
    else:
        if password == pword:
            return('True')
        else:
            return('False')

authenticate('moti_atma', 'test1432')

'''if __name__=='__main__':
    uname = str(input("Enter Username: "))
    password = input('Enter the password: ')

    a = getPass(uname)
    if a == password:
        print("Ok")
    else:
        print("Hattttttttt")'''