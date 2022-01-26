Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
while True:
    sides = sorted(input("Enter the dimensions to check whether triangle possible or not : ").split())  #Sorting the inputted values in a list
    if len(sides) == 3:                                                                                 #Making sure only 3 values are entered
        break
    else:
        print("\nA triangle has only 3 sides!\nPlease enter only 3 values")
if int(sides[2]) > (int(sides[0]) + int(sides[1])):
    print("No\n")
else:
    print("Yes\n")