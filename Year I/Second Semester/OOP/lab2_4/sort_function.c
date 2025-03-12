#include "sort_function.h"

/**
 * Sorts a list
 * @param some_list: the list (ElementsList)
 * @param cmpF: the compare function  (CompareFunction)
 * @param reversed: flags descending sort (bool)
 */
void sort(ElementsList* some_list, CompareFunction cmpF, bool reversed)
{
    int i,j;
    for(i = 0; i < get_size(some_list); i++)
        for(j = i + 1; j < get_size(some_list); j++){
            Element* aux;
            if(cmpF(get_element(some_list, i), get_element(some_list, j), reversed)){
                aux = some_list->nr[i];
                some_list->nr[i] = some_list->nr[j];
                some_list->nr[j] = aux;
            }
        }
}