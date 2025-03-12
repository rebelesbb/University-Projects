from domain import task
def print_menu():
    print('1. Adaugare task')
    print('2. Cautare task cu deadline intre 2 date')
    print('3. Stergere task dupa descriere')
    print('4. Eliminare task-uri dupa status')
    print('5. Filtrare: afisare task-uri carre contin in descriere string')
    print('6. Afisare raport pe luna')
    print('7. Undo')
    print('P. Afisarea tuturor task-urilor')
    print('A. Adaugare task-uri default')
    print('E. Iesire')

def print_task_list(task_list):
    for task in task_list:
        print(task)

def start():
    task_list = []
    while True:
        print_menu()
        option = input('>')
        option = option.upper().strip()
        if option == "P":
            print_task_list(task_list)
        elif option == "A":
            pass
        elif option == '1':
            descriere = input("Introduceti descrierea:")
            data = input("Introduceti data:")
            status = input("Introduceti status:")

            task = create_task(descriere, data, status)
            add_task(task_list, task)
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == '6':
            pass
        elif option == '4':
            pass
        elif option == "E":
            break
        else:
            print("Invalid option.")

