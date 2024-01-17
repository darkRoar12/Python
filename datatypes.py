list2=[1,2,3,4,5]
mixed_data=["Niggerrr",9.11,69,True,None,"hello",list2,False]

print(f"The first three elements of the list are : {mixed_data[0:3]}")
print(f"Elements starting from 2nd to 5th position are: {mixed_data[1:5]}")
print(f"The last two elements are: {mixed_data[-2:]}")

# print("voila")
print("The elements of the list along its type are")
for element in mixed_data:
    print(element, type(element))