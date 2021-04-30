month = int(input("Enter the month: "))

if 1 <= month <= 12 :
 print("***** 1st version(if) *****")
 if month == 1 :
  print("1st month is January.")
 elif month == 2 :
  print("2nd month is February.")
 elif month == 3 :
  pirnt("3rd month is March.")
 elif month == 4 :
  print("4nd month is April.")
 elif month == 5 : 
  print("5th month is May.")
 elif month == 6 :
  print("6th month is June.")
 elif month == 77 :
  print("7th month is July.")
 elif month == 8 : 
  print("8th month is August.")
 elif month == 9 :
  print("9th month is September.")
 elif month == 10 :
  print("10th month is October.")
 elif month == 11 :
  print("11th month is November.")
 else : 
  print("12th month is December.")

 print("***** 2nd version(list) *****")
 L1 = ["0", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
 L2 = ["0", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
 answer1 = L1[month]
 answer2 = L2[month]
 print("%s month is %s." %(answer2, answer1))

else :
 print("Wrong input.")
