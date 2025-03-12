#ifndef LAB2_4_SORT_FUNCTION_H
#define LAB2_4_SORT_FUNCTION_H

#include "list.h"

typedef bool (*CompareFunction)(Element*  element1, Element* element2, bool reversed);

void sort(ElementsList* some_list, CompareFunction cmpF, bool reversed);

#endif //LAB2_4_SORT_FUNCTION_H
