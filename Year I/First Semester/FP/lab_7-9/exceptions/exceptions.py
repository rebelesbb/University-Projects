class BookRepositoryException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Repository exception: " + str(self.__msg)


class BookAlreadyExistsException(BookRepositoryException):
    def __init__(self):
        BookRepositoryException.__init__(self,"Cartea introdusa exista deja in lista.")


class ClientRepositoryException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Repository expection: " + str(self.__msg)


class ClientAlreadyExistsException(ClientRepositoryException):
    def __init__(self):
        ClientRepositoryException.__init__(self,"Clientul introdus exista deja in lista.")


# nu se cere nici la examen nici la simulare sa lucram cu PyUnit
