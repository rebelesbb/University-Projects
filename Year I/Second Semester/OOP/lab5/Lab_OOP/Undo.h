#ifndef UNTITLED_UNDO_H
#define UNTITLED_UNDO_H
#include "List.h"

void store_current_state(MyList* list, MyList* undo_list);

MyList* undo(MyList* list, MyList* undo_list);

void destroyUndoMeds(MyList* meds_list);

#endif //UNTITLED_UNDO_H
