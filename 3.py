#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#*Пример:*
#- x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
#x = int(input ("Введите координату X: "))
#y = int(input ("Введите координату Y: "))
#f x == 0 and y == 0:
 #   print("Начало координат")
#elif x == 0:
 #   print("на оси Y")
#elif y == 0:
 #   print("на оси X")
#elif x > 0 and y > 0:
  #  print("в I четверти")
#elif x < 0 and y > 0:
 #   print("во II четверти")
#elif x < 0 and y < 0:
   # print("в III четверти")
#else:
 #   print("в IV четверти")
x = int(input ())
y = int(input ())
if x > 0 and y > 0:
    print(1)
elif x < 0 < y:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 > y:
    print(4)
else:
    print("Ошибка!")

    