def add_item(shopping_list):
    name = input("Insert name: ")
    quantity = int(input("Insert quantity: "))
    price = float(input("Insert price: "))

    item = {"name": name,
          "quantity": quantity,
          "price": price
    }

    shopping_list.append(item)
    print(f"✅ {name} added!")

def show_list(shopping_list):
    # shopping_list = [{"name = bread}]
    # for i in range (len(shopping_list)):
    #     print(f"{i+1}. {shopping_list[i]["name"]} - {shopping_list[i]["quantity"]} x {shopping_list[i]["price"]} Eur")
    if not shopping_list:
        print("\nList is empty")
        return

    print("\nYour list: ")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item["name"]} - {item["quantity"]} x {item["price"]}€")


def count_total(shopping_list):
    total = 0
    for item in shopping_list:
        total =+ item["quantity"] * item["price"]
        print(f'Total price: {total:.2f}€')
def save_to_file(shopping_list):
    with open("text.txt", "w", encoding="utf-8") as f:
        for i, item in enumerate(shopping_list, start=1):
            f.write(f"{i}. {item["name"]} - {item["quantity"]} x {item["price"]}€\n")
    print("shopping list saved to text.txt")

def upload_file():
    shopping_list = []
    with open("text.txt", "r", encoding="utf-8") as f:
        for line in f:
            line_list = line.strip()[:-1].split()
            # for i in range(1, len(line_list), 2):
            print(line_list)
            name, quantity, price = line_list[1], line_list[3], line_list[5]
            item = {
                "name": name,
                "quantity": int(quantity),
                "price": float(price)
            }
            shopping_list.append(item)
    print("✅Load file")
    return shopping_list




def main():
    print("Вітаю у менеджері покупок!")
    shopping_list = []
    while True:
        print('''
    Меню:
    1. добавить покупку
    2. просмотреть список
    3. посчитать общ сумму
    4. Сохранить
    5. загрузить из файла
    6. Выход
            ''')
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Enter number 1-6")
            continue
            choice = int(input("Your  choice: "))
            # if choice == 1:
            #     pass
            # elif choice == 2:
            #     pass
        match choice:
            case 1:
                try:
                    add_item(shopping_list)
                except Exception as e:
                    print(f"Your error: {e}")
            case 2:
                show_list(shopping_list)
            case 3:
                count_total(shopping_list)
            case 4:
                save_to_file(shopping_list)
            case 5:
                try:
                    shopping_list = upload_file()
                except FileNotFoundError:
                    print("File not found")
            case 6:
                print("See You!")
                break
            case _:
                print ("Error! Enter number 1-6!")
        except ValueError:
                print("Enter number 1-6!")

if __name__ == "__main__":
    main()



