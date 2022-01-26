Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=56
b=10
print("a.\ta & b = %d" % (a & b))
print("b.\ta | b = %d" % (a | b))
print("c.\ta ^ b = %d" % (a ^ b))
print("d.\tLeft shift both a and b with 2 bits : a = %d, b = %d" % (a << 2,b << 2))
print("e.\tRight shift a with 2 bits and b with 4 bits : a = %d, b = %d\n" % (a >> 2,b >> 4))