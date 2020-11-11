from unionfind import unionFind

temp = unionFind(10)
temp.union_parent(temp.parent,1,2)
temp.union_parent(temp.parent,3,4)

print(temp.parent)
print(temp.find_parent(temp.parent,1,3))
print(temp.find_parent(temp.parent,3,4))
