a = 257
b = 257
print (a is b)

s = "Python"
print(s[0:10])

a= (5)
b=(6,)
print(type(a))
print(type(b))


print(bool("False"))
print(bool(""))
print(bool(0))
print(bool(-1))

a = [1,2,3]
a = a + [4]
b = a.copy()
print(a)
print(b)

age = int(input("Enter age : "))
if age > 18:
    print("adult")

a = "10"
b = 4
print(a*b)

a = [1,2,3]
b = a.copy()
b.append(4)
print(a)
print(b)

s = int(input("Number : "))
print(float(s))
print(type(s))
print(str(s))
print(s*s)


def identify(data):
    return type(data)

d = identify(data={"Name":"Jose"})
print(d)


def find(data):
    if isinstance(data, int):
        print("True")
    else:
        print("False")

a = "123"
print(find(a))


a = "Hello"
print(id(a))
a = a + "Jose"
print(id(a))


l = [1,2,3]
print(id(l))
print(l)
l.append(4)
print(id(l))
print(l)


x = 10
print(isinstance(x,(int,float)))


class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b,B))
print(isinstance(b,A))
print(type(b) == A)

a = 10
print(type(str(a)))