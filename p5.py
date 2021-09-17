# wapp to read 4 numbers  and find max of the 4
n1 = float(input("enter first number"))
n2 = float(input("enter second number"))
n3 = float(input("enter third number"))
n4 = float(input("enter fourth number"))

# compare n1 and n2
if n1  > n2:
	r1 = n1
else:
	r1 = n2

#compare n3 and n4
if n3 > n4:
	r2 = n3
else:
	r2 = n4

# finally compare r1 and r2
if r1 >  r2 :
	res = r1
else:
	res = r2
print(" max of 4 numbers is = ", res)

print("max of 4 numbers is =", max(n1,n2,n3,n4))