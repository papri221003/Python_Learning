#Tupple
"""
tup=(97,98,95,96,93,91,92,94,97,97)
# tuples are immutable...means creating adding or removing any elemt from a tuple is not possible s it is immutable..once it is created it cant be deleted or rectified
#tup[0]=14 .........not allowed
print(tup.count(97))
print(tup.index(98))
"""

#Set 
"""
nums={1,2,4,5,8,1,2,6,9,7,4,2,(40,85,'papri')}
print(nums)
nums.add(10)
print(nums)
nums1={10,15,18,17,19}
print(nums.union(nums1))
print(nums.intersection(nums1))
"""

#Dictionary
my_Dict={}

my_Dict.update({"Name":"Papri"})
my_Dict.update({"cgpa":8.72})
my_Dict.update({"Subjects":('Control','Analog System','Device','Signal system')})
my_Dict.update({"Marks":(85,91,96,87)})

print(my_Dict)
print(my_Dict["Marks"])
print(my_Dict.keys())
print(my_Dict.values())

