from collections import Counter


#Counter("superfluous")
counter = Counter("superfluous")
print(counter)

print(counter["u"])


print(list(counter.elements()))


print(counter.most_common(2))

name=Counter("My name is name")
name1=Counter("name is two of one")


print(name.subtract(name1))

print(name)



