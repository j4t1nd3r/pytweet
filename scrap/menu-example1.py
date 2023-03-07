def menu():
    print("[1] Opt 1")
    print("[2] Opt 2")
    print("[3] Opt 3")

menu()
option = int(input("Enter an option: "))

while option != 0:
    if option == 1:
        print("option 1 has been picked")
        def menu():
            print("[1] Opt 1")
            print("[2] Opt 2")
        menu()
        option = int(input("Enter an option: "))    
    elif option == 2:
        print("option 2 has been picked")
    elif option == 3:
        print("option 3 has been picked")
    else:
        print("invalid option.")

    print()
    menu()
    option = int(input("Enter an option: "))

print("end program")