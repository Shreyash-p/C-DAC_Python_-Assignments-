
#LIST_ASS

#Q1
lst=[10,20,50,75,95,80,36]
sum=avg=0
for i in lst:
    sum+=i
    
avg=sum/len(lst)

print("Average : ",'%.2f'%avg)


#Q2----------------------------------------------------------------------------

lst=[10,20,50,75,95,80,36,-85,-62,-42,49]
s1=s2=s3=0

for i in lst:
    if(i<0):
        s1+=i
    elif(i%2==0 and i>0):
        s2+=i
    elif(i%2==1 and i>0):
        s3+=i
    
print("Negative : ",s1,"Even : ",s2,"Odd : ",s3)


#Q3----------------------------------------------------------------------------

lst=[10,20,50,75,196,80,36,815,62,42,49]
lst1=[]
lst2=[]

for i in range(0,len(lst)):
    if lst[i]%2==0:
        lst1.append(lst[i])
    elif lst[i]%2==1:
        lst2.append(lst[i])
        
print(lst1)
print(lst2)
print(max(lst1))
print(max(lst2))


#Q4----------------------------------------------------------------------------

lst=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for i in range(0,len(lst)):
    print(lst[i][0:3],end=' ')


#Q5----------------------------------------------------------------------------

l=[10,20,50,75,196,20,36,815,50,62,42,49,20]
l2=[]

for i in l:
    if i not in l2:
        l2.append(i)

for i in range(0,len(l2)):
    print(l2[i],l.count(l2[i]))


#Q6----------------------------------------------------------------------------

l=[10,20,50,75,196,20,36,85,62,42,49,20]

print("Largest number is : ",max(l))


#Q7----------------------------------------------------------------------------

l=[10,20,50,75,196,20,36,85,-62,-42,49,20]

print("Largest number is : ",max(l))

l.sort()                        #OR we can make a varible like max=l[0]
print(l)                        #then compare it with the list and make a second variable
print(l[-2])                    #compare like if(max<l[i])
                                #                   second=max
                                #                   l[i]=max
#Q8----------------------------------------------------------------------------

lst=[10,20,50,75,196,80,36,815,62,42,49]
lst1=[]
lst2=[]

for i in range(0,len(lst)):
    if lst[i]%2==0:
        lst1.append(lst[i])
    elif lst[i]%2==1:
        lst2.append(lst[i])

print(lst1)
print(lst2)


#Q9----------------------------------------------------------------------------

l1=[10,20,50,75,49]
l2=[196,80,36,815,62,42]
lst=[]
lst= l1+l2
print(lst)
lst.sort() 
print(lst)


#Q10---------------------------------------------------------------------------

lst=[10,20,50,75,196,80,36,815,62,42,49]
print(lst)

first,last=lst[0],lst[-1]
lst[-1],lst[0]=first,last
print(lst)


#Q11---------------------------------------------------------------------------

l=[10,20,50,75,196,20,36,815,50,62,42,49,815,20]
lst=[]

for i in l:
    if i not in lst:
        lst.append(i)
print(lst)


#Q12---------------------------------------------------------------------------

lst=[10,20,50,75,196,80,36,815,62,42,49]
no=int(input("Enter number : "))

x=lst.index(no)
print("Index of the number : ",x)


#Q13---------------------------------------------------------------------------

l=[]
ip=1
while ip!=0:

    print("1. Add data in list (last)")
    print("2. Add data by position")
    print("3. Delete data by value")
    print("4. Delete data by position")
    print("5. Sort data in ascending order")
    print("6. Sort data in descending order")
    print("7. Reverse data")
    print("8. Display List")
    print("0. Exit")
     
    ip=int(input("Choose the options : "))

    if(ip==1):
        v=input("Enter name - ")
        l.append(v)
    elif(ip==2):
        value=input("Enter name - ")
        index=int(input("Enter index value : "))
        l.insert(index,value)
    elif(ip==3):
        value=input("Enter name to delete - ")
        l.remove(value)
    elif(ip==4):
        index=int(input("Enter index value : "))
        l.pop(index)
    elif(ip==5):
        l.sort()
    elif(ip==6):
        l.sort(reverse=True)
    elif(ip==7):
        l.reverse()
    elif(ip==8):
        print(l)
   
    
#Q14---------------------------------------------------------------------------

l=[]

l=[x*x for x in range(1,21) ]
print(l)


#Q15---------------------------------------------------------------------------

l=[]

l=[x for x in range(1,1001) if x%7==0]
print(l)


#Q16---------------------------------------------------------------------------

l=[]

l=[x for x in range(1,1001) if '5' in str(x)]
print(l)


#Q17---------------------------------------------------------------------------

lst=["this","is","an","example"]


l=[x[0] for x in lst]
print(l)


#Q18---------------------------------------------------------------------------

lst=["this","is","an","example"]


l=[(x,len(x)) for x in lst]
print(l)

