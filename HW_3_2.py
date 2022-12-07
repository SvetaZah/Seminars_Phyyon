#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#in
#4
#out
#[2, 5, 8, 10]
#[20, 40]

from random import sample
def List_rand_nums (count: int):
    if count < 0:
       print("Negativ value of the numbers of numbers!")
       return []
    list_nums = sample(range(1, count * 2), count)
    return list_nums

def prod_pairs (list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums [k] * list_nums [len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums [len_list // 2])
    return res_list

all_list = List_rand_nums(int (input ("Number of numbers: ")))
print(all_list)
print(prod_pairs(all_list))   
    