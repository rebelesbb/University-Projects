#include "Testing.h"
#include "List.h"
#include "Medicament.h"
#include "Undo.h"
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <stdio.h>

void test_create_list()
{
    MyList* list = createList();

    assert(list->lungime == 0);

    destroyList(list, (DestroyFunction) free); //????
}

void test_create_med()
{
    Medicament* med = createMed(1, "hello", 0.2, 20);
    Medicament* med2 = createMed(2, "hi", 0.4, 12);
    assert(med->cod == 1);
    assert(med->concentratie == 0.2);
    assert(med->cantitate == 20);
    assert(strcmp(med->nume, "hello") == 0);
    assert(med2->cod == 2);
    assert(med2->concentratie == 0.4);
    assert(med2->cantitate == 12);
    assert(strcmp(med2->nume, "hi") == 0);

    destroyMed(med);
    destroyMed(med2);
}

void test_add_medicament()
{

    MyList* list = createList();
    Medicament* med1 = createMed(1, "hello10", 0.2, 20);
    add_medicament(med1, list);

    assert(list->lungime == 1);
    assert(get_cod(get_element(list, 0)) == med1->cod);

    Medicament* med2 = createMed(1, "hello10", 0.2, 20);
    add_medicament(med2, list);
    assert(list->lungime == 1);

    destroyList(list, (DestroyFunction) destroyMed);

}

void test_validate()
{
    Medicament* med1 = createMed(1, "hello", 0.2, 20);
    Medicament* med2 = createMed(1, "hello", 0.2, 0);
    Medicament* med3 = createMed(-1, "hello", 0.2, 5);
    Medicament* med4 = createMed(5, "", 0.2, 5);
    Medicament* med5 = createMed(5, "", -0.5, 5);

    assert(validateMed(med1) == 0);
    assert(validateMed(med2) == 1);
    assert(validateMed(med3) == 1);
    assert(validateMed(med4) == 1);
    assert(validateMed(med5) == 1);

    destroyMed(med1);
    destroyMed(med2);
    destroyMed(med3);
    destroyMed(med4);
    destroyMed(med5);
}

void test_delete_medicament()
{
    MyList* list = createList();
    Medicament* med1 = createMed(1, "hello6", 0.2, 20);
    Medicament* med2 = createMed(2, "hello7", 0.2, 5);
    add_medicament(med1, list);
    add_medicament(med2, list);

    delete_medicament(1, list);

    assert(list->lungime == 1);
    assert(get_cod(list->elems[0]) == med2->cod);

    delete_medicament(2, list);
    assert(list->lungime == 0);


    destroyList(list, (DestroyFunction) destroyMed);
}

void test_modify_medicament()
{
    MyList* list = createList();

    Medicament* med1 = createMed(1, "hello5", 0.2, 20);
    Medicament* med2 = createMed(2, "hello4", 0.2, 5);
    add_medicament(med1, list);
    add_medicament(med2, list);

    modify_medicament(1, 0.3, "hi", list);
    modify_medicament(2, 0.4, "no", list);
    modify_medicament(3,0.2,"hello",list);

    assert(get_cod(list->elems[0]) == 1);
    assert(get_concentratie(list->elems[0]) == 0.3);
    assert(get_cantitate(list->elems[0]) == 20);
    assert(strcmp(get_nume(list->elems[0]), "hi") == 0);

    assert(get_cod(list->elems[1]) == 2);
    assert(get_concentratie(list->elems[1]) == 0.4);
    assert(get_cantitate(list->elems[1]) == 5);
    assert(strcmp(get_nume(list->elems[1]), "no") == 0);

    destroyList(list, (DestroyFunction) destroyMed);
}

