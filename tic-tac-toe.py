def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ', ' '] 
row2 = [' ',' ', ' '] 
row3 = [' ',' ', ' '] 

# Example of putting an X at a index position
row2[1] = 'X'

# Display the rows
display(row1,row2,row3)

def user_choice():
    choice = 'WRONG'
    acceptable_range = range(0,4)
    within_range = False

    # Can use .isdigit() this translates a string number
    while choice.isdigit() == False or within_range == False:
        choice = input ("Please enter a number (0-3): ")
        if choice.isdigit() == False:
            print("Sorry, that is not a digit!")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0 to 3)")
                within_range = False

    return int(choice)

user_choice()

# Ask user for index position, change from str to int
#position_index = int(input("Choose an index position: "))


