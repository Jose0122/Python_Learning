# a = [0,1,2,1,3,5,1]
# b = []
# c = []
# for i in a:
#     if i != 1:
#         b.append(i)
#     else:
#         c.append(i)

# for i in range(len(a)-1):
#     if a[i] == 1:
#         temp = a[i]
#         a[i] = a[i+1]
#         a[i+1] = temp
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)-1):
#         if a[i] != 1 or a[j]:
#             temp = a[i]
#             a[j] = temp

# print(a)

# thislist = ["apple", "banana", "cherry"]

# thislist[1:3] = ["watermelon"]

# print(thislist)

a = [1,3,4,1,2,3,4]

new = [i for i in range(len(a)) if i == 1]

print(new)