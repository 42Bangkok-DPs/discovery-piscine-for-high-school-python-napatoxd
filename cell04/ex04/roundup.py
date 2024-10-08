def round_up(number):
    if number == int(number):
        return int(number)
    else:
        return int(number) + 1

user_input = input("Please enter a number: ")
number = float(user_input)
        
rounded_number = round_up(number)
        
print("The number rounded up is: ",rounded_number)
