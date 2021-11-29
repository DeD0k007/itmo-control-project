import main

p = main.PhoneBook()

a = p.getContactByName("Nik")


try:
    p.postNewContact("Bill", "awdaw")
    print('Ok')
except ValueError:
    print("Вы ввели не номер а строку")
except SyntaxError:
    print("Произошла синтаксическая ошибка. кажется вы ввели число начинающееся на 0")
finally:
    try:
        a = p.getContactByName("Nik")
        if not a:
            print("Кажется такого человека нет в базе")
    except Exception:
        print("Произошла ошибка")

