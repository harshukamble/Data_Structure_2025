def hashmap(arr1,arr2):
    if len(arr1)!=len(arr2):
        return False
    else:
        hash={}
        for i in arr1:
            if i in hash:
                hash[i]+=1
            if i not in hash:
                hash[i]=1
        for i in arr2:
            if i not in hash or hash[i]==0:
                return False
            else:
                hash[i]-=1
        return True
arr1=[1, 7, 1]
arr2=[7, 7, 1]
result=hashmap(arr1,arr2)
if result==True:
    print("same arry!!!")
else:
    print("array not same!!!")