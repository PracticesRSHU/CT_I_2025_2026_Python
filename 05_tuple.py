tuple1=()
tuple2=tuple()
tuple3=(3,)
tuple4=4,
print(f"tuple1={tuple1} type: {type(tuple1)}")
print(f"tuple2={tuple2} type: {type(tuple2)}")
print(f"tuple3={tuple3} type: {type(tuple3)}")
print(f"tuple4={tuple4} type: {type(tuple4)}")

x,y,z=23,"Python",67
print(x)
print(y)
print(z)

books=('Shevchenko', 'Franko')
print(books)
# books[0]='Stusa'  #error runtime
library=list(enumerate(books,start=1))
print(library)
# methods count; index
# function: len, min, max
tuple5=(56,34,53,23,56)
print("len=",len(tuple5))
print("min=",min(tuple5))
print("max=",max(tuple5))
print("count=",tuple5.count(56))
print("index(34) =",tuple5.index(34))
print(" find element by index 3 =",tuple5[3])

list1=[]
for i, number in enumerate(tuple5):
    print(i,"-й елемнт=> ",number,sep="")
    list1.append(number**2)

tuple6=tuple(list1)
print(tuple6)