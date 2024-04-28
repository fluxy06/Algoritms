# функция бинарной сортировки
def binary_serch(list, item):
    low = 0 #переменная начало массива
    hight = len(list)-1 #переменная берет количество элементов массива -1 
    
    while low <= hight:
        mid = low + hight
        guess = list[mid]
        if guess == item:
            return mid
        if guess >= item:
            hight = mid - 1
        else:
            low = mid + 1
            return None

m_l = [1, 3, 5, 7, 9]#пример отсортированного массива

print(binary_serch(m_l, 15))#проверяем есть ли в массиве 15