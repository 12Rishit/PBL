#Function to return the number of seats available in a hall

def getseats(hno):
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT frontseats, midseats, backseats FROM hall_det WHERE hallno='%d'" % (hno)
        mycursor.execute(sql)
        rec = mycursor.fetchone()
        con.close()
    except myc.Error as err:
        print(err)
    finally:
        return rec

#Function to get all the hall numbers
def hallnums():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT hallno FROM hall_det ORDER BY hallno"
        mycursor.execute(sql)
        rec = mycursor.fetchall()
        hlst =[]
        for x in rec:
            hlst.append(x[0])
    except myc.Error as err:
        print(err)
    finally:
        con.close()
        return hlst

#Function to get all ticket numbers
def getticketdet():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT ticketno FROM booking_det"
        mycursor.execute(sql)
        rec = mycursor.fetchall()
        tlst =[]
        for x in rec:
            tlst.append(x[0])
    except myc.Error as err:
        print(err)
    finally:
        con.close()
        return tlst

#Function to update the seats based on bookings
def updateseats(hno,stype,amt):
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        if stype=='A':
            sql = "UPDATE hall_det SET frontseats=frontseats-'%d' WHERE hallno='%d'" % (amt,hno)
        if stype=='B':
            sql = "UPDATE hall_det SET midseats=midseats-'%d' WHERE hallno='%d'" % (amt,hno)
        if stype=='C':
            sql = "UPDATE hall_det SET backseats=backseats-'%d' WHERE hallno='%d'" % (amt,hno)
        mycursor.execute(sql)
        con.commit()    
    except myc.Error as err:
        print(err)
    finally:
        print('Seats updated')
        con.close()
    
#Function to book the seats and also call update seats function     
def booking(hno, cname,noseat, cost,stype, disc):
    import mysql.connector as myc
    s1,s2,s3=getseats(hno)
    if (stype=='A' and noseat>s1) or (stype=='B' and noseat>s2) or (stype=='C' and noseat>s3):
        print('Requested number of seats not available, please try again')
    else:
        try:
            con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
            mycursor=con.cursor()
            cost = cost - disc
            sql="INSERT INTO booking_det(hallno,customer,no_of_seats,seattype, discount,total_cost) \
            VALUES(%s,%s,%s,%s,%s,%s)"
            rows=[(hno, cname,noseat,stype, disc,cost)]
            mycursor.executemany(sql,rows)
            con.commit()
            #update the seats after booking
            updateseats(hno,stype,noseat)
            tno = getticketno()[0][0]
            print('Booking success, your ticket number is : ' + str(tno))
        except myc.Error as err:
            print(err)
        finally:

            con.close()     
#booking(101,1001,'Ashok',4,500,'A',0)  

#Function to display booking details for a given hall
def showhallbooking(hno):
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT b.hallno, b.ticketno,b.customer,h.hallname, b.seattype,h.cost_of_seat, b.no_of_seats,b.discount,b.total_cost\
        FROM booking_det b, hall_det h WHERE b.hallno=h.hallno and b.hallno='%d'" % (hno)
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(showhallbooking(1001))

#Function to print the hall status
def hallstat():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT * FROM hall_det"
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(hallstat())  
#function to display all bookings
def allbookings():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT b.hallno, b.ticketno, h.hallname, b.seattype, b.no_of_seats,h.cost_of_seat, b.discount,b.total_cost,\
        h.frontseats, h.midseats, h.backseats FROM booking_det b, hall_det h WHERE b.hallno=h.hallno"
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(allbookings())

def addhall(hname, fs,ms,bs,cost):

    try:

        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql="INSERT INTO hall_det(hallname, frontseats, midseats, backseats,cost_of_seat) VALUES(%s,%s,%s,%s,%s)"
        rows=[(hname,fs,ms,bs,cost)]
        mycursor.executemany(sql,rows)
        con.commit()

    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:

        print('Hall added')
        con.close()
#addhall(1005,'VAISHNAVI-SAPPHIRE', 100,100,100) 

def printticket(tno):
    
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd='pranav1401', database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT b.ticketno, b.hallno, h.hallname, b.customer,b.seattype, b.no_of_seats,h.cost_of_seat, b.discount,b.total_cost\
        FROM booking_det b, hall_det h WHERE b.hallno=h.hallno and b.ticketno='%d'" % (tno)
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(printticket(101))  

#Function to enforce integer input. Use this while accepting integers
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break

def getCost(hallno):
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd = 'pranav1401',database = 'cinemaproj')
        mycursor = con.cursor()
        sql = "select cost_of_seat from hall_det where hallno = '%d'" %(hallno)
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
def getticketno():
    import mysql.connector as myc
    con = myc.connect(host='localhost', user='root', passwd='pranav1401', database='cinemaproj')
    mycursor = con.cursor()
    sql = "SELECT ticketno FROM booking_det ORDER BY ticketno DESC LIMIT 1;"
    mycursor.execute(sql)
    rec = mycursor.fetchall()
    return rec
