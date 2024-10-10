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

# Ask user for index position, change from str to int
position_index = int(input("Choose an index position: "))
