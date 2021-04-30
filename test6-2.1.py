ent = input("Enter sentence:\n")
if ent == '' :
 print("\nNo sentence")
else :
 ent = ent.lower()
 entset = set(ent.split())
 entlist = sorted(list(entset))
 print("Non duplicate words (list): ", end = '')
 print(entlist)

 new = input("Enter one character for string : ")
 final = new.join(entlist)
 print("Non duplicate words(string) : ", end = ''); print(final)
