donor = input("Введите фенотип группы крови (I, II, III, IV): ").upper()
recipient = input("Введите фенотип группы крови (I, II, III, IV): ").upper()
if donor == "I" or donor == recipient:
    print("Можно переливать")
else:
    print("Нельзя переливать")
