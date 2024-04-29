def find_smallest(arr):
    small = arr[0] #берем 1 элемент массива
    small_index = 0#его индекс
    for i in range(1, len(arr)):#создаем цикл и бежим по массиву
        if arr[i] < small:#если элемент массива i < 1 элемента
            small = arr[i]#то он соответственно становится первым в массиве 
            small_index = i#задаем ему соответствующий индекс
    return small_index#возвращаем исправленный массив


def sortSelection(arr):#создаем функцию перезаписи в список
    newArr = []#создаем пустой список
    for i in range(len(arr)):#проганяемся по массиву
        small = find_smallest(arr)#совершаем проверку по возрастанию
        newArr.append(arr.pop(small))#добавляем измененный элемент в список и при помощи pop возвращаем измененный массив
    return newArr# возвращаем список


print(sortSelection([111, 93, 100, 15, 24, 1]))#тест команда на то что все так работает