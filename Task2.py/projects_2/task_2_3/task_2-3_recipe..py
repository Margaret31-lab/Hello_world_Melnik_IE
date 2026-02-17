medium_name = input("Введите название среды: ")
agar_concentration = input("Введите концентрацию (%): ")
sterilization_temp = input("Введите температуру стерилизации: ")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium_name}\n")
    file.write(f"- Концентрация агара: {agar_concentration}")
    file.write(f"- Температура стерилизации:{sterilization_temp}")

print("Файл 'recipe.txt' успешно сформирован!")
