from sys import argv

script, filename = argv

extra_credit = open(filename)

print(extra_credit.read())

extra_credit.close()
