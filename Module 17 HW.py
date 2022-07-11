a = str(input('введите числа через пробел:'))
b = int(input('введите число:'))
array = a.split()

for i, item in enumerate(array):
    array[i] = int(item)
array.append(b)
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(binary_search(array, b, 0, len(array)-1))