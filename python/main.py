first_number = int(input("Enter First Number: "))
second_number =int(input("Enter second Number: "))
third_number = int(input("Enter third Number: "))

if (first_number)>(second_number) and (first_number)>(third_number):
    print("%d first number is the greatest") % first_number
elif int(second_number)>int(first_number) and (second_number)>(third_number):
    print("%d second no is greatest")% second_number
else:
    print ("%d third number is the greatest") % third_number
