#ifndef LAB2_4_LIST_H
#define LAB2_4_LIST_H

#include <stdbool.h>
#include <crtdbg.h>
#include "participant.h"

typedef Participant Element;

typedef struct {
    Element** nr;
    int length;
    int capacity;
}ElementsList;

ElementsList create_list();

void resize(ElementsList *some_list);

void free_list(ElementsList* some_list);

int get_size(ElementsList *some_list);

int get_capacity(ElementsList *some_list);

Element * get_element(ElementsList *some_list, int index);

void store(ElementsList *list, Participant *element);

int find(ElementsList *list, Element element);

void delete(ElementsList *list, int position);

void update(ElementsList *list, Element *updated_element, int position);

#endif //LAB2_4_LIST_H
