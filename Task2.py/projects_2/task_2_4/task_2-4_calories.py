protein = float(input("Введите массу белков: "))
fat = float(input("Введите массу жиров: "))
carb = float(input("Введите массу углеводов :"))
calories = protein * 4 + fat * 9 + carb * 4
print(f"Каллорийность продукта: {calories} ккал")