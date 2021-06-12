first_num = 124
second_num = 2.768
sum = first_num + second_num
print("=======IMPLICIT TYPE CONVERSION========")
print("Type of First Number:",type(first_num))
print("Value of First Number:",first_num)

print("Type of Second Number:",type(second_num))
print("Value of Second Number:",second_num)

print("Type of SUM :",type(sum))
print("Value of SUM:",sum)

print("=========EXPLICIT TYPE CONVERSION========")
first_num = 124
second_num = "256.987"
sum = first_num + float(second_num)

print("Type of First Number:",type(first_num))
print("Value of First Number:",first_num)

print("Type of Second Number:",type(second_num))
print("Value of Second Number:",second_num)

print("Type of SUM :",type(sum))
print("Value of SUM:",sum)



