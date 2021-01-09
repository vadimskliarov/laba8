




def add(peoples,name, name1, number, dat):
    peopl = {
        'name': name,
        'name1': name1,
        'number': number,
        'day' : day
    }

    peoples.append(people)
    if len(peoples) > 1:
        peoples.sort(key=lambda item: item.get('type', ''))


def list(peoples):
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "Имя",
            "Фамилия",
            "Номер телефона",
            "День рождения"
        )
    )
    table.append(line)

    for idx, people in enumerate(peoples, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
               people.get('name', ''),
               people.get('name1', ''),
               people.get('number', )
            )
        )

    table.append(line)

    return '\n'.join(table)


def select(airplane, period):

    result = []
    for people in peoples:
        if period == people.get('name'):
            result.append(people)

    return result


if __name__ == '__main__':
    peoples = []

    while True:
        command = input(">>> ")

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Имя")
            name1 = input("Фамилия")
            number = input("Номер телефона")
            day = input('День рождения')



        elif command == 'list':
            print(list(peoples))

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            selected = select(peoples, parts[1])
            count = 0
            if selected:
                for idx, people in enumerate(selected, 1):
                    print(
                        '{:>4}: {}, Тип самолета - {}, Номер рейса - {}'.format(count, people.get('name', ''),
                                                                                       people.get('name1', ''),
                                                                                       people.get('number', '')

                                                                                )
                    )
            else:
                print("Рейс с таким названием не найден.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить рейс;")
            print("list - Вывести список людей;")
            print("select <Рейс> - Вывести всю информацию  о человеке;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)