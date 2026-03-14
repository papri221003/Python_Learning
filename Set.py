New_Set={1,2,3,"papri",4,3}

print(New_Set)

#creating Null Set
null_Set=set()
print(null_Set)

#Set Methods

New_Set.add(5)
New_Set.add(6)
New_Set.add(7)
New_Set.add(8)

New_Set.remove("papri")
print(New_Set)

#Union
New_set2={7,8,9,10,11,12,13,14}
print(New_Set.union(New_set2))

#Intersection
print(New_Set.intersection(New_set2))