#OOP_1


#Q1

class Power:
    def __init__(self,x,n):
        self.x=x
        self.n=n
        
    def __del__(self):
        print("Destructor called ")
        
    def powerFun(self):
        self.x=self.x**self.n
        return self.x
    
    def __str__(self):
        return f"{self.x} , {self.n}"
    
cube=Power(2, 3)
print(cube)
print(cube.powerFun())
del cube


#Q2----------------------------------------------------------------------------

class StrReverse:
    def __init__(self,s):
        self.s=s
        
    def ReverseStr(self):
        self.s=self.s.split(" ")
        self.s=self.s[::-1]
        self.s=" ".join(self.s)
        return self.s
    
    def __str__(self):
        return f"{self.s}"

s1=StrReverse("I love my country")
print(s1)

print(s1.ReverseStr())


#Q3----------------------------------------------------------------------------

class Str:
    def __init__(self,s):
        self.s=s
        
    def get_String(self,s):
        self.s=s
        return s
        
    def print_String(self):
        self.s=self.s.upper()
        print(self.s)
        
    def __str__(self):
        return f"{self.s}"

s=Str("hello world!!!!!!!!!!!")
s.print_String()
print(s.get_String(input("Enter the string : ")))


#Q4----------------------------------------------------------------------------

class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        
    def area(self):
        return self.l*self.w
    
    def __str__(self):
        return f"Length - {self.l}, Width - {self.w}"

r=Rectangle(12,30)
print(r)
print(r.area())


#Q5----------------------------------------------------------------------------

class Temperature:
    def __init__(self,f,c):
        self.f=f
        self.c=c
        
    def FerToCel(self,fe):
        self.c=(fe-32)*(5/9)
        return self.c
        
    def CelToFer(self,ce):
        self.f=(ce*1.8+32)
        return self.f
        
    def __str__(self):
        return f"Fareheit - {self.f}, Celcius - {self.c}"
        
t=Temperature(60,40)
print(t)
print("Temp in cel - ",t.FerToCel(80))
print("Temp in fer - ",t.CelToFer(40))


#Q6----------------------------------------------------------------------------

class Student:
    a=0
    m=0
    def __init__(self,n,r):
        self.n=n
        self.r=r

    def setAge(self,a):
        self.a=a
    def setMarks(self,m):
        self.m=m
    
    def display(self):
        print("Name -\t",self.n)
        print("Roll no -\t",self.r)
        print("Age -\t",self.a)
        print("Marks -\t",self.m)

s1=Student("Sheetal",101)
s2=Student("Priya", 102)

s2.setAge(22)
s2.setMarks(438)

s1.display()
s2.display()


#Q7----------------------------------------------------------------------------

class Time:
    def __init__(self,h,m):
        self.h=h
        self.m=m
    
    def addTime(self,h1,m1,h2,m2):
        h=0
        m=0
        if(m1+m2<60):
            h=h1+h2
            m=m1+m2
            return h,m
        elif(m1+m2>=60):
            h=(h1+h2+1)
            m=(m1+m2-60)
            return h,m
        
    def addMin(self,h,m):
        cnt=0
        for i in range(0,h):
            cnt+=60
        return cnt+m
    
    def display(self):
        print("Time - ",self.h,"h :",self.m,"m")

t1=Time(1,30)
t2=Time(3,40)
t1.display()
t2.display()

h,m=t1.addTime(1,30,3,40)
print("Added time - ",h,":",m)
print("Total mins - ",t1.addMin(3,40))


#Q8----------------------------------------------------------------------------

class Dealer:
    def __init__(self,id,n,m,ad):
        self.id=id
        self.n=n
        self.m=m
        self.ad=ad
        
    def mobPalin(self):
        newm=self.m
        mob=0
        while(self.m>0):
            rem=self.m%10
            mob=(mob*10)+rem
            self.m=self.m//10
        if(newm==mob):
            print("Number is palindrome")
        else:
            print("Number is not palindrome")
        
    def cityPune(self):
        if(self.ad=='Pune'):
            print("YES")
        else:
            print("NO")
        
    def __str__(self):
        return f"Cus ID- {self.id}, Name- {self.n}, Mob- {self.m}, Add- {self.ad}"

d1=Dealer(101, "Priya", 1234554321, "Mumbai")
d2=Dealer(102, "Arjun", 1234557321, "Pune")
d3=Dealer(103, "Geeta", 9534554321, "Goa")
d4=Dealer(104, "Seema", 7834554321, "Nagpur")
d5=Dealer(105, "Rohit", 12344321, "Pune")   
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
        
d1.cityPune()
d2.cityPune()
d1.mobPalin()
d3.mobPalin()


#Q9----------------------------------------------------------------------------

class Student:
    def __init__(self,n,r,c,d):
        self.n=n
        self.r=r
        self.c=c
        self.d=d
        
    def __str__(self):
        return f"Roll- {self.r}, Name- {self.n}, Course- {self.c}, Dict- {self.d}"
    

ip=1
while(ip!=0):
    print("Option 1 - Add student info " )
    print("Option 2 - Print student data " )
    print("Option 3 - Check failed subjects " )
    print("Option 0 - Exit")
    
    ip=int(input("Choose option - "))
    
    if(ip==1):
        size=int(input("Enter how many students data you want - "))
        lst=[size]
        
        for i in range(0,size):
            n=input("Enter name - ")
            r=int(input("Enter roll no - "))
            c=input("Enter course - ")
            d={}
            num=int(input("Enter how many subjects you have - "))
            for i in range(0,num):
                k=input("Enter Subject - ")
                v=input("Enter marks - ")
                d[k]=[v]
            lst.append(Student(n, r, c, d))
        
    elif(ip==2):
        for i in range(0,len(lst)):
            print()
            print(lst[i])
            
    elif(ip==3):
        sum=0
        for v in d.values:
            sum+=v
        if((sum/3)<45):
            print("Fail")
        else:
            print("Pass")

        
#NOT COMPLETE ^
          

























