# not pointer
num1 = 11

num2 = num1

print("Before value is updated:")
print("num1 ={}", num1)
print("num2 ={}", num2)

num1 = 22

print("\nAfter num1 value is updated:")
print("num1 ={}", num1)
print("num2 ={}", num2)

##################################################
# pointer: dict2 points to dict1
dict1 ={
    'value': 11
}

dict2 = dict1

print("Before dict value is updated:")
print("dict1 = {}", dict1)
print("dict2 = {}", dict2)

dict1['value'] = 22
print("\nAfter dict value is updated:")
print("dict1 = {}", dict1)
print("dict2 = {}", dict2)

# dict2 points to dict3
dict3 = {
    'value': 57
}

dict2 = dict3
print("\ndict2 now points to dict3 value is updated:")
print("dict1 = {}", dict1)
print("dict2 = {}", dict2)
print("dict3 = {}", dict1)

dict1 = dict3
print("\ndict1 now points to dict3 value is updated. \n Now they all point to dict3:")
print("old derefrenced values will be garbage collected")
print("dict1 = {}", dict1)
print("dict2 = {}", dict2)
print("dict3 = {}", dict1)


