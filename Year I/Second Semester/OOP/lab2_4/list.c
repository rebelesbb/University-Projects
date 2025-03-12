#include "participant.h"
#include "sort_function.h"
#include "participants_functions.h"
#include <ctype.h>
#include <string.h>
#include "list.h"
#include "stdlib.h"


/**
 * Creates an empty list of participants.
 * @return the list (ElementsList)
 */
ElementsList create_list()
{
    ElementsList new_list;
    new_list.capacity = 10;
    new_list.nr = (Element **)malloc(new_list.capacity * sizeof(Element *));
    new_list.length = 0;
    return new_list;
}

/**
 * Extends the capacity of a list.
 * @param some_list: the list of elements (ElementsList)
 */
void resize(ElementsList *some_list)
{
    some_list->capacity = 2 * some_list->capacity;
    int new_capacity = some_list->capacity;
    some_list->nr = (Element **)realloc(some_list->nr, sizeof(Element *) * new_capacity);
}

/**
 * Frees the memory allocated for a list.
 * @param some_list: the list of elements (ElementsList)
 */
void free_list(ElementsList* some_list)
{
    int index;
    for(index = 0; index < some_list->length; index++) {
        free_participant(some_list->nr[index]);
    }
    free(some_list->nr);
}

int get_size(ElementsList *some_list)
{
    return some_list->length;
}

int get_capacity(ElementsList *some_list)
{
    return some_list->capacity;
}

Element * get_element(ElementsList *some_list, int index)
{
    return some_list->nr[index];
}


/**
 * Stores an element in the list
 * @param list: the list of participants (ElementsList)
 * @param element: the participant that we want to store (Element)
 */
void store(ElementsList *list, Participant* element)
{
    if(list->length == list->capacity)
        resize(list);
    list->nr[list->length] = element;
    list->length++;
}

/**
 * Finds if an element exists in a list.
 * @param list: the list of elements (ElementsList)
 * @param element: the element we search for (Element)
 * @return if the participant is in the list
 *            -> the position of the participant in the list
 *         else ->  -1
 *       : (int)
 */
int find(ElementsList *list, Element element)
{
    int len = get_size(list);

    for(int index = 0; index < len; index++)
        if(equal(*get_element(list, index), element))
            return index;

    return -1;
}

/**
 * Deletes an element from the list.
 * @param list: the list of elements (ElementsList)
 * @param position: the position of the element in the list (int)
 */
void delete(ElementsList *list, int position)
{
    int index, len = get_size(list);
    free_participant(get_element(list, position));
    for(index = position; index < len - 1; index++)
        list->nr[index] = list->nr[index + 1];
    list->length--;
}

/**
 * Updates an element from the list.
 * @param list: the list of elements (ElementsList)
 * @param participant: the element we want to update (Element)
 * @param position: the position of the element in the list (int)
 */
void update(ElementsList *list, Element *updated_element, int position)
{
    free_participant(list->nr[position]);
    list->nr[position] = updated_element;
}