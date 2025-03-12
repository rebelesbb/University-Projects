# clase si obiect
# clasa = mod de a crea propriile tipuri de date
# obiect = instanta unei clase
# ex. clasa = caine => obiect = cainele tau/ cainele meu/ un caine

class Task:
    # self face referire la obiect; e implicit, nu trebuie specificat
    def __init__(self, descriere, zi_deadline, luna_deadline, status):
        print("Init called")
        self.__descriere = descriere
        self.__zi_deadline = int(zi_deadline)
        self.__luna_deadline = int(luna_deadline)
        self.__status = status #__atribut <=> camp/atribut privat

    def get_descriere(self):
        return self.__descriere

    def get_zi_deadline(self):
        return self.__zi_deadline

    def get_luna_deadline(self):
        return self.__luna_deadline

    def get_status(self):  #metoda
        return self.__status

    def __str__(self):
        return 'Descriere: ' + self.get_descriere() + ' | Zi: ' + str(self.get_zi_deadline()) + ' | Status: ' + self.get_status()

    def __eq__(self, other):
        return self.__descriere == other.get_descriere() and self.__zi_deadline == other.get_zi_deadline() \
               and self.__status == other.get_status()


class Validator():
    def __init__(self):
        pass # nu primeste niciun parametru ca atribut

    def validare_task(self, task):
        # functia de validare de la s5 cu modificarile necesare

v = Validator()


t1 = Task("Book Skydiving Adventure",11,12,'pending')
t2 = Task("Book Skydiving Adventure",11,12,'pending')

#assert t1 == t2 eroare deoarece sunt doua obiecte diferite aflate la doua adrese diferite; trebuie
#sa definim noi ce inseamna doua obiecte egale

assert t1.__eq__(t2)

print(t1,'\n')






