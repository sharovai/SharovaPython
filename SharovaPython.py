first_input = input("Введите число:")
try:
    your_number = int(first_input)
    if your_number > 7:
        print("Привет")
except ValueError:
    print(f"Ошибка!{first_input} не является числом!")

second_input = str(input("Напишите имя:"))
if second_input == "Вячеслав":
    print("Привет, Вячеслав")
else:
    print("Нет такого имени")

third_input = input("Введите числовой массив(например:1 2 3 4):")
try:
    numbers = third_input.split()
    new_list = []
    for x in numbers:
        if int(x) % 3 == 0 and int(x) != 0:
            new_list.append(x)

    print(new_list)
except ValueError:
    print(f"Ошибка!{third_input} не является числовым массивом!")
