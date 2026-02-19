weight = float(input("Введите ваш вес: "))
height_cm = float(input("Введите ваш рост :"))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
print("\n--- Отчёт о состоянии здоровья ---")
print(f"Рост:\t{height_cm:.1f} см")
print(f"Вес:\t{weight:.1f} кг")
print(f"Индекс массы тела пациента:\t{bmi:.2f}")