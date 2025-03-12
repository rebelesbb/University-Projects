#ifndef LAB2_4_PARTICIPANT_H
#include <stdbool.h>

typedef struct {
    char* first_name;
    char* last_name;
    int score;
}Participant;

Participant* create_participant(char first_name[], char last_name[], int score);

void set_first_name(Participant *participant, char name[]);

void set_score(Participant *participant, int score);

void set_last_name(Participant *participant, char name[]);

char* get_first_name(Participant *participant);

char* get_last_name(Participant *participant);

int get_score(Participant *participant);

bool equal_name(char name1[], char name2[]);

bool equal(Participant participant1, Participant participant2);

void free_participant(Participant *participant);

#define LAB2_4_PARTICIPANT_H

#endif //LAB2_4_PARTICIPANT_H
