L = [12, 29, 30, 0, 99]
i = input("Enter the data for L:")
if i.isdigit():
 i=float(i)
 if  i < 0 or i % 1 != 0:
  print("input can be only bigger integer  than 0.")
  print(L)
 elif i == 12 or i== 29 or i==30 or i ==0 or i ==99:
  print("Input is already in L.")
  print(L)
 else :
  i=int(i)  
  L[5:5] = [i]
  print(L)
else :
 print("input can be only bigger integer  than 0.")
