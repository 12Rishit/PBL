def start():
    import dbinit as d
    import modules as m
    import os

    while True:

        print('||==============Book My Show===================||')
        print('||      You can perform the following tasks    ||')
        print('|| Type 0 to reset Application                 ||')
        print('|| Type 1 to add a hall in your portal         ||')
        print('|| Type 2 to view all the halls in your portal ||')
        print('|| Type 3 to see the booking status of a hall  ||')
        print('|| Type 4 to see booking of all the halls      ||')
        print('|| Type 5 to return to main screen             ||')
        print('||=============================================||')
        choice = m.inputNumber('Enter your choice: ')
        if choice == 0:
            d.dbcon()
        if choice == 1:
            hname = input('Enter your hall name: ')
            fs = m.inputNumber('Enter the maximum front seats: ')
            ms = m.inputNumber('Enter the maximum middle seats: ')
            bs = m.inputNumber('Enter the maximum back seats: ')
            cost = m.inputNumber('Enter cost of a seat: ')
            m.addhall(hname, fs, ms, bs, cost)
        if choice == 2:
            import pandas as pd
            rec = m.hallstat()
            df = pd.DataFrame(rec)
            df.columns = ['Hall No', 'Hall Name', 'Cost of Seat', 'A-Type', 'B-Type', 'C-Type']
            print(df)

        if choice == 3:
            import pandas as pd
            pd.set_option('display.width', 200)
            pd.set_option('display.max_columns', None)
            print('You can get details of the following hall Numbers')
            print(m.hallnums())
            hno = m.inputNumber('Enter a valid hallno: ')
            if hno in m.hallnums():
                try:
                    rec = m.showhallbooking(hno)
                    df = pd.DataFrame(rec)
                    df.columns = ['Hall No', 'Ticket No', 'Customer', 'Hall Name', 'Seat Type', 'Cost_of_Seat',
                                  'No of Seats', 'Discount', 'Total Cost']
                    print(df)
                except:
                    print('No Bookings Found for the Hall Number')

            else:
                print('Invalid Hall Number')
        if choice == 4:
            try:
                import pandas as pd

                pd.set_option('display.max_columns', None)
                pd.set_option('display.width', 200)
                rec = m.allbookings()
                df = pd.DataFrame(rec)
                df.columns = ['Hall No', 'Ticket NO', 'Hall Name', 'Seat Type', 'No of Seats', 'Cost of Seat', \
                              'Discount', 'Total Cost', 'A-Type', 'B-Type', 'C-Type']
                print(df)
            except:
                print('No Bookings Found')


        if choice == 5:
            return
        os.system('pause')
        os.system('cls')