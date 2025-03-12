
def create_task(descriere: str, data: str, status: str) -> dict:
    """
    Creeaza un task
    :param descriere: descrierea task-ului
    :type descriere: str
    :param data: data task-ului (dd-mm)
    :type data: str
    :param status: status-ul task-ului
    :type status: str
    :return: task-ul creat
    :rtype: dict
    """
    elements_date = data.split('-')
    day = int(elements_date[0].strip())
    month = int(elements_date[1].strip())
    return {'descriere': descriere, 'zi_deadline': day,
            'luna_deadline': month, 'status': status}

def test_create_task():
    # assert
    # testez creare de task

    task = create_task("HostMovieMarathon", "11-12", "pending")
    assert (type(task) == dict)
    assert (type(task) != list)

    assert (task['descriere'] == "HostMovieMarathon")
    assert (task['zi_deadline'] == 11)
    assert (task['luna_deadline'] == 12)
    assert (task['status'] == "pending")