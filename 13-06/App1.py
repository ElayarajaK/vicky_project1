value1 = int(input("Enter the value1 "))

value2 =int(input("Enter the value2 "))

value3 = int(input("Enter the value3 "))

value4 =int(input("Enter the value4 "))
''''''
Max = None;
'''
if(value1 > value2 and value1 > value3 and value1 > value4):
    Max=value1;
elif(value2 > value3 and value2 > value4):
    Max = value2;
elif(value3 > value4):
    Max=value3
else:
    Max=value4;
'''
Max = value1 if value1 > value2 and value1 > value3 and value1 > value4 else value2 if value2 > value3 and value2 > value4 else value3 if value3 > value4 else value4;
print(Max)

