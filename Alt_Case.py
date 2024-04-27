mystr=input("Enter the string:")
l=len(mystr)
strr=""
for i in range(0,l):
    if(i%2==0):
        strr+=mystr[i].lower()
    else:
        strr+=mystr[i].upper()

print(strr)