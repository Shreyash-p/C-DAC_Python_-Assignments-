
#FUNCTION_ASS

#Q1

def display(n,a):
    print("Welcome ",n," your age is ",a)
    
display("Priya",25)


#Q2----------------------------------------------------------------------------

def func1(*a):
    print("Value is : ",a)

func1(1,2,5,6,85,0,5,5)


#Q3----------------------------------------------------------------------------

def calculation(a,b):
    return a+b,a-b

x,y=calculation(8,3)
print("Addition : ",x,"Substration : ",y)


#Q4----------------------------------------------------------------------------

def showEmployee(n,s=9000):
    print("Employee name : ",n,", Salary : ",s)

showEmployee("Priya",15000)
showEmployee("Rani")


#Q5----------------------------------------------------------------------------

def square(sides):
    print("Side = ",sides)
    
fun=square(6)


#Q6----------------------------------------------------------------------------

def fun():
    l=[x for x in range(4,31) if x%2==0]
    return l
   
x=fun()        
print("List - ",x)


#Q7----------------------------------------------------------------------------

def lst(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2

list1=[1,1,2,3,5,2,1,5,3,6,4,8,3,3,9,4,2,2]
print(list1)


print("New list is - ",lst(list1))


#Q8----------------------------------------------------------------------------

def square():
    l=[x*x for x in range(1,31)]
    return l
   
x=square()        
print("List - ",x)


#Q9----------------------------------------------------------------------------

l1=['r','g','b']
l2=['red','green','blue']

l3=dict(zip(l1,l2))
print(l3)


#Q10---------------------------------------------------------------------------

l1=[1,2,3,4,5,6,7,8,9,10]
l2=list(map(lambda a:a*a,l1))
print(l2)


#Q11---------------------------------------------------------------------------

y=lambda a:a+15
print(y(15))

x=lambda a,b:a*b
print(x(4,3))


#Q12---------------------------------------------------------------------------

l1=[1,2,3,4,5,6,7,8,9,10]
lst=[1,2,3,4,5,6,7,8,9,10]

cube=lambda a:a**3
sqr=lambda a:a*a
l2=list(map(cube,l1))
l3=list(map(sqr,lst))

print(l2+l3)


