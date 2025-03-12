#ifndef PARTICIPANTSFUNCIONS_H
#define PARTICIPANTSFUNCIONS_H
#include <crtdbg.h>
#include <stdbool.h>
#include "participant.h"
#include "list.h"

bool valid(ElementsList *participants, Participant new_participant, char err[5][100], int *len);

void delete_participant(ElementsList *participants, char fname[], char lname[], int score, char [5][100], int* len);

void add_participant(ElementsList *participants, char fname[], char lname[], int score, char err[5][100], int* len);

void update_participant(ElementsList *participants, int position, char new_first_name[], char new_last_name[],
                        int new_score, char err[5][100], int* len);

void filter_participants(ElementsList* participants, ElementsList *filtered_list, char key[], char value[], char err[][100], int *len);

void sort_list(ElementsList *participants, char key[], bool reversed, char e[5][100], int* len);

#endif //PARTICIPANTSFUNCIONS_H
