import timeit

s = """\
elements = []
for i in range(0,100):
    elements.append(i)"""

print(timeit.timeit(s))



s2 = 'elements2 = [*range(0,100)]'
print(timeit.timeit(s2))

s3 = 'elements3 = [i for i in range(0,100)]'
print(timeit.timeit(s3))

s4 = 'elements4 = []; elements4.extend(range(0,100))'
print(timeit.timeit(s4))
