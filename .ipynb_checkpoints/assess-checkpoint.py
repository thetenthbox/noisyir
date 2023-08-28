def manipulate_strings(original_strings, number_list):
    manipulated_strings = []
    manipulate = original_strings
    for numbers in number_list:
        # Use list comprehension to rearrange the strings based on the current number list
        new_strings = [manipulate[i - 1] for i in numbers]
        manipulated_strings.append(new_strings)
        manipulate = new_strings
    return manipulated_strings

def main():
    original_strings = []
    number_list = []

    while True:
        print("\nMenu:")
        print("1. Enter 4 different strings to form the original list")
        print("2. Enter a list of numbers for manipulation")
        print("3. Perform manipulation")
        print("4. Print the current strings")
        print("5. Go back to the previous manipulation")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            original_strings = []
            for i in range(4):
                string = input(f"Enter string {i + 1}: ")
                original_strings.append(string)

        elif choice == "2":
            n = int(input("Enter the number of manipulations: "))
            number_list = []
            for i in range(n):
                numbers = input(f"Enter manipulation {i + 1} (e.g., 3 4 2 1): ").split()
                number_list.append([int(num) for num in numbers])

        elif choice == "3":
            if not original_strings:
                print("Please enter the original strings first.")
            elif not number_list:
                print("Please enter the list of numbers for manipulation first.")
            else:
                result = manipulate_strings(original_strings, number_list)
                original_strings = result[-1]
                print("Manipulation complete. Current strings:", original_strings)

        elif choice == "4":
            if not original_strings:
                print("Original strings have not been entered yet.")
            else:
                print("Current strings:", original_strings)

        elif choice == "5":
            if len(number_list) > 1:
                # Remove the last manipulation and set the current strings to the previous manipulation result
                number_list.pop()
                original_strings = manipulate_strings(original_strings, number_list)[-1]
                print("Returned to the previous manipulation.")

        elif choice == "6":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