void test_sort_meds()
{
    MyList* list = createList();

    Medicament* med1 = createMed(1, "hello3", 0.2, 20);
    Medicament* med2 = createMed(2, "aaa", 0.2, 25);
    Medicament* med3 = createMed(3, "zzz", 0.2, 1);
    Medicament* med4 = createMed(4, "ads",0.1,1);
    add_medicament(med1, list);
    add_medicament(med2, list);
    add_medicament(med3, list);

    MyList* res1 = sort_meds(list, (CompareFunction) compare_nume);
    MyList* res2 = sort_meds(list, (CompareFunction) compare_cantitate_cresc);
    MyList* res3 = sort_meds(list, (CompareFunction) compare_cantitate_descresc);

    assert(get_cod(res1->elems[0]) == 2);
    assert(get_cod(res1->elems[1]) == 1);
    assert(get_cod(res1->elems[2]) == 3);

    assert(get_cod(res2->elems[0]) == 3);
    assert(get_cod(res2->elems[1]) == 1);
    assert(get_cod(res2->elems[2]) == 2);

    assert(get_cod(res3->elems[0]) == 2);
    assert(get_cod(res3->elems[1]) == 1);
    assert(get_cod(res3->elems[2]) == 3);

    add_medicament(med4, list);
    MyList* res4 = sort_meds(list, (CompareFunction) compare_cantitate_concentratie);
    assert(get_cod(res4->elems[0]) == 4);
    assert(get_cod(res4->elems[1]) == 3);

    destroyList(list, (DestroyFunction) destroyMed);
    destroyList(res1, (DestroyFunction) destroyMed);
    destroyList(res2, (DestroyFunction) destroyMed);
    destroyList(res3, (DestroyFunction) destroyMed);
    destroyList(res4, (DestroyFunction) destroyMed);

}

void test_expand()
{
    MyList* list = createList();

    Medicament* med1 = createMed(1, "hello", 0.2, 20);
    Medicament* med2 = createMed(2, "aaa", 0.2, 5);
    Medicament* med3 = createMed(3, "zzz", 0.2, 1);
    add_medicament(med1, list);
    add_medicament(med2, list);
    add_medicament(med3, list);

    assert(list->capacitate == 10);


    for (int i = 0; i < 20; i++) {
        Medicament* med = createMed((i + 1) * 13, "hello", 0.2, 20);
        add_medicament(med, list);
    }

    assert(list->capacitate == 40);


    destroyList(list, (DestroyFunction) destroyMed);

}

void test_filter_meds()
{
    MyList* list = createList();

    Medicament* med1 = createMed(1, "hello2", 0.2, 20);
    Medicament* med2 = createMed(2, "aaa", 0.2, 5);
    Medicament* med3 = createMed(3, "zzz", 0.2, 1);
    add_medicament(med1, list);
    add_medicament(med2, list);
    add_medicament(med3, list);

    MyList* res1 = filter_meds(list, 2, 'a');
    MyList* res2 = filter_meds(list, 2, 'f');
    MyList* res3 = filter_meds(list, 1, 10);
    MyList* res4 = filter_meds(list, 3, 5);

    assert(res1->lungime == 1);
    assert(get_cod(res1->elems[0]) == 2);

    assert(res2->lungime == 0);

    assert(res3->lungime == 2);
    assert(get_cod(res3->elems[0]) == 2);
    assert(get_cod(res3->elems[1]) == 3);

    assert(res4->lungime == 1);
    assert(get_cod(res4->elems[0])== 1);
    destroyList(list, (DestroyFunction) destroyMed);
    destroyList(res1, (DestroyFunction) destroyMed);
    destroyList(res2, (DestroyFunction) destroyMed);
    destroyList(res3, (DestroyFunction) destroyMed);
    destroyList(res4, (DestroyFunction) destroyMed);

}

void test_undo_functions()
{
    MyList *list = createList();
    MyList *undo_list = createList();

    Medicament* med1 = createMed(1, "hello2", 0.2, 20);
    Medicament* med2 = createMed(2, "aaa", 0.2, 5);


    assert(undo_list->lungime == 0);
    assert(list->lungime == 0);

    store_current_state(list, undo_list);
    add_medicament(med1, list);
    assert(undo_list->lungime == 1);
    assert(list->lungime == 1);

    store_current_state(list, undo_list);
    add_medicament(med2, list);
    assert(undo_list->lungime == 2);
    assert(list->lungime == 2);

    list = undo(list, undo_list);
    assert(list->lungime == 1);
    assert(undo_list->lungime == 1);

    list = undo(list, undo_list);
    assert(list->lungime == 0);
    assert(undo_list->lungime == 0);

    Medicament *med3 = createMed(3, "hello2", 0.2, 20);
    Medicament *med4 = createMed(4, "hello2", 0.2, 20);

    store_current_state(list, undo_list);
    add_medicament(med3, list);
    store_current_state(list, undo_list);
    add_medicament(med4, list);

    assert(list->lungime == 2);
    assert(undo_list->lungime == 2);

    destroyList(list, (DestroyFunction) destroyMed);
    destroyList(undo_list, (DestroyFunction) destroyUndoMeds);
}

void test_all()
{
    test_create_list();
    test_create_med();
    test_expand();
    test_validate();

    test_add_medicament();
    test_delete_medicament();
    test_modify_medicament();
    test_sort_meds();
    test_filter_meds();

    test_undo_functions();
}