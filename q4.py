Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter third number : "))
if first_number >= second_number:
    if first_number >= third_number:
        print("The greatest number is %s\n" % first_number)
    else:
        print("The greatest number is %s\n" % third_number)
else:
    if second_number >= third_number:
        print("The greatest number is %s\n" % second_number)
    else:
        print("The greatest number is %s\n" % third_number)