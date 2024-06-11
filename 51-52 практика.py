#Инкапсуляция - возможность программы скрыть атрибуты класса

def add_person():
    person_name = input("Введите фамилию и имя работника:")
    if person_name in data_base_staff:
        print("Такой работник уже есть!")
        return
    person_phone = int(input("Введите номер телефона:"))
    person_post = input("Введите e-mail:")
    person_position = input("Введите должность: ")
    person_room_number = input("Введите номер кабинета:")
    person_skype = input("Введите skype:")
    data_base_staff[person_name] = {"Имя и фамилия": person_name, "Телефон": person_phone, "Почта": person_post,
                                    "Должность": person_position, "Номер кабинета": person_room_number,
                                    "Skype": person_skype}
    print("Работник добавлен!")


def delete_person():
    person_name = input("Введите фамилию и имя работника:")
    if person_name not in data_base_staff:
        print("Такого работник нет!")
        return
    data_base_staff.pop(person_name)
    print("Работник удален!")


def find_person():
    person_name = input("Введите фамилию и имя работника:")
    if person_name not in data_base_staff:
        print("Такого работник нет!")
        return
    for person_name in data_base_staff:
        print("Работник:", data_base_staff[person_name])


def change_person():
    person_name = input("Введите фамилию и имя работника:")
    if person_name not in data_base_staff:
        print("Такого работник нет!")
        return
    data_base_staff.pop(person_name)
    person_name1 = input("Введите новые фамилию и имя работника:")
    person_phone = int(input("Введите новый номер телефона:"))
    person_post = input("Введите новый e-mail:")
    person_position = input("Введитет новую должность: ")
    person_room_number = input("Введите новый номер кабинета:")
    person_skype = input("Введите новый skype:")
    data_base_staff[person_name] = person_name1, person_phone, person_post, person_position, person_room_number, person_skype
    print("Данные успешно изменены!")


if __name__ == "__main__":
    data_base_staff = {}

while True:
    print("1. Добавить работника")
    print("2. Удалить работника")
    print("3. Найти работника")
    print("4. Изменить данные работника")
    print("0. Выход!")
    user_choice = input("Выберите операцию: ")
    match user_choice:
        case "1": add_person()
        case "2": delete_person()
        case "3": find_person()
        case "4": change_person()
        case "0": quit()
        case _: print("Неизвестная операция!")



class Strana:
    tuple1 = ("Санкт-Петербург","Псков","Калининград", "Воронеж", "Ростов-на-Дону")
    def __init__(self, name_strany:str, name_kontin:str, colvo_peoples:int, phone_cod:int, name_stolic:str, name_gorodov:str):
        self.name_strany = name_strany
        self.name_kontin =name_kontin
        self.colvo_peoples = colvo_peoples
        self.phone_cod = phone_cod
        self.name_stolic =name_stolic
        self.name_gorodov = name_gorodov

    def setName_strany(self)->None:
        self.name_strany = str(input("Введите название страны: "))

    def setName_kontin(self)->None:
        self.name_kontin = str(input("Введите название континента: "))

    def setColvo_peoples(self)->None:
        self.colvo_peoples = int(input("Введите количество жителей в стране: "))

    def setphone_cod(self)->None:
        self.phone_cod = int(input("Введите телефонный код страны: "))

    def setname_stolic(self)->None:
        self.name_stolic = str(input("Введите название столицы: "))

    def setname_gorodov(self)->None:
        self.name_gorodov = str(input("Введите название городов страны: "))

    def getName_strany(self)->str:
        return self.name_strany

    def getName_kontin(self)->str:
        return self.name_kontin

    def getColvo_peoples(self)->int:
        return self.colvo_peoples

    def getPhone_cod(self)->int:
        return self.phone_cod

    def getName_stolic(self)->str:
        return self.name_stolic

    def getName_gorodov(self)->str:
        return self.name_gorodov

    def display(self):
        print(f"Название страны: {self.name_strany}")
        print(f"Название континента: {self.name_kontin}")
        print(f"Количество жителей в стране: {self.colvo_peoples}")
        print(f"Телефонный код страны: {self.phone_cod}")
        print(f"Название столицы: {self.name_stolic}")
        print(f"Название городов страны: {self.name_gorodov}")

objStrana = Strana("Россия", "Евразия", 150000000, +7, "Москва", Strana.tuple1)
objStrana.display()

objStrana.setName_strany()
print(objStrana.getName_strany())

objStrana.setName_kontin()
print(objStrana.getName_kontin())

objStrana.setColvo_peoples()
print(objStrana.getColvo_peoples())

objStrana.setphone_cod()
print(objStrana.getPhone_cod())

objStrana.setname_stolic()
print(objStrana.getName_stolic())

objStrana.setname_gorodov()
print(objStrana.getName_gorodov())


















class Person:
    def __init__(self, FIO:str, age:int, salary:float):
        self.FIO = FIO
        self.age = age
        self.__salary = salary

    def display(self):
        print(f"ФИО: {self.FIO}")
        print(f"Возраст: {self.age}")
        print(f"Зарплату: {self.__salary}")

    def getSalary(self)->float:
        return self.__salary

objPerson = Person("Иванов И.И", 25, 50000)
objPerson.display()
#вывод данных об объекте
print(objPerson.FIO) #атирбут открыт и можем его вывести
#бращение к закрытому арибуту - бъект._имяКласса__имяАтрибутов
print(objPerson._Person__salary)#атрибут закрыли
print(objPerson.getSalary())
#изменение ФИО
objPerson.FIO = "Петров П.П"
objPerson.display()




print()



#Разбор классов дробь
class Fraction: #класс дробь
    def __init__(self, numenator, denominator): #numenator - числитель, denominator - знаментель
        self.numenator = numenator
        while denominator == 0:
            print(f"Знаменатель не может быть равен 0.")
            denominator = int(input("Введите значение заново: "))
        self.denominator = denominator
        print("Вызван метод __init__() класса Fraction")
    #метод для сложения 2 объектов(дробей)
    def summa(self, objFr2):

        if self.denominator==objFr2.denominator: #если равны знаменатели обеих дробей
            print(f"{self.numenator + objFr2.numenator} \n --- \n {objFr2.denominator}")
        else: #если не равны знаменатели обеих дробей
            print(f"{self.numenator * objFr2.denominator + self.denominator * objFr2.numenator} \n --- \n {self.denominator * objFr2.denominator}")
objFr1 = Fraction(3,4)
objFr2 = Fraction(int(input("Числитель: ")),
                  int(input("Знаменатель: ")))
objFr1.summa(objFr2)
