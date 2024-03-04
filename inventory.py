from tabulate import tabulate


class Shoe:
    for_sale = False

    # Constructor method with instance variables 'country', 'code', 'product', 'cost' and 'quantity'.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # This method changes the 'for_sale' parameter to True
    def mark_for_sale(self):
        self.for_sale = True


# Thw function below reads from the file the user entered.
# The for loop within the with statement iterates through each line in the 'f' which is the file.
# Each line is split where there is a comma and these iterations are appended to 'products_inner' which then creates
# a nested list which is returned when this function is called.
def read_data(file_input):
    products_inner = []

    with open(file_input, 'r') as f:
        next(f)     # Used to skip first line
        for line in f:
            products_inner.append(line.strip('\n').split(','))

    return products_inner


# The function below returns the information of the product if the code the user entered is in 'list_input'
def find_shoe(code_input, list_input):
    # The for loop below iterates through 'list_input'.
    for i in list_input:
        if i.code == code_input:
            print(f"Country: {i.country} - Code: {i.code} - Product: {i.product} - Cost: {i.cost} - Quantity:"
                  f" {i.quantity}")


# The function below calculates the total stock worth of each of product
def value_per_item(list_input):
    value_list = []
    # The for loop below iterates through 'list_input'.
    # The values at index value i[3] and i[4] are multiplied and appended to 'value_list'
    for i in list_input:
        value_list.append(int(i[3]) * int(i[4]))

    return value_list


file = None

while True:
    # The exception block below ensures that the user inputs a valid file name.
    try:
        file_name = input("Enter the files name - eg. 'input.txt': ")
        file = open(file_name, 'r')
    except FileNotFoundError as error:
        print("The file that you are trying to open does not exist.")
        print(error)
    # The finally block is used to close the file and to read from 'file' and display its contents.
    finally:
        if file is not None:
            # 'products_outer' contains the list of content in 'file'
            products_outer = []

            # The with statement below reads from a certain file dependent on what the user entered as the name
            with open(file_name, 'r') as f:
                # The for loop below iterates through each line and appends each line to 'products_outer'
                for line in f:
                    products_outer.append(line.strip('\n'))

            # The if statement below checks whether the specified content is inside 'products_outer' to ensure that the
            # correct contents are being read.
            if 'Country,Code,Product,Cost,Quantity' not in products_outer:
                print("Cannot read the contents from this file. ")
            else:
                # 'file_shoes' stores what is returned from the 'read_data' function which has 'file_name'
                # as a parameter.
                file_shoes = read_data(file_name)
                file.close()
                break

shoe_objects = []

# The for loop below iterates through 'file_shoes' and appends each iteration in 'file_shoes' as 'Shoe' objects to
# 'shoe_objects'
for i in file_shoes:
    shoe_objects.append(Shoe(i[0], i[1], i[2], i[3], i[4]))

quantity_list = []
shoe_codes = []

# The for loop below iterates through 'shoe_objects' and appends the value in the 'quantity' parameter to
# 'quantity_list and also appends the value in the 'code' parameter' to 'shoe_codes.
for i in shoe_objects:
    quantity_list.append(int(i.quantity))
    shoe_codes.append(i.code)

menu_option = ''

# The while loop continuously executes until the user inputs 5
while menu_option != 5:
    # The try and except ensures that the user inputs an integer
    try:
        menu_option = int(input("Select one of the options below:\n1. Search for product using code\n"
                                "2. Determine product with the lowest cost and restock\n"
                                "3. Determine the product with the highest quantity and mark it up as being for sale\n"
                                "4. View inventory\n5. Quit\n"))
        # The if/elif/else statements below ensure that the user chooses the correct option
        if menu_option == 1:
            # Functionality to search product by code
            # The user is prompted to enter the code of the product they would like to access
            user_code = input("Enter the code of the shoe: ")
            # The while loop below ensures that the code is inside 'shoe_codes'
            while user_code not in shoe_codes:
                user_code = input(
                    "Invalid product code. Enter the code of the shoe: ")
            # 'file_shoes' stores what is returned from the 'read_data' function which has 'file_name'
            # as a parameter.
            # 'user_code' and 'shoe_objects' are placed in the parameters of 'find_shoe'
            find_shoe(user_code, shoe_objects)
        elif menu_option == 2:
            # Code to determine the lowest quantity and restock it
            # The for loop below iterates through 'shoe_objects'.
            # The if statement checks whether the minimum value is equal to the value in the parameter 'quantity' is
            # the same and outputs the details of the products.
            for i in shoe_objects:
                if min(quantity_list) == int(i.quantity):
                    print(f"Country: {i.country} - Code: {i.code} - Product: {i.product} - Cost: {i.cost} - "
                          f"Quantity: {i.quantity}")

            count = 0
            # The for loop below iterates through 'file_shoes'.
            # The if statement checks whether the minimum of 'quantity_list' is the same as the index position i[4] in
            # 'file_shoes' and replaces adds 100 to the current value.
            for i in file_shoes:
                if min(quantity_list) == int(i[4]):
                    file_shoes[count][4] = int(i[4]) + 100
                count += 1

            # The with statement below overwrites 'inventory.txt'
            with open('inventory.txt', 'w') as f:
                f.write('Country,Code,Product,Cost,Quantity\n')
                # The for loop below iterates through 'file_shoes' and writes each iteration in a certain format
                # to 'inventory.txt'
                for i in file_shoes:
                    f.write(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n')

            print("Item(s) have been restocked.")
        elif menu_option == 3:
            # Code to determine the product with the highest quantity and mark it up as being for sale.
            # The for loop below iterates through 'shoe_objects'.
            # The if statement checks whether the maximum value is equal to the value in the parameter 'quantity' is
            # the same and outputs the details of the products.
            # The specific product is marked as for sale.
            for i in shoe_objects:
                if max(quantity_list) == int(i.quantity):
                    print(
                        f"Country: {i.country} - Code: {i.code} - Product: {i.product} - Cost: {i.cost} - "
                        f"Quantity: {i.quantity}")
                    i.mark_for_sale()

            print("Item(s) is up for sale.")
        elif menu_option == 4:
            # The 'total_worth' stores the function 'value_per_item' and has 'file_shoes' as a parameter
            total_worth = value_per_item(file_shoes)

            count = 0
            # The for loop below iterates through 'file_shoes' and appends each iteration in 'total_worth' to
            # the corresponding x iteration.
            for x in file_shoes:
                x.append(str(total_worth[count]))
                count += 1

            tabulate_list = [
                ['Country', 'Code', 'Product', 'Cost', 'Quantity', 'Value']]

            # The for loop below iterates through 'file_shoes' and appends i to it.
            for i in file_shoes:
                tabulate_list.append(i)

            # The tabulate function is used to display the content in the list in table format.
            print(tabulate(tabulate_list, headers="firstrow", tablefmt="github"))
        elif menu_option == 5:
            print("Exiting program!")
        else:
            print("Invalid Option!")
    except ValueError:
        print('Invalid Input!')

# references
# https://pypi.org/project/tabulate/
