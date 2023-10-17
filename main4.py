a = int(input("a: "))
b = int(input("b: "))
if a != b and a < b:
   print(str(a) + " " + str(b))
elif a != b and a > b:
   print(str(b) + " " + str(a))
else:
   print("a = b")