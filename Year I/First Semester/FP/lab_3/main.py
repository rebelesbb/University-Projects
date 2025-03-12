#5,6

import re

def print_menu():
    """
    Prints out the menu
    """
    print("1.Citire lista")
    print("2.Determinare secventa de lungime maxima care are toate elementele egale")
    print("3.Determinare secventa de lungime maxima care are toate elementele distincte intre ele")
    print("4.Determinare secventa de lungime maxima in care oricare doua elemente au semne contare")
    print("5.Iesire din aplicatie\n")

def read_list() :
    """
     Reads a list of numbers
     returns a list of integer numbers
     :return : the list of numbers
     :rtypet : list
    """
    initial_list = input("Introduceti lista de numere: ")
    initial_list = initial_list.strip(', ')
    initial_list = re.split(r", | ", initial_list)
    list = [int(number) for number in initial_list]
    return list


def determine_longest_sequence_equal_elements(list):
    """
    Determines the longest sequence of consecutive elements,
    all of which are equal
    :parameter list: the list of elements
    :type list: list
    :return : the longest sequence of equal elements
    :rtype: list
    """
    list_length = len(list)

    # the indices of the first and last element of the longest sequence found in the list
    longest_sequence_start = longest_sequence_end = 0

    for current_sequence_start in range(list_length) :

        current_sequence_end = current_sequence_start + 1

        while current_sequence_end < list_length and list[current_sequence_start] == list[current_sequence_end] :
            current_sequence_end += 1

        current_sequence_end -= 1

        if longest_sequence_end - longest_sequence_start + 1 < current_sequence_end - current_sequence_start + 1 :
            longest_sequence_end = current_sequence_end
            longest_sequence_start = current_sequence_start

        current_sequence_start = current_sequence_end + 1

    if longest_sequence_end - longest_sequence_start + 1 < current_sequence_end - current_sequence_start + 1 :
        longest_sequence_end = current_sequence_end
        longest_sequence_start = current_sequence_start

    return list[longest_sequence_start:longest_sequence_end+1]

def determine_longest_sequence_unequal_elements(list) :

    """
    Determines and prints the longest sequence of consecutive elements,
    all of which have distinct values from one another
    :parameter list: the list of elements
    :type list: list
    :return : the longest sequence of distinct elements
    :rtype: list
    """

    list_length = len(list)

    #the indices of the first and last element of the longest sequence found in the list
    longest_sequence_start = longest_sequence_end = 0

    for current_sequence_start in range(list_length) :

        current_sequence_end = current_sequence_start + 1

        while current_sequence_end < list_length and len(list[current_sequence_start : current_sequence_end + 1]) == len(set(list[current_sequence_start : current_sequence_end + 1])):
            current_sequence_end += 1

        current_sequence_end -= 1

        #checks if the current list has a length greater than the longest one found so far
        if longest_sequence_end - longest_sequence_start + 1 < current_sequence_end - current_sequence_start + 1:
            longest_sequence_end = current_sequence_end
            longest_sequence_start = current_sequence_start

        current_sequence_start = current_sequence_end + 1

    #checks if the last sequence in the list satisfies the condition, because it wasn't checked in the for loop
    if longest_sequence_end - longest_sequence_start + 1 < current_sequence_end - current_sequence_start + 1 :
        longest_sequence_end = current_sequence_end
        longest_sequence_start = current_sequence_start

    return list[longest_sequence_start:longest_sequence_end+1]

def determine_longest_sequence_opposite_signs(list):
    """
    Determines the longest sequence of consecutive elements,
    in which any two consecutive elements have opposite signs
    :parameter list: the list of elements
    :type list: list
    :return : the longest sequence of elements with opposite signs
    :rtype: list
    """
    list_length = len(list)

    # the indices of the first and last element of the longest sequence found in the list
    longest_sequence_start = longest_sequence_end = 0

    for current_sequence_start in range(list_length) :

        current_sequence_end = current_sequence_start + 1

        while current_sequence_end < list_length and list[current_sequence_end]+list[current_sequence_end-1] != abs(list[current_sequence_end])+abs(list[current_sequence_end-1]) :
            current_sequence_end += 1

        current_sequence_end -= 1

        if longest_sequence_end - longest_sequence_start + 1 < current_sequence_end - current_sequence_start + 1 :
            longest_sequence_end = current_sequence_end
            longest_sequence_start = current_sequence_start

        current_sequence_start = current_sequence_end + 1

    # checks if the last sequence in the list satisfies the condition, because it wasn't checked in the for loop
    if longest_sequence_end - longest_sequence_start + 1 < current_sequence_end - current_sequence_start + 1 :
        longest_sequence_end = current_sequence_end
        longest_sequence_start = current_sequence_start

    return list[longest_sequence_start:longest_sequence_end+1]

def test_sequence_equal_elements():
    test_list = [11, 11, 2, 3, 2, 2, 2 ]
    assert(determine_longest_sequence_equal_elements(test_list) == [2, 2, 2])
    test_list = [23, 23, 23, 23, 2, 5, 7, 7, 7, 7]
    assert(determine_longest_sequence_equal_elements(test_list) == [23, 23, 23, 23])
    test_list = [1, 2, 3, 4, 5]
    assert(determine_longest_sequence_equal_elements(test_list) == [1])

def test_sequence_unequal_elements():
    test_list = [1, 2, 3, 3, 4, 5, 4]
    assert determine_longest_sequence_unequal_elements(test_list) == [1, 2, 3]
    test_list = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8]
    assert determine_longest_sequence_unequal_elements(test_list) == [4, 5, 6, 7, 8]
    test_list = [7, 2, 5, 18, 3]
    assert determine_longest_sequence_unequal_elements(test_list) == [7, 2, 5, 18, 3]

list = []
option = 1
test_sequence_unequal_elements()
test_sequence_equal_elements()
print_menu()
while True:
    option = int(input("Introduceti optiunea pe care o doriti: "))
    if option == 1 :
        list = read_list()
        print('Lista introdusa este:\n', list, '\n')
    elif option == 2 :
        sequence = determine_longest_sequence_equal_elements(list)
        print(sequence)
    elif option == 3 :
        sequence = determine_longest_sequence_unequal_elements(list)
        print(sequence)
    elif option == 4 :
        sequence = determine_longest_sequence_opposite_signs(list)
        print(sequence)
    elif option == 5:
        break