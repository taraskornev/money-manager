def add_item(shopping_list):
    pass
def show_list():
    pass
def count_total():
    pass
def save_to_file():
    pass
def upload_file():
    pass
def main():
    print("Ghbdtn d vty gjregjr привет")
    shopping_list = []
    while True:
        print('''
    Меню:
    1. добавить покупку
    2. просмотреть список
    3. посчитать общ сумму
    4. Сохранить
    5. загрузить с файла
    6. Выход
        ''')
        choice = int(input("Your choice: "))
        # if choice == 1:
        #     pass
        # elif choice == 2:
        #     pass
        match choice:
            case 1:
                add_item(shopping_list)
            case 2:
                show_list()
            case 3:
                count_total()
            case 4:
                save_to_file()
            case 5:
                upload_file()
            case 6:
                print("See You!")
                break
            case _:
                print ("Enter number 1-6!")


main()