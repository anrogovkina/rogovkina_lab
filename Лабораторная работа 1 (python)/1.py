numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing =4
new_numbers=numbers[:missing]+numbers[missing+1:]
average = sum(new_numbers)/len(numbers)
numbers[missing]=average
print("Измененный список:",numbers)
