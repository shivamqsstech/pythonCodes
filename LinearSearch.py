num = int(input("Enter the element u are looking"))
print("Enter the list element seperated by space")
arr_1 = [int(x) for x in input().split()]
ele= -1
for i in range(len(arr_1)):
    if arr_1[i] == num:
        ele = i
        break
if ele>=0:
    print(ele)
else:
    print(ele)
