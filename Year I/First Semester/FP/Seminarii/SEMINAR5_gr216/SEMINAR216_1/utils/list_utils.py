def make_list_copy(list_of_dicts):
    """
    Face o copie a listei (de dictionare) date
    :param list_of_dicts: lista de dictionare
    :return: copie a listei
    """
    new_list = []
    for element in list_of_dicts:
        new_element = {}
        for key, value in element.items():
            new_element[key] = value

        new_list.append(new_element)
    return new_list
