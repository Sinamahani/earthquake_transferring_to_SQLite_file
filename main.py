from database_filling.database import eq_transfer


def menu():
    print("""Please Enter the order you want
    a. Transfering historical data
    b. Transfering data related 1900-1960
    c. Transfering data related 1960-1970
    q. for exit""")
    User_Input = input("Enter your command: ")
    if User_Input == 'q':
        print("\nHope to see you again.")


    while User_Input != 'q':
        if User_Input == '1':
            your_input = 'Catoalog_2000.csv'
            eq_class = eq_transfer(your_input)
            eq_class.open_data_hist()
            eq_class.data_transfer_hist
        elif User_Input == '2':
            your_input = 'Catoalog_1900.csv'
            eq_class = eq_transfer(your_input)
            eq_class.open_data_hist()
            eq_class.data_transfer_1900
        elif User_Input == '3':
            your_input = 'Catoalog_1963.csv'
            eq_class = eq_transfer(your_input)
            eq_class.open_data_hist()
            eq_class.data_transfer_1963
        else:
            print("you have entered a wrong input".upper())
        print("""Please Enter the order you want
                a. Transfering historical data
                b. Transfering data related 1900-1960
                c. Transfering data related 1960-1970""")
        User_Input = input("Enter your command: ")

#RUN THE FILE
menu()




