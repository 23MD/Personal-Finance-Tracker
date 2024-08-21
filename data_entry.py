# This file will collect data from the user, includes all the input. 
# All the function to collect data from the user 
# and interact with the user will be written here.
# So that our code is cleaner.abs

from datetime import datetime

date_format="%d-%m-%Y"
CATEGORIES={"I":"Income","E":"Expense"}

def get_date(prompt,allow_default=False):
    # prompt - the question that we will ask the user before he give his date.
    # Making a function to get date give us the flexibility to use where ever we want dates.
    # We might require date multiple times.
    # Default value=False allows user to just press enter for todays date.
    date_str=input(prompt)
    #if user not entering anything then
    if  allow_default and not date_str:
        return datetime.today().strftime(date_format)

    # If user enters the date
    try: # using try bcz we are converting input to datetime obj and then again to string 
        valid_date=datetime.strptime(date_str,date_format) # converting into date time object
        return valid_date.strftime(date_format) # then converting back to string 
    except ValueError: # if try does not work.
        print('Invalid date format. Please enter the date in dd-mm-yyyy format  ')
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount=float(input("Enter the amount:")) # we try to convert to float otherwise it goes to except.
        if amount<=0: # we want values to be positive.
            raise ValueError("Amount must be a non-negative non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount() # recalling function again as there was error raised 
        # becasue entered amount is not a number or not a positive number.


def get_category():
    category=input("Enter the category ('I' for Income or 'E'for Expense):").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense. ")
    return get_category()



def get_description():
    description=input("Enter a desription (Optional):")
    return description

