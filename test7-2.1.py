fs = input("Enter the first string:")
ss = input("Enter the second string:")
fsi = list(fs)
ssi = list(ss)
fsis = sorted(fsi)
ssis = sorted(ssi)


if fsis == ssis :
 print("%s, %s is anagram." %(fs, ss))
else :
 print("%s, %s is not anagram." %(fs, ss))
