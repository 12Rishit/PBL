def dbcon():
    # Initial Script to create database schema
    import mysql.connector as myc
    import random
    try:
        con = myc.connect(host='localhost',user='root',passwd='pranav1401')
        mycursor = con.cursor()
        mycursor.execute('DROP DATABASE IF EXISTS cinemaproj')
        mycursor.execute('CREATE DATABASE cinemaproj')
        mycursor.execute('USE cinemaproj')
        mycursor.execute('DROP TABLE IF EXISTS hall_det')
        sql = '''CREATE TABLE hall_det(
                    hallno INT(5) PRIMARY KEY AUTO_INCREMENT,
                    hallname VARCHAR(20) NOT NULL,
                    cost_of_seat INT(4) NOT NULL,
                    frontseats INT(3) NOT NULL,
                    midseats INT(3) NOT NULL,
                    backseats INT(3) NOT NULL)'''
        mycursor.execute(sql)
        mycursor.execute('DROP TABLE IF EXISTS booking_det')
        sql = '''CREATE TABLE booking_det(
                    ticketno INT(5) PRIMARY KEY AUTO_INCREMENT,
                    hallno INT(5) NOT NULL,
                    customer VARCHAR(15) NOT NULL,
                    no_of_seats INT(2) NOT NULL,
                    seattype CHAR(1) NOT NULL,
                    discount INT(3) NULL,
                    total_cost INT(3) NOT NULL,
                    CONSTRAINT FOREIGN KEY(hallno) 
                    REFERENCES hall_det(hallno))'''
        mycursor.execute(sql)

        #Inserting Rows in to the Cinema hall table
        sql = """INSERT INTO hall_det(hallno, hallname,cost_of_seat, frontseats, midseats,backseats)
        VALUES(%s, %s,%s, %s, %s, %s)"""
        rows = [(1001,'PVR-YPR',random.randint(150,250),50,50,50)]
        mycursor.executemany(sql, rows)
        sql = """INSERT INTO hall_det( hallname,cost_of_seat, frontseats, midseats,backseats)
                VALUES(%s,%s, %s, %s, %s)"""
        rows = [('INOX-MANTRI',random.randint(150,250), 50, 50, 50), \
          ('PVR-GOP',random.randint(150,250), 50, 50, 50), ('PHOENIX',random.randint(150,250), 60, 50, 50)]
        mycursor.executemany(sql, rows)
        con.commit()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        print('Database schema Created')
        con.close()
