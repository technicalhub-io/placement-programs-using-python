# To perform the reverse of the string

#take input from user

string=input()

#initialize the empty string

a=""

#access the string elemnts in reverse order

for i in range(len(string)-1,-1,-1):

#perform the concatenation

    a=a+string[i]
    
#print output

print(a)
