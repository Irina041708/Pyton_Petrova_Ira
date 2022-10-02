# n = {'1','22','3'}

# print(type(n))
# print(n)


# n.remove('22')
# print(n)


# n.clear()
# n = {'r','23'}
# print(n)


a = {1,2,3,6}
b = {9,8,2}

# c = a.copy()
# print(c)

# u = a.union(b)
# print(u)

# i = a.intersection(b)
# print(i)

# dl = a.difference(b)
# print(dl)

# dl2 = b.difference(a)
# print(dl2)

q = a \
    .union(b)\
    .difference(a.intersection(b))
print(q)
    