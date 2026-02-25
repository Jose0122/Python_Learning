# name = {
#     "Ind" : 123,
#     "aus" : 202,
#     "Ind" : {"Team" : "chennai"}
# }

# print(name["Ind"])

# l = [1,2,3,4]

# for i,u in enumerate(l):
#     print(i)

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict["colors"][2])

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child1"]["name"])