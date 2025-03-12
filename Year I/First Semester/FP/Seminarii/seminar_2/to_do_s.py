def print_menu():
    print("1.Citire lista")
    print("2.Adaugare\n3.Filtrare\n4.Afisare")
    print("5.Iesire")

#BookSkydivingAdventure_18_in-progress, LearnJuggling_25_pending, StartVegetableGarden_27_in-progress
def read_list():
    lista = input("Introduceti taskurile:\n")
    taskuri = lista.split(',')
    taskuri = [task.strip() for task in taskuri]
    return taskuri

def read_task() :
    descriere = input("Descriere: ")
    zi_deadline = int(input("Zi deadline: "))
    status = input( "Status: ")
    return descriere+'_' + str(zi_deadline) + '_' + status

def adauga_in_lista(my_list) :
    task = read_task()
    my_list.append(task)

lista_taskuri = []
while True:
    print_menu()
    optiune = int(input("Introduceti optiunea: "))

    if  optiune == 1 :
        lista_taskuri = read_list()
        print('Lista este: ', lista_taskuri)
    elif optiune == 2 :
        adauga_in_lista(lista_taskuri)
    elif optiune == 3:
        pass
    elif optiune == 4 :
        print(lista_taskuri)
    if optiune == 5:
        break