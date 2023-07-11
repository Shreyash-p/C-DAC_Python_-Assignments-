#DICTIONARY_ASS

#Q1

d={}

for i in range(0,5):
    k=int(input("Enter key : "))
    v=int(input("Enter value : "))
    d[k]=v

print(d)


#Q2----------------------------------------------------------------------------

d1={1: 11, 2: 22, 3: 33, 4: 44, 5: 55}
d2={'a':1,'b':2,'c':3}

d1.update(d2)
print(d1)
d3={**d1,**d2} #<------------------------------Other way
print(d3)


#Q3----------------------------------------------------------------------------

n=int(input("Enter range : "))
d={x:x**3 for x in range(1,n)}

print(d)


#Q4----------------------------------------------------------------------------

d={1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
sum=1

for i in d.values():
    sum*=i
          
print(sum)


#Q5----------------------------------------------------------------------------

d={1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
print(d)

k=int(input("Enter key : "))
del d[k]
print(d)


#Q6----------------------------------------------------------------------------

d={'name':'priya','age':45,'state':'pune'}
print(d)

d.pop('state')
d['location']='pune'
print(d)


#Q7----------------------------------------------------------------------------

l1=[10,20,50,75,49]
l2=[196,80,36,815,62,42]

d=dict(zip(l1,l2,strict=False))
print(d)


#Q8----------------------------------------------------------------------------

ip=1
while ip!=0:

    print("1. Add data in dictionary ")
    print("2. Update data ")
    print("3. Delete data ")
    print("4. Display dict ")
    print("5. Find data ")
    print("0. Exit")
    
    ip=int(input("Choose the options : "))
    
    if(ip==1):
        d={}
        num=int(input("Enter how many subjects you have - "))
        for i in range(0,num):
            k=input("Enter  first ltter - ")
            v=input("Enter Subject - ")
            d[k]=[v]    
    elif(ip==2):
        k=input("Enter  first ltter - ")
        v=input("Enter Subject - ")
        d.update({k:v})
    elif(ip==3):
        k=input("Enter  first ltter to delete - ")
        del d[k]
    elif(ip==4):
        for x,y in d.items():
            print(x,y)
    elif(ip==5):
        k=input("Enter  first ltter to find - ")
        if(d.get(k)!=None):
            print("Present")
        else:
            print("Not present")
            
            
#Q9----------------------------------------------------------------------------

d={'Priya':'1256897423','Madhuri':'9675842631','Rama':'8545652513'}
print(d)

d.update({'Madhuri':'7548968525'})
print(d)

d.update({'Ankita':'9785246315'})
print(d)

if(d.get('Rama')!=None):
    print(d.get('Rama'))
else:
    print("None")
    
for k in d.keys():
    print(k)

for v in d.values():
    print(v)
    
    
#Q10---------------------------------------------------------------------------

d={'Zack':'orange','Priya':'yellow','Rama':'pink','Rohit':'black','Lisa':'red'}
print(d)

cnt=0
for k in d.keys():
    cnt+=1
print("Number of students - ",cnt)

d.update({'Lisa':'Purple'})
print(d)

del d['Priya']
print(d)

d2=list(d.items())
print(d2)
d2.sort()
print(d2)
d=dict(d2)
print(d)



