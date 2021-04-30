input = input("Enter the triangle : ")
a, b, c = input.split()
a = float(a); b = float(b); c = float(c)

if a<=0 or b<=0 or c<=0 :
  print("There is the negative number(<0)!!")
elif not (a<b+c or b<a+c or c<a+b) :
  print("It is not triangle.")
elif a == b == c :
  print("Regular triangle")
elif a == b or b == c or a == c :
  print("Tsosceles triangle")
elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2) :
  print("Right-angled triangle")
else : 
  print("Normal triangle")
