list=[5,2,4,3,1]
n=len(list)

for i in range(n):
    for j in range(0,n-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("list is sorted",list)