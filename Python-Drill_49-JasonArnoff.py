arr1 = [67,45,2,13,1,998]
arr2 = [89,23,33,45,10,12,45,45,45]


def mySortFunction(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print(arr)
