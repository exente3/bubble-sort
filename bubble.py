array1 = [5, 22, 16, 8, 101, 77, 3, 1 ]

def bSort(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bSort(array1))