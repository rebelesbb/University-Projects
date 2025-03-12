#include "participants_functions.h"
#include "participants_tests.h"
#include "list.h"
#include <assert.h>
#include <string.h>
#include <crtdbg.h>
#include <stdio.h>
#include <stdlib.h>

///list and participant

void test_create_list()
{
    ElementsList participants = create_list();

    assert(get_size(&participants) == 0);
    assert(get_capacity(&participants) == 10);
    for(int index = 0; index < participants.capacity; index++)
        assert(sizeof(participants.nr) == sizeof(Participant*));

    free_list(&participants);
}

void test_create_participant()
{
    Participant* participant = create_participant("Prenume", "Nume", 150);

    assert(strcmp(get_first_name(participant),"Prenume") == 0);
    assert(strcmp(get_last_name(participant),"Nume") == 0);
    assert(get_score(participant) == 150);

    free_participant(participant);
}

void test_equal()
{
    Participant *participant1, *participant2, *participant3;
    participant1 = create_participant("Prenume","Nume", 150);
    participant2 = create_participant("Prenume", "Nume", 150);
    participant3 = create_participant("Prenume3", "Nume3", 150);

    assert(equal(*participant1, *participant2));
    assert(!equal(*participant1,*participant3));

    set_first_name(participant2,"Prenumele");
    assert(!equal(*participant1,*participant2));

    set_first_name(participant2,"Prenume");
    set_score(participant2,151);
    assert(!equal(*participant2, *participant1));

    free_participant(participant2);
    free_participant(participant1);
    free_participant(participant3);
}

void test_valid()
{
    ElementsList participants = create_list();
    Participant* participant;
    char err[5][100];
    int len;
    participant = create_participant("prenume","nume",20);
    assert(valid(&participants,*participant, err, &len));
    assert(len == 0);

    store(&participants,participant);
    assert(!valid(&participants,*participant, err, &len));
    assert(len == 1);

    for(int i = 0; i < strlen(err[0]); i++)
        err[0][i] = '\0';

    participant = create_participant("jav3", "ashj4", 101);
    assert(!valid(&participants,*participant,err,&len));
    assert(len == 3);
    free_participant(participant);

    participant = create_participant("jav3", "ashj4", -3);
    assert(!valid(&participants, *participant, err, &len));
    assert(len == 3);

    free_list(&participants);
    free_participant(participant);
}

void test_resize()
{
    ElementsList participants = create_list();
    unsigned long long total_capacity = 0;
    for(int i = 0; i < participants.capacity; i++)
        total_capacity += sizeof(participants.nr[i]);

    Participant* participant = create_participant("name", "last_name", 40);
    store(&participants, participant);

    assert(equal(*get_element(&participants, 0), *participant));
    assert(participants.capacity == 10);
    assert(total_capacity == participants.capacity * sizeof(Participant*));
    resize(&participants);


    total_capacity = 0;
    for(int i = 0; i < participants.capacity; i++)
        total_capacity += sizeof(participants.nr[i]);

    assert(participants.capacity == 20);
    assert(total_capacity == participants.capacity * sizeof(Participant*));
    assert(equal(*get_element(&participants, 0), *participant));
    free_list(&participants);

}

void test_store()
{
    ElementsList participants = create_list();
    Participant *participant1, *participant2, *participant3;
    participant1 = create_participant("Prenume","Nume", 150);
    participant2 = create_participant("Prenume", "Nume", 160);
    participant3 = create_participant("Prenume3", "Nume3", 150);

    store(&participants, participant1);
    store(&participants, participant2);
    store(&participants, participant3);
    store(&participants, create_participant("Prenume3", "Nume3", 150));
    store(&participants, create_participant("Prenume3", "Nume3", 150));
    store(&participants, create_participant("Prenume3", "Nume3", 150));
    store(&participants, create_participant("Prenume3", "Nume3", 150));
    store(&participants, create_participant("Prenume3", "Nume3", 150));
    store(&participants, create_participant("Prenume3", "Nume3", 150));
    store(&participants, create_participant("Prenume3", "Nume3", 150));

    assert(participants.capacity == 10);
    store(&participants, create_participant("Prenume3", "Nume3", 150));
    assert(participants.nr != NULL);
    assert(participants.capacity == 20);


    assert(equal(*get_element(&participants, 0), *participant1));
    assert(equal(*get_element(&participants, 1), *participant2));
    assert(equal(*get_element(&participants, 2), *participant3));
    assert(participants.capacity == 20);

    free_list(&participants);
}

