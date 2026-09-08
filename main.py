import numpy as np

#1D Array
a=np.array([1,2,3,4,5])
print (a)

#2D Array
b=np.array([[1,2],[2,3],[3,4]])
print (b)

c=np.array([1,2,3,4,5], dtype=float)
print (c)

d=np.array([[1,2,3],[2,3,4],[3,4,5]])
print (d.shape)

e = np.array([[[1,2,3],[4,5,6]],
               [[7,8,9],[10,11,12]],
               [[13,14,15], [16,17,18]],
               [[17,18,19],[20,21,22]]])
print(e.shape)

print(e[0]) #[[1,2,3],[4,5,6]]
print(e[1]) #[7,8,9],[10,11,12]
print(e[0][0]) #[1,2,3]
print(e[0][1]) #[4,5,6]
print(e[0][0][0]) #1
print(e[0][0][1]) #2
print(e[0][0][2]) #3

a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print (b) #[[1 2] [3 4] [5 6]]
c = a.reshape(6) #[1 2 3 4 5 6]
print(c)

x = np.zeros([10,5], dtype = int) 
print (x)

x = np.ones([5,5], dtype = int) 
print (x)

x = np.arange(10,20,2) 
print (x) #[10 12 14 16 18]

x = np.linspace(10,20,5) 
print (x) #[10.  12.5 15.  17.5 20. ]

mylist = np.array([10,20,30,40,50,60,70,80,90,100])
print(mylist) #[10,20,30,40,50,60,70,80,90,100]
print(mylist[1]) #20
print(mylist[2:5]) #[30 40 50]
print(mylist[2:]) #[ 30  40  50  60  70  80  90 100]
print(mylist[:5]) #[10 20 30 40 50]
print(mylist[len(mylist)-1]) #100
print(mylist[-1]) #100
print(mylist[-(len(mylist))]) #10

a = np.array([10,20,30,40,50])
b = np.array([2, 3, 4, 5, 6])
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a * 2
print(c)
c = a * 2 + 5
print(c)
c = b ** 2
print(c)

print(a.sum())
print(a.min())
print(a.max())
print(a.mean())

