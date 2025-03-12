#include "Undo.h"
#include <stdlib.h>

/**
 * Stores the current state of a list
 * @param list: the list (MyList*)
 * @param undo_list: the lists that stores all previous
 *                   states of a list (MyList*)
 */
void store_current_state(MyList* list, MyList* undo_list)
{
    MyList* current_state = createList();
    copyElems(list, current_state, (CopyFunction) copyMed);
    store(undo_list, current_state);
}

/**
 * Returns the previous state of a list
 * @param list: the list              (MyList*)
 * @param undo_list: the lists that stores all previous
 *                   states of a list (MyList*)
 * @return the previous state of a list (MyList*)
 */
MyList* undo(MyList* list, MyList* undo_list)
{
    destroyList(list, (DestroyFunction) destroyMed);

    undo_list->lungime--;

    return undo_list->elems[undo_list->lungime];
}

/**
 * Destroys a list that contains lists of meds
 * @param meds_list: a list of meds
 */
void destroyUndoMeds(MyList* meds_list)
{
    ///we basically just need to delete a list of meds within the undo list
    destroyList(meds_list, (DestroyFunction) destroyMed);
}
