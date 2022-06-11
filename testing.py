def ls(val, l=[]):
	print(f"Val is: {val} and l is: {l}")
	l.append(val)
	print(f"Val is: {val} and l is: {l}\n")
	return l

l1 = ls('NodeJS')
print("%s" % l1)

l2 = ls('Java', [])
print("%s" % l2)

l3 = ls('ReactJS')
print("%s" % l3)