from ticket import create_ticket

def campus_work_flow():
    opt = "0"
    while opt != "5":
        if opt == "0":
           opt = input(
            "====== main menu ======\n"
            "1,   creat ticket\n"
            "2,   view ticket\n"
            "3,   list ticket\n"
            "4,   asign ticket\n"
            "5    exit/invalid transaction\n"
            "\n================================\n"
            "select option 1 - 4\n"
        )
        elif opt == "1":
            create_ticket()
            opt = "0"
        elif opt == "2":
            print("view ticket")
            opt = "0"
        elif opt == "3":
            print("list ticket")
            opt = "0"
        elif opt == "4":
            print("asign ticket")
            opt = "0"
        else:
            print("exist/invalid transaction")

    print("Close program")

campus_work_flow()