# Запит користувача на введення ім'я та прізвища
name = input("Введіть своє ім'я: ")
surname = input("Введіть своє прізвище: ")

# Запит користувача на введення номеру телефону (необов'язково)
phone_number = input("Введіть свій номер телефону (необов'язково): ")

# Перевірка чи хоча б одне поле не є порожнім
if name or surname or phone_number:
    print("Спасибі")
else:
    print("Не залишайте всі поля порожніми")


#Якщо хоча б одне поле заповнено, виводиться "Спасибі". Номер телефону вводити необов'язково, і це не вплине на вивід "Спасибі".