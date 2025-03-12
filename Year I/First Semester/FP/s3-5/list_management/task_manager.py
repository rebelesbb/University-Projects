def add_task(task_list, task):
    """
    Adauga task-ul dat in lista de task-uri
    :param task_list: lista in care se adauga
    :type task_list: list
    :param task: task-ul care se adauga
    :type task: dict
    :return: -; modifica task_list adaugand la sfarsit task-ul dat
    :rtype: -
    """
    task_list.append(task)

def test_add():
    # testez adaugare in lista
    test_task_list = []
    assert (len(test_task_list) == 0)

    task = create_task("HostMovieMarathon", "11-12", "pending")
    add_task(test_task_list, task)
    assert (len(test_task_list) == 1)
    assert (test_task_list[0]['descriere'] == 'HostMovieMarathon')

def test_cautare():
    test_task_list = []
    assert (len(test_task_list) == 0)

    # + add default task
    task = create_task("HostMovieMarathon", "11-12", "pending")
    add_task(test_task_list, task)
    assert (len(test_task_list) == 1)
    assert (test_task_list[0]['descriere'] == 'HostMovieMarathon')