void test_find()
{
    ElementsList participants = create_list();
    Participant *participant1, *participant2, *participant3;
    participant1 = create_participant("Prenume","Nume", 150);
    participant2 = create_participant("Prenume", "Nume", 160);
    participant3 = create_participant("Prenume3", "Nume3", 150);
    store(&participants, participant1);
    store(&participants, participant2);
    store(&participants, participant3);

    assert(find(&participants,*participant1) == 0);
    assert(find(&participants,*participant3) == 2);
    assert(find(&participants,*participant2) == 1);
    participant3 = create_participant("asd","asd",20);
    assert(find(&participants, *participant3) == -1);

    free_list(&participants);
    free_participant(participant3);
}

void test_delete()
{
    ElementsList participants = create_list();
    Participant *participant1, *participant2, *participant3, *participant4;
    participant1 = create_participant("Prenume","Nume", 150);
    participant2 = create_participant("Prenume", "Nume", 160);
    participant3 = create_participant("Prenume3", "Nume3", 150);
    store(&participants, participant1);
    store(&participants, participant2);
    store(&participants, participant3);

    assert(get_size(&participants) == 3);

    int position = find(&participants,*participant1);
    delete(&participants,position);
    assert(get_size(&participants) == 2);

    participant4 = create_participant("Prenume","Nume", 150);
    assert(!equal(*get_element(&participants, position), *participant4));
    free_participant(participant4);

    //participant4 = create_participant("Prenume", "Nume", 160);
    assert(equal(*get_element(&participants, position), *participant2));
    //free_participant(participant4);

    position = find(&participants, *participant2);
    delete(&participants,position);
    assert(get_size(&participants) == 1);

    position = find(&participants, *participant3);
    delete(&participants,position);
    assert(get_size(&participants) == 0);
    free_list(&participants);
}

void test_update()
{
    ElementsList participants = create_list();
    Participant *participant1, *participant2, *participant3, *participant4;
    participant1 = create_participant("Prenume1","Nume1", 150);
    participant2 = create_participant("Prenume2", "Nume2", 160);
    store(&participants, participant1);
    store(&participants, participant2);

    participant3 = create_participant("Prenume1","Nume1", 200); // = initial participant1
    participant4 = create_participant("Prenume4", "Nume4", 200);

    update(&participants,participant4,find(&participants, *participant1));
    assert(equal(*get_element(&participants, 0), *participant4));
    assert(!equal(*get_element(&participants, 0), *participant3));
    free_participant(participant3);

    participant3 = create_participant("Prenum3", "Num3", 20); // = initial participant1
    update(&participants,participant3,0);

    participant4 = create_participant("Prenume","Nume", 150);
    assert(!equal(*get_element(&participants, 0), *participant4));
    free_participant(participant4);

    participant4 = create_participant("Prenume","Nume", 160); // = initial participant2
    assert(!equal(*get_element(&participants, 0), *participant4));
    free_participant(participant4);
    free_list(&participants);
}

///participants_function

void test_add_participant()
{
    ElementsList participants = create_list();
    Participant *participant;
    char err[5][100];
    int i, j, len = 0;


    add_participant(&participants, "Prenume", "Nume", 50, err, &len);
    assert(get_size(&participants) == 1);

    participant = create_participant("Prenume", "Nume", 50);
    assert(equal(*get_element(&participants, 0), *participant));
    free_participant(participant);

    assert(len == 0);

    add_participant(&participants, "Prenume", "Nume", 50, err, &len);
    assert(get_size(&participants) == 1);
    assert(len == 1);

    len = 0;
    for(i = 0; i < strlen(err[0]); i++)
        err[0][i] = '\0';

    add_participant(&participants, "Prenume2", "Nume2", 101, err, &len);
    assert(get_size(&participants) == 1);
    assert(len == 3);

    for(j = 0; j < len; j++)
        for(i = 0; i < strlen(err[j]); i++)
            err[j][i] = '\0';
    len = 0;

    add_participant(&participants, "asd", "asd", 100, err, &len);
    assert(get_size(&participants) == 2);

    participant = create_participant("asd", "asd", 100);
    assert(equal(*get_element(&participants, 1), *participant));
    free_participant(participant);
    free_list(&participants);
}

void test_delete_participant()
{
    ElementsList participants = create_list();
    Participant *participant1, *participant2, *participant3, *participant_copy;
    participant1 = create_participant("Ion","Popescu", 50);
    participant2 = create_participant("Ion", "Popescu", 60);
    participant3 = create_participant("Ana", "Georgescu", 100);
    store(&participants, participant1);
    store(&participants, participant2);
    store(&participants, participant3);

    char err[5][100];
    int i, j, len = 0;

    assert(get_size(&participants) == 3);

    participant_copy = create_participant("Ion","Popescu", 60);
    delete_participant(&participants, "Ion", "Popescu", 60, err, &len);
    assert(get_size(&participants) == 2);
    assert(len == 0);

    delete_participant(&participants, "Nume", "Prenume", 20, err, &len);
    assert(get_size(&participants) == 2);
    assert(find(&participants, *participant_copy) == -1);
    assert(len == 1);
    free_participant(participant_copy);


    for(j = 0; j < len; j++)
        for(i = 0; i < strlen(err[j]); i++)
            err[j][i] = '\0';
    len = 0;

    participant_copy = create_participant("Ion","Popescu", 50);
    delete_participant(&participants, "Ion", "Popescu", 50, err, &len);
    assert(get_size(&participants) == 1);
    assert(find(&participants, *participant_copy) == -1);
    assert(len == 0);
    free_participant(participant_copy);

    participant_copy = create_participant("Ana", "Georgescu", 100);
    delete_participant(&participants, "Ana", "Georgescu", 100, err, &len);
    assert(get_size(&participants) == 0);
    assert(find(&participants, *participant_copy) == -1);
    assert(len == 0);
    free_participant(participant_copy);

    delete_participant(&participants, "Ion", "Popescu", 20, err, &len);
    assert(len == 1);
    free_list(&participants);
}

void test_update_participant()
{
    char err[5][100];
    int len = 0, i ,j;
    ElementsList participants = create_list();

    update_participant(&participants, 0, "Gheorghe", "Gheorghescu", 100, err, &len);
    assert(len == 1);
    for(j = 0; j < len; j++)
        for(i = 0; i < strlen(err[j]); i++)
            err[j][i] = '\0';
    len = 0;

    Participant *participant1, *participant2;
    participant1 = create_participant("Ion","Popescu", 50);
    participant2 = create_participant("Ion","Popescu", 50);
    store(&participants, participant1);


    update_participant(&participants, 0, "Gheorghe", "Gheorghescu", 100, err, &len);
    assert(find(&participants, *participant2) == -1);
    assert(len == 0);
    free_participant(participant2);

    participant2 = create_participant("Gheorghe", "Gheorghescu", 100);

    update_participant(&participants, 0, "Ghe0rghe", "Gheorgh2", 101, err, &len);
    assert(find(&participants, *participant2) == 0);
    assert(len == 3);
    free_participant(participant2);


    for(j = 0; j < len; j++)
        for(i = 0; i < strlen(err[j]); i++)
            err[j][i] = '\0';
    len = 0;

    participant2 = create_participant("Gheorghe", "Gheorghescu", 100);
    update_participant(&participants, 0, "-1", "-1", -1, err, &len);
    assert(len == 0);
    assert(find(&participants, *participant2) == 0);

    free_participant(participant2);
    free_list(&participants);
}

