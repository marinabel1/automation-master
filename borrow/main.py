from borrow.Borrow import Borrow, Newbie, Repeater


def main():
    while True:
        print("""
        ====== borrow tests =======
        Новая анкета
        1. Run all tests
        2. Run Newbie tests
        3. Run Repeater tests
        0. Exit
        """)

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            borrow = Borrow()

        elif choice == 2:
            borrow = Borrow(Newbie)

        elif choice == 3:
            borrow = Borrow(Repeater)

        elif choice == 0:
            break
        else:
            print("Invalid input. Please enter number between 1-4 ")


if __name__ == "__main__":
    main()
