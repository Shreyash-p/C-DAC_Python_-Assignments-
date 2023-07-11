

#STRING_ASS

#Q1
str="Amit is a good boy"
print(str)
s=str.replace('a','$')
print(s)


#Q2------------------------------------------------

s="Amit is a good boy"
str=""
n=6
print(str)

for ch in range(0,len(s)):
    if(ch!=n):
        str=str+s[ch]
print(str,end='')
    

#Q3------------------------------------------------

str="Amit is a good boy"
v="aeiouAEIOU"
cnt=0

for i in str:
    if i in v:
        cnt=cnt+1
else:
    print(cnt)
    
    
#Q4------------------------------------------------

str="Amit is a good boy"
print(str)
s=str.replace(' ','_')
print(s)


#Q5------------------------------------------------

str="Amit is a good boy"
cnt=0

for ch in str:
    cnt+=1
print(cnt)


#Q6------------------------------------------------

str="Amit is a good boy"
str=""
print(str)

for ch in range(0,len(s)):
    if(ch%2!=0):
        str=str+s[ch]
print(str,end='')


#Q7------------------------------------------------

str="Amit is a good boy"
cnt1=cnt2=0

for i in str:
    if(i.isupper()):
        cnt1+=1
    elif(i.islower()):
        cnt2+=1
print("Upper case : ",cnt1)
print("Lower case : ",cnt2)


#Q8------------------------------------------------

str="nitin"
temp=str
s=""
print(str)

for i in str:
    s=i+s

if(temp==s):
    print("String is palindrome")
else:
    print("String is not a palindrome")
    
    
#Q9------------------------------------------------
    
str="Amit is a good boy"
s=""

s=str[0:2]+str[-2]+str[-1]          
print(s)   
  

#Q10------------------------------------------------  
    
str=input("Enter the string : ")
ch=input("Enter the character : ") 

if(str.startswith(ch)):
    print("Present")
else:
    print("Not Present")
    

#Q11------------------------------------------------    
    
str="Amit is a good boy"
v="aeiouAEIOU"
cnt=0

for i in str:
    if i not in v:
        cnt=cnt+1
else:
    print(cnt)


#Q12------------------------------------------------
   
name=input("Enter the name : ")
age=int(input("Enter the age : "))
salary=int(input("Enter the salary : ")) 

print("Hello {}, you are {} years old and getting {} salary".format(name,age,salary))
print("Hello {1}, you are {0} years old and getting {2} salary".format(name,age,salary))
print("Hello {s}, you are {a} years old and getting {n} salary".format(n=name,a=age,s=salary))
print(F"Hello {name}, you are {age-10} years old and getting {salary} salary")


#Q13------------------------------------------------

str="AlwaysThinkPosiTive"

print(str[5])
print(str[10])
print(str[5:8])
print(str[8:5:-1])
print(str[:])


#Q14------------------------------------------------

str="The Quick brown fox jumps over the lazy dOG"

print(str)
print(str.lower())
print(str.upper())
print(str.title())
print(str.swapcase())


#Q15------------------------------------------------

str=input("Enter the string : ")
cnt=0

for i in str:
    if(i.isalpha()):
        cnt+=1
print(cnt)


#Q16------------------------------------------------

str="The 1Quick brown fox jumps over the 2lazy 4dOG"
x=sum=0

for i in str:
    if(i.isnumeric()):
        x=int(i)
        sum+=x
print(sum)


#Q17------------------------------------------------

str="I am smart and clever"
lst=str.split()

for i in lst:
    if 'a' in i:
        print(i)
        
        
#Q18------------------------------------------------

str="clever"

for i in range(0,len(str)+1):
    print(str[:i])                  #[:i]->means stop at i=0 which is (c)
                                    #[:i]->means stop at i=1 which is (cl)
                                    #[:i]->means stop at i=2 which is (cle)


#Q19------------------------------------------------

str="The Quick brown fox jumps over the lazy dOG"
lst=str.split()

print(str)
print(lst)

for i  in range(0,len(lst)):
    print(lst[i][0:2],end=' ')

























   
   
    
