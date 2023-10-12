def comparearray(arr1,arr2):
    arr1.sort()
    arr2.sort()
    if len(arr1)!=len(arr2):
        return False
    else:
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return False
        return True
arr1=[4,2,5,4,2,7,8]
arr2=[4,2,5,4,2,7,8]
result=comparearray(arr1,arr2)
if result==True:
    print("same arry!!!")
else:
    print("not same arry!!!")