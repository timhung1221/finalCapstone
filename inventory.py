
from tabulate import tabulate


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    # Return the code of the shoe.
    def get_code(self):
        return self.code

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    def str(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    inventory_file = None
    try:
        inventory_file = open("inventory.txt", "r")
        inventory_lines = inventory_file.readlines()

        for i in range(1, len(inventory_lines)):
            inventory_lines[i] = inventory_lines[i].replace("\n", "")
            lines_split = inventory_lines[i].split(",")
            shoe = Shoe(lines_split[0], lines_split[1], lines_split[2], lines_split[3], lines_split[4])
            shoe_list.append(shoe)

    except FileNotFoundError as error:
        print(f"Open file error: {error}")

    finally:
        if inventory_file is not None:
            inventory_file.close()
    print("Read data has finised!")


# Define a function to get message from user.
def input_message(subject):
    in_message = ""
    while len(in_message) == 0:
        in_message = input(subject)
    return in_message


# Define a function to get a number from user.
def input_number(subject):
    num = ""
    while not num.isdigit():
        num = input(subject)
    return int(num)


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("Please input 5 items below to append data in shoe list.")
    country = input_message("Input the country of shoe: ")
    code = input_message("Iput the code of shoe: ").upper()
    product = input_message("Input the product of shoe: ")
    cost = input_number("Input the cost of shoe(digit): ")
    quantity = input_number("Input the quantity of shoe(digit): ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    # Update new data in file.
    data = "Country,Code,Product,Cost,Quantity\n"            
    for i in range(0, len(shoe_list)):
        data += (shoe_list[i].str() + "\n")
    update_data(data)

    print("Capture shoe data has finished!")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''
    if len(shoe_list) > 0:
        table_header = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
        table_data = []
        for object in shoe_list:
            table_data.append(object.str())
        print("'Country', 'Code', 'Product', 'Cost', 'Quantity'")
        print(tabulate(table_data)) #, headers=table_header)) #, tablefmt='grid'))
    else:
        print("No data found!")

# Define a function to update data in file.
def update_data(data):
    file = None
    try:
        file = open("inventory.txt", "w")
        file.write(data)
    except FileExistsError as error:
        print(f"Open file to write data error: {error}")
    finally:
        if file is not None:
            file.close()


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if len(shoe_list) > 0:
        # 1) Define a dict to store information from shoe object. key is code, value is quantity.
        shoe_dict = {}
        
        for object in shoe_list:
            shoe_dict[object.get_code()] = int(object.get_quantity())

        # 2) Sort dict.
        sort_shoe_dict = dict(sorted(shoe_dict.items(), key=lambda x: x[1]))

        # 3) The 1st item is lowest quantity value.
        lowest_code = ""
        lowest_quantity = 0
        for key, value in sort_shoe_dict.items():
            lowest_code = key
            lowest_quantity = value
            break

        # 4) Ask the user if they want to be re-stocked.
        print(f"The shoe's code {lowest_code}, quantity is lowest: {lowest_quantity}, waiting for re-stock.")
        choice_message = ""
        while True:
            choice_message = input_message("Do you want to re-stocked for this shoe? Choose 'y'(Yes) or 'n'(No) please.")
            if choice_message == 'y' or choice_message == 'n':
                break
        if choice_message == 'y':
            choice_number = input_number("Please input a number to be re-stocked this shoe: ")
            

            # 5) Confirm need re-stock by the user, then update shoe object list and update the file.
            for i in range(0, len(shoe_list)):
                if lowest_code ==  shoe_list[i].get_code(): # Delete old object in list
                    split_items = shoe_list[i].str().split(",")
                    del shoe_list[i]  
                    break
            
            # 6) Append new object in list.
            shoe_list.append(Shoe(split_items[0], split_items[1], split_items[2], split_items[3], choice_number))

            # 7) Update new data in file.
            data = "Country,Code,Product,Cost,Quantity\n"            
            for i in range(0, len(shoe_list)):
                data += (shoe_list[i].str() + "\n")
            
            update_data(data)
            print("Re-stock has finished!")
        else:
            print("No action to re-stock.")
        
    else:
        print("No data found!")    


def search_shoe(code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    if len(shoe_list) > 0:
        return_str = ""
        for object in shoe_list:
            if code.upper() == object.get_code():
                return_str = object.str()
                print(f"The shoe's {code} has been found and the information is: {object.str()}")
        if len(return_str) == 0:
            print(f"No data found by this {code}!")
    else:
        print("No data found!")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    if len(shoe_list) > 0:
        for object in shoe_list:
            print(f"The shoe code: {object.get_code()}, it's total value is: {int(object.get_cost()) * int(object.get_quantity())}")
    else:
        print("No data found!")    


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if len(shoe_list) > 0:
        # 1) Define a dict to store information from shoe object. key is code, value is quantity.
        shoe_dict = {}
        
        for object in shoe_list:
            shoe_dict[object.get_code()] = int(object.get_quantity())

        # 2) Sort dict.
        sort_shoe_dict = dict(sorted(shoe_dict.items(), key=lambda x: x[1], reverse=True))

        # 3) The 1st item is highest quantity value.
        highest_code = ""
        highest_quantity = 0
        for key, value in sort_shoe_dict.items():
            highest_code = key
            highest_quantity = value
            break

        print(f"The shoe's {highest_code}, stock is highest: {highest_quantity}, waiting for sale.")
    else:
        print("No data found!")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main_menu():

    print(" ------------------ Main Menu -----------------------------------")
    print(" rd: Read all data out from file and put it in shoe list.")
    print(" cs: Caputure one shoe data from user and add it in shoe list.")
    print(" va: View all data from the shoe list.")
    print(" rs: Find the lowest quantity of shoe and ask to re-stock.")
    print(" ss: Search one shoe data by code.")
    print(" vv: View every shoe's value, value = cost x quantity")
    print(" hq: Find the highest quantity of shoe.")
    print(" q:  Quit.")
    print(" ----------------------------------------------------------------")



# Define main function entry.
def main():
    while True:
        main_menu()
        user_choice = input("Please choose one item from list to run application: ")
        print()
        if user_choice == "rd":
            read_shoes_data()
        elif user_choice == "cs":
            capture_shoes()
        elif user_choice == "va":
            view_all()
        elif user_choice == "rs":
            re_stock()
        elif user_choice == "ss":
            code = input_message("Please input the code of product to search information: ")
            search_shoe(str(code))
        elif user_choice == "vv":
            value_per_item()
        elif user_choice == "hq":
            highest_qty()
        elif user_choice == "q":
            print("*************** Goodbye *****************")
            break
        else:
            print("Choose error, try again!")
        print()


if __name__ == '__main__':
    main()

