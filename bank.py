def bank():
    try:
        with open('balance.txt', 'r') as f:
            balance = int(f.read())
    except:
        balance = 0
    try:
        with open('history.txt', 'r') as f:
            history = f.read()
            if history:
                history = history[2:-2].split('), (')
                history = [(h.split(', ')[0][1:-1], int(h.split(', ')[1])) for h in history]
            else:
                history = []
    except:
        history = []
    print(balance, history)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. сохранение суммы счета в файл')
        print('5. сохранение истории покупок в файл')
        print('6. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            balance += int(input('введите сумму на сколько пополнить счет'))
        elif choice == '2':
            price = int(input('введите сумму покупки'))
            if balance < price:
                print('денег не хватает')
            else:
                goods = input('введите название покупки')
                balance -= price
                history.append((goods, price))
        elif choice == '3':
            print(history)
        elif choice == '4':
            with open('balance.txt', 'w') as f:
                f.write(str(balance))
        elif choice == '5':
            with open('history.txt', 'w') as f:
                f.write(str(history))
        elif choice == '6':
            return
        else:
            print('Неверный пункт меню')