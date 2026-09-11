print("==============================================")
print(" Welcome to Pattern Generator and Number Analyzer")
print("==============================================")

while True:

    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        while True:
            rows = int(input("Enter the number of rows for the pattern: "))

            if rows <= 0:
                print("Invalid row count! Please enter a positive number.")
                continue

            break

        print("\nRight-Angled Triangle:")

        # Nested loops
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == "2":

        while True:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            if end <= start:
                print("Invalid range! End number must be greater than start number.")
                continue

            break

        print("\nNumber Analysis:")

        total = 0

        # Using range() and for loop
        for number in range(start, end + 1):

            if number % 2 == 0:
                print("Number", number, "is Even")
            else:
                print("Number", number, "is Odd")

            total = total + number

        print("\nSum of all numbers from", start, "to", end, "is:", total)

    elif choice == "3":

        print("\nThank you for using Pattern Generator and Number Analyzer!")
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue


    print("----"*40)
