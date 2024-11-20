import mysql.connector as mys
connect = mys.connect(user="root",password="divyansh@1234",host="localhost")
cursor = connect.cursor()
cursor.execute("use nightshade")
print (" NightShade database in use")
print ()

#function break -----------------------------------------------------------------------------
def add_player():

    igid=int(input("Enter player's InGame ID : - "))
    dcid=input("Enter player's Discord ID : - ")
    name=input("Enter player's Name : - ")
    doj=input("Enter player's joining Date (YYYY-MM-DD) : - ")

    q1='insert into player values(%s,%s,%s,%s)'
    data=(igid,dcid,name,doj)

    cursor.execute(q1,data)
    connect.commit()

    print("Player added Succesfully ")

#function break ------------------------------------------------------------------------------

def delete_player():
    print("'NOTE :- data once deleted cannot be undo carefully go forward otherwise fill wrong InGame ID '")
    igid=(input("Enter InGame ID : - "),)

    q2='delete from player where igid = %s'
    data=(igid)

    cursor.execute(q2,data)
    connect.commit()

    print("Player Deleted Succesfully ")

#function break ------------------------------------------------------------------------------

from datetime import datetime

def update_player():
    igid = int(input("Enter player's InGame ID: "))
    dcid = input("Enter player's Discord ID: ")
    name = input("Enter player's Name: ")
    doj = input("Enter player's joining Date (YYYY-MM-DD): ")
    
    try:
        doj = datetime.strptime(doj, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    print("NOTE: InGame ID can't be updated.")
    query = 'UPDATE player SET dcid=%s, name=%s, doj=%s WHERE igid=%s'
    data = (dcid, name, doj, igid)

    cursor.execute(query, data)
    connect.commit()
    print("Player updated successfully.")

    updated_data="New value added "
    cursor.execute(query,data)
    connect.commit()

# function break -----------------------------------------------------------------

def view_player():
    igid=(input("Enter InGame Id to search Player : - "),)
    q3='select * from player where igid = %s'
    data=(igid)

    cursor.execute(q3,data)
    result=cursor.fetchone()

    if result:
        print("Player found:", result)
    else:
        print("Player not found.")
    connect.commit()

#function break --------------------------------------------------------------------------

def main_player():
    print()
    print("Tables in Database: \n \n Player \n Staff \n Events \n Sponser")
    print()
    print("""
========================================
| --------------- PLAYER ------------- |
========================================
| 1 . Add Player                       |
========================================
| 2 . View Player Info                 |
========================================
| 3 . Update Player Info               |
========================================
| 4 . Delete Player Info               |
========================================
| 5 . EXIT                             |
========================================
|    CHOOSE A OPTION FROM ABOVE        |
========================================""")
    choice=int(input("Enter Your Choise from Player Table : - "))
    if choice==1:
        add_player()
    elif choice==2:
        view_player()
    elif choice==3:
        update_player()
    elif choice==4:
       delete_player()
    elif choice==5:
       exit()
    else:
      print("Wrong Choise")

#Table break ==========================================================================================================

def add_staff():

    sigid=int(input("Enter Staff Member's InGame ID : - "))
    sdcid=input("Enter Staff Member's Discord ID : - ")
    sname=input("Enter Staff Member's Name : - ")
    sdoj=input("Enter Staff Member's joining Date (YYYY-MM-DD) : - ")
    spost= input("Enter post of Staff Member ")

    q1='insert into player values(%s,%s,%s,%s,%s)'
    data=(sigid,sdcid,sname,sdoj,spost)

    cursor.execute(q1,data)
    connect.commit()

    print("Staff Member Added Succesfully ")

def delete_staff():
    print("'NOTE :- data once deleted cannot be undo carefully go forward otherwise fill wrong InGame ID '")
    sigid=(input("Enter InGame ID : - "),)

    q2='delete from staff where igid = %s'
    data=(sigid)

    cursor.execute(q2,data)
    connect.commit()

    print("Staff Member  Deleted Succesfully ")

 #function break ----------------------------------------------------------------------------------------

from datetime import datetime

def update_staff():
    sigid = int(input("Enter Staff Member's InGame ID: "))
    sdcid = input("Enter Staff Member's Discord ID: ")
    sname = input("Enter Staff Member's Name: ")
    sdoj = input("Enter Staff Member's joining Date (YYYY-MM-DD): ")
    spost = input("Enter post of Staff Member")
    try:
        sdoj = datetime.strptime(sdoj, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    print("NOTE: InGame ID can't be updated.")
    query = 'UPDATE staff SET sdcid=%s, sname=%s, sdoj=%s, spost=%s WHERE igid=%s'
    data = (sdcid, sname, sdoj, sigid,spost)

    cursor.execute(query, data)
    connect.commit()
    print("Staff Member updated successfully.")

    updated_data="New value added "
    cursor.execute(query,data)
    connect.commit()

# function break -------------------------------------------------------------------------------------

def view_staff():
    sigid=(input("Enter InGame Id to search Staff Member : - "),)
    q3='select * from staff where sigid = %s'
    data=(sigid)

    cursor.execute(q3,data)
    result=cursor.fetchone()

    if result:
        print("Staff Member found:", result)
    else:
        print("Staff Member not found.")
    connect.commit()

# function break -----------------------------------------------------------------------------------------------

def main_staff():
    print("""
========================================
| -------------- STAFF ----------------|
========================================
| 1 . Add Staff Member                 |
========================================
| 2 . View Staff Member Info           |
========================================
| 3 . Update Staff Member Info         |
========================================
| 4 . Delete Staff Member Info         |
========================================
| 5 . EXIT                             |
========================================
|    CHOOSE A OPTION FROM ABOVE        |
========================================""")
    choice=int(input("Enter Your Choise from Staff : - "))
    if choice==1:
        add_staff()
    elif choice==2:
        view_staff()
    elif choice==3:
        update_staff()
    elif choice==4:
       delete_staff()
    elif choice==5:
       exit()
    else:
      print("Wrong Choise")

# table break =================================================================================================

def add_events():

    eno=int(input("Enter Event Number : - "))
    ename=input("Enter Event Name : - ")
    edate=input("Enter Date of the Events (YYYY-MM-DD) : - ")
    eresult=input("Enter Result of Event : - ")

    q1='insert into events values(%s,%s,%s,%s)'
    data=(eno,ename,edate,eresult)

    cursor.execute(q1,data)
    connect.commit()

    print("Event added Succesfully ")

# function Break -----------------------------------------------------------------------------------------------

from datetime import datetime

def update_events():
    eno = int(input("Enter Event Number : - "))
    ename = input("Enter Event Name : - ")
    edate = input("Enter Date of the Event (YYYY-MM-DD): ")
    eresult = input("Enter Staff Member's Name: ")

    try:
        edate = datetime.strptime(edate, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    print("NOTE: Event Number can't be updated.")
    query = 'UPDATE events SET ename=%s, edate=%s, eresult=%s WHERE eno=%s'
    data = (eno,ename,edate,eresult)

    cursor.execute(query, data)
    connect.commit()
    print("Event updated successfully.")

    updated_data="New value added "
    cursor.execute(query,data)
    connect.commit()

# function Break --------------------------------------------------------------------------------------

def view_events():
    eno=(input("Enter Event No  : - "),)
    q3='select * from events where eno = %s'
    data=(eno)

    cursor.execute(q3,data)
    result=cursor.fetchone()

    if result:
        print("Event found:", result)
    else:
        print("Event not found.")
    connect.commit()

# function Break -----------------------------------------------------------------------------------------

def main_events():
    print("""
========================================
| --------------- EVENTS --------------|
========================================
| 1 . Add Event                        |
========================================
| 2 . View Event Info                  |
========================================
| 3 . Update Event Info                |
========================================
| 4 . EXIT                             |
========================================
|    CHOOSE A OPTION FROM ABOVE        |
========================================""")
    choice=int(input("Enter Your Choise from Event : - "))
    if choice==1:
        add_events()
    elif choice==2:
        view_events()
    elif choice==3:
        update_events()
    elif choice==4:
        exit()
    else:
      print("Wrong Choise")

# table break =========================================================================================

def add_sponsor():

    spno=int(input("Enter sponsor Number : - "))
    spname=input("Enter sponsor Name : - ")
    offer=input("Enter offer of sponsor : - ")
    spdate=input("Enter Date of Sponsor offer (YYYY-MM-DD) : - ")

    q1='insert into sponsor values(%s,%s,%s,%s)'
    data=(spno,spname,offer,spdate)

    cursor.execute(q1,data)
    connect.commit()

    print("Sponsor added Succesfully ")

# function break ---------------------------------------------------------------------------------------

from datetime import datetime

def update_sponsor():
    spno = int(input("Enter sponsor number : - "))
    spname = input("Enter name of the sponsor : - ")
    offer = input("Enter sponsor offer: -")
    spdate = input("Enter date of sponsor (YYYY-MM-DD): ")
    

    try:
        spdate = datetime.strptime(spdate, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    print("NOTE: Event Number can't be updated.")
    query = 'UPDATE sponsor SET spname=%s, offer=%s, spdate=%s WHERE spno=%s'
    data = (spno,spname.offer,spdate)

    cursor.execute(query, data)
    connect.commit()
    print("sponsor updated successfully.")

    updated_data="New value added "
    cursor.execute(query,data)
    connect.commit()

# function break -----------------------------------------------------------------------------------------

def view_sponsor():
    spno=(input("Enter sponsor No  : - "),)
    q3='select * from sponsor where spno=%s'
    data=(spno)

    cursor.execute(q3,data)
    result=cursor.fetchone()

    if result:
        print("sponsor found:", result)
    else:
        print("sponsor not found.")
    connect.commit()

# function break -----------------------------------------------------------------------------------------------------


def main_sponsor():
    print("""
========================================
| -------------- SPONSER --------------|
========================================
| 1 . Add sponser                      |
========================================
| 2 . View sponser Info                |
========================================
| 3 . Update sponser Info              |
========================================
| 4 . EXIT                             |
========================================
|    CHOOSE A OPTION FROM ABOVE        |
========================================""")
    choice=int(input("Enter Your Choise from Sponser : - "))
    if choice==1:
        add_sponsor()
    elif choice==2:
        view_sponsor()
    elif choice==3:
        update_sponsor()
    elif choice==4:
        exit()
    else:
      print("Wrong Choise")

# Code Break ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



while True:
    loggin=input("Enter password to unlock software for use :- ")
    if loggin=='a':
        print()
        print("""
========================================
| --------- Game Team Manager ---------|
========================================
| 1 . PLAYER                           |
========================================
| 2 . STAFF                            |
========================================
| 3 . EVENTS                           |
========================================
| 4 . SPONSOR                          |
========================================
| 5. EXIT                              |
========================================
|    CHOOSE A OPTION FROM ABOVE        |
========================================""")
        print()
        fnchose = int(input("Enter you choise here : - "))
        if fnchose==1:
            main_player()
        elif fnchose==2:
            main_staff()
        elif fnchose==3:
            main_events()
        elif fnchose==4:
            main_sponsor()
        elif fnchose==5:
            exit()
        else:
            continue
    else:
        continue
