A = [(1,2), (3,4)]
B = [(2,3), (4,6)]
aa = A[0][0]; ab = A[0][1]; ac = A[1][0]; ad = A[1][1]
ba = B[0][0]; bb = B[0][1]; bc = B[1][0]; bd = B[1][1]

print("Matrix A")

if aa*ad-ab*ac == 0 :
 print("There's no inverse.")
else :
 c = aa*ad-ab*ac
 af1 = (1/c)*ad; af2 = (1/c)*(-ab); af3 = (1/c)*(-ac); af4 = (1/c)*(aa)
 af = [(af1, af2), (af3, af4)]
 print("inverse matrix of A = ", end =''); print(af)

print("Matrix B")

if ba*bd-bb*bc == 0 :
 print("There's no inverse.")
else :
 cb = ba*bd-bb*bc
 bf1 = (1/cb)*bd; bf2 = (1/cb)*(-bb); bf3 = (1/cb)*(-bc); bf4 = (1/cb)*(ba)
 bf = [(bf1, bf2), (bf3, bf4)]
 print("inverse matrix of B = ", end =''); print(bf)


