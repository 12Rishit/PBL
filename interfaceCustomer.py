def start():

    import modules as m
    import os

    while True:

        print('||==============Book My Show===================||')
        print('||      You can perform the following tasks    ||')
        print('|| Type 1 to view all the halls in your portal ||')
        print('|| Type 2 to book a ticket in a hall           ||')
        print('|| Type 3 to generate ticket for booking       ||')
        print('|| Type 4 to return to main screen             ||')
        print('||=============================================||')
        choice = m.inputNumber('Enter your choice: ')
        if choice == 1:
            import pandas as pd

            rec = m.hallstat()
            df = pd.DataFrame(rec)
            df.columns = ['Hall No', 'Hall Name', 'Cost of Seat', 'A-Type', 'B-Type', 'C-Type']
            print(df)
        if choice == 2:
            import pandas as pd

            print('You have the following hall Numbers')
            print(m.hallnums())
            hno = m.inputNumber('Enter a valid hallno: ')
            cname = input('Enter Customer name: ')
            stype = input('Enter Seat Type as A,B,C: ')
            noseat = m.inputNumber('Enter number of seats: ')
            cost = m.getCost(hno)[0][0]
            # print(cost)
            cost *= noseat
            dis = 0
            if cost >= 2000:
                dis = 100
            m.booking(hno, cname, noseat, cost, stype, dis)

        if choice == 3:
            tno = m.inputNumber('Enter the ticket number: ')
            rec = m.getticketdet()
            if tno in rec:
                rec = m.printticket(tno)
                print("---------Ticket Details-----------")
                print("Ticket Number is   :%d" % (rec[0][0]))
                print("Hall Number is     :%d" % (rec[0][1]))
                print("Hall Name          :%s" % (rec[0][2]))
                print('Customer name is   :%s' % (rec[0][3]))
                print('Seat Type          :%s' % (rec[0][4]))
                print("Number of Seats    :%d" % (rec[0][5]))
                print("Cost per Seat      :%d" % (rec[0][6]))
                print("Discount           :%d" % (rec[0][7]))
                print("Total Cost         :%d" % (rec[0][8]))
                # print(rec)
            else:
                print('Ticket Number not available')

        if choice == 4:
            return

        os.system('pause')
        os.system('cls')