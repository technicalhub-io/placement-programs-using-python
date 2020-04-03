def palindrome(val):
    s=str(val)
    j=len(s)-1
    for i in range(len(s)//2):
        if(s[i]==s[j]):
            j-=1
        else:
            return 0
    return 1    
def largest_palindrome(l):
    pal=[]
    for i in range(len(l)):
        if(palindrome(l[i])):
            pal.append(l[i])
    max_pal=max(pal)        
    return max_pal            
l=list(map(int,input().split()))
k=largest_palindrome(l)
print(k,"is the largest palindrome in the given list")
