###  ATM Simulator (Control Flow)

def atm_simulator():
    balance = 10000000000000000000000000000000
    while True:
        print("\n1. Check Balance\n2. Withdraw\n3. Exit")
        choice = input("Choose: ")
        if choice == '1':
            print(f"Balance: ${balance}")
        elif choice == '2':
            amount = int(input("Enter amount: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn: ${amount}")
            else:
                print("Insufficient funds!")
        elif choice == '3':
            break
        else:
            print("Invalid option!")

atm_simulator()