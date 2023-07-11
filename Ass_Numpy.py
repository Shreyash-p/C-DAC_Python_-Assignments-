
#Q1
import numpy as np
l=[1,2,3,4,5,6,7,8]
a=np.array(l)
print(a)

print("dim : ",a.ndim)
print("shape : ",a.shape)
print("type : ",a.dtype)
print("size : ",a.size)


#Q2--------------------------------------------------


b=np.empty((5,3),dtype=int)
print(b)
c=np.full((3,5),1,dtype=int)
print(c)
b=np.zeros((5,3),dtype=int)
print(b)
b=np.ones((5,3),dtype=int)
print(b)


#Q3--------------------------------------


b=np.arange(14,40)
print(b)


#Q4--------------------------------


b=np.random.randint(1,40,(8,5))
print(b)


#Q5-------------------------------------


c=np.resize(b,(4,10))
print(c)


#Q6----------------------------------------------------


b=np.random.randint(1,40,(5,5))
print(b)
print()
print(b[0:3,0:4])
print(b[0:3,4:])
print(b[2:4])
print(b[:,2:])


#Q7---------------------------------------


b=np.random.randint(1,40,(5,5))
print(b)
b[b%2==1]
print(b)


#Q8---------------------------------------


b=np.random.randint(1,40,(5,5))
print(b)
b[b%2==1]=-1
print(b)


#Q9---------------------------------------


a=np.arange(1,9)
b=np.arange(11,19)
print(a)
print(b)
np.append(a,b)


#Q10--------------------------------------


d=np.arange(1,17)
print(d)
d.reshape(2,8)
print(d)


#Q11--------------------------------------


c=np.random.randint(13,40,(12))
print(c)
np.sort(c)
print(c[::-1])


#Q12---------------------------------------


b=np.random.randint(1,15,(5,3))
print(b)
print(b+4)
print(b*2)
print(b-3)
print(b//2)


#Q13----------------------------


b=np.random.randint(1,9,(3,3))
c=np.random.randint(1,9,(3,3))

print(b+c)
print(b-c)
print(b*c)
print(b.dot(c))
print(b.sum(axis=0))
print(b.min(axis=0))
print(c.max(axis=0))