void test_sort_list()
{
    char err[5][100];
    int len = 0;
    ElementsList participants = create_list();

    sort_list(&participants, "scor", false, err, &len);
    assert(len == 1);

    Participant *participant1, *participant2, *participant3, *participant5, *participant6, *participant7;
    participant1 = create_participant("Ion","Popescu", 50);
    participant2 = create_participant("Ion", "Popescu", 60);
    participant3 = create_participant("Ana", "Georgescu", 100);
    participant5 = create_participant("Rares","Rares", 60);
    participant6 = create_participant("Ion", "Anghel", 40);
    participant7 = create_participant("Ana", "Zenobia", 90);
    store(&participants, participant1);
    store(&participants, participant2);
    store(&participants, participant3);
    store(&participants, participant5);
    store(&participants, participant6);
    store(&participants, participant7);

    ElementsList sorted_list = create_list();
    participant1 = create_participant("Ion", "Anghel", 40);
    participant3 = create_participant("Ana", "Georgescu", 100);
    participant2 = create_participant("Rares","Rares", 60);
    participant5 = create_participant("Ion", "Popescu", 60);
    participant6 = create_participant("Ion","Popescu", 50);
    participant7 = create_participant("Ana", "Zenobia", 90);
    store(&sorted_list,participant1);
    store(&sorted_list,participant3);
    store(&sorted_list,participant6);
    store(&sorted_list,participant5);
    store(&sorted_list,participant2);
    store(&sorted_list,participant7);

    sort_list(&participants, "nume", false, err, &len);

    int size = get_size(&participants);
    for(int i = 0; i < size; i++)
        if(!equal(*get_element(&participants, i), *get_element(&sorted_list, i)))
            assert(false);

    free_list(&sorted_list);

    sorted_list = create_list();
    assert(get_size(&sorted_list) == 0);

    participant1 = create_participant("Ion", "Anghel", 40);
    participant3 = create_participant("Ana", "Georgescu", 100);
    participant2 = create_participant("Rares","Rares", 60);
    participant5 = create_participant("Ion", "Popescu", 60);
    participant6 = create_participant("Ion","Popescu", 50);
    participant7 = create_participant("Ana", "Zenobia", 90);

    store(&sorted_list,participant3);
    store(&sorted_list,participant7);
    store(&sorted_list,participant2);
    store(&sorted_list,participant5);
    store(&sorted_list,participant6);
    store(&sorted_list,participant1);

    sort_list(&participants, "scor", true, err, &len);

    for(int i = 0; i < size; i++)
        if(!equal(*get_element(&participants, i), *get_element(&sorted_list, i)))
            assert(false);

    free_list(&sorted_list);

    sorted_list = create_list();
    assert(get_size(&sorted_list) == 0);

    participant1 = create_participant("Ion", "Anghel", 40);
    participant3 = create_participant("Ana", "Georgescu", 100);
    participant2 = create_participant("Rares","Rares", 60);
    participant5 = create_participant("Ion", "Popescu", 60);
    participant6 = create_participant("Ion","Popescu", 50);
    participant7 = create_participant("Ana", "Zenobia", 90);

    store(&sorted_list,participant1);
    store(&sorted_list,participant6);
    store(&sorted_list,participant2);
    store(&sorted_list,participant5);
    store(&sorted_list,participant7);
    store(&sorted_list,participant3);

    sort_list(&participants, "scor", false, err, &len);

    for(int i = 0; i < size; i++)
        if(!equal(*get_element(&participants, i), *get_element(&sorted_list, i)))
            assert(false);

    free_list(&sorted_list);

    sorted_list = create_list();
    assert(get_size(&sorted_list) == 0);

    participant1 = create_participant("Ion", "Anghel", 40);
    participant3 = create_participant("Ana", "Georgescu", 100);
    participant2 = create_participant("Rares","Rares", 60);
    participant5 = create_participant("Ion", "Popescu", 60);
    participant6 = create_participant("Ion","Popescu", 50);
    participant7 = create_participant("Ana", "Zenobia", 90);

    store(&sorted_list,participant7);
    store(&sorted_list,participant2);
    store(&sorted_list,participant5);
    store(&sorted_list,participant6);
    store(&sorted_list,participant3);
    store(&sorted_list,participant1);

    sort_list(&participants, "nume", true, err, &len);

    for(int i = 0; i < size; i++)
        if(!equal(*get_element(&participants, i), *get_element(&sorted_list, i)))
            assert(false);

    free_list(&sorted_list);

    sort_list(&participants, "jhad", true, err, &len);
    assert(len == 2); ///didn't set len back on one after checking the empty list error

    free_list(&participants);
}

void test_filter_participants()
{
    int index;
    char err[5][100];
    int len = 0;
    ElementsList participants, filtered_list;
    participants = create_list();
    filtered_list = create_list();

    ///check potential errors and set len back on 0 only after
    filter_participants(&participants, &filtered_list, "scor", "20", err, &len);
    assert(len == 1);

    Participant *participant1, *participant2, *participant3, *participant4, *participant5;
    participant1 = create_participant("Ion","Popescu", 50);
    participant2 = create_participant("Ion", "Popescu", 60);
    participant3 = create_participant("Ana", "Georgescu", 100);
    participant4 = create_participant("Rares","Rares", 60);
    participant5 = create_participant("Ion", "Anghel", 40);
    store(&participants, participant1);
    store(&participants, participant2);
    store(&participants, participant3);
    store(&participants, participant4);
    store(&participants, participant5);

    filter_participants(&participants, &filtered_list, "scor", "-1", err, &len);
    assert(len == 2);

    filter_participants(&participants, &filtered_list, "initiala", "0", err, &len);
    assert(len == 3);

    filter_participants(&participants, &filtered_list, "scor", "101", err, &len);
    assert(len == 4);

    len = 0;
    for(int i = 0; i < len; i++)
        for(index = 0; index < strlen(err[i]); index++)
            err[i][index] = '\0';

    filter_participants(&participants, &filtered_list, "scor", "70", err, &len);

    assert(filtered_list.length == 4);
    for(index = 0; index < filtered_list.length; index++)
        assert(get_score(get_element(&filtered_list, index)) < 70);

    free_list(&filtered_list);

    filtered_list = create_list();

    filter_participants(&participants, &filtered_list, "initiala", "P", err, &len);
    assert(get_size(&filtered_list) == 2);
    for(index = 0; index < filtered_list.length; index++)
        assert(get_last_name(get_element(&filtered_list, index))[0] == 'P');

    free_list(&filtered_list);


    filtered_list = create_list();

    filter_participants(&participants, &filtered_list, "initia", "Q", err, &len);
    assert(len == 1);

    free_list(&filtered_list);


    free_list(&participants);

}

void test_functions()
{
    test_create_list();
    test_create_participant();
    test_equal();
    test_valid();
    test_resize();

    test_store();
    test_find();
    test_delete();
    test_update();

    test_add_participant();
    test_delete_participant();
    test_update_participant();
    test_sort_list();
    test_filter_participants();
}