#include "participant.h"
#include "string.h"
#include "stdlib.h"

/**
 * Creates a participant
 * @param first_name: participant's first name  (char*)
 * @param last_name: participant's last name    (char*)
 * @param score: participant's score            (char*)
 * @return the created participant (Participant)
 */
Participant* create_participant(char first_name[], char last_name[], int score)
{
    Participant* new_participant = (Participant*)malloc(sizeof(Participant));

    new_participant->last_name = (char*) malloc((1 + strlen(last_name))*sizeof(char));
    new_participant->first_name = (char*) malloc((1 + strlen(first_name))*sizeof(char));

    set_last_name(new_participant, last_name);
    set_first_name(new_participant, first_name);
    set_score(new_participant,score);

    return new_participant;
}

void set_first_name(Participant *participant, char name[])
{
    ///in case the new name has a greater length than the current first_name
    if((strlen(name) + 1) * sizeof(char) > (strlen(participant->first_name) + 1) * sizeof(char))
        participant->first_name = (char*) realloc(participant->first_name, (strlen(name) + 1) * sizeof(char));
    strcpy(participant->first_name, name);

}

void set_last_name(Participant *participant, char name[])
{
    ///in case the new name has a greater length than the current last_name
    if((strlen(name) + 1) * sizeof(char) > (strlen(participant->last_name) + 1) * sizeof(char))
        participant->last_name = (char*) realloc(participant->last_name, (strlen(name) + 1) * sizeof(char));
    strcpy(participant->last_name,name);
}

void set_score(Participant *participant, int score)
{
    participant->score = score;
}

char* get_first_name(Participant *participant)
{
    return participant->first_name;
}

char* get_last_name(Participant *participant)
{
    return participant->last_name;
}

int get_score(Participant *participant)
{
    return participant->score;
}

/**
 * Checks if two names are equal
 * @name1: a name (char*)
 * @name2: a name (char*)
 * @return true if the two names are equal
 *         false otherwise
 */
bool equal_name(char name1[], char name2[])
{
    if(strcmp(name1,name2) == 0)
        return true;
    return false;
}

/**
 * Checks if two participants are equal
 * @param participant1: a participant (Participant)
 * @param participant2: a participant (Participant)
 * @return true if the two participants have:
 *            -the same first name
 *            -the same last name
 *            -the same score
 *         false otherwise
 */
bool equal(Participant participant1, Participant participant2)
{
    if(equal_name(get_first_name(&participant1), get_first_name(&participant2))
       && equal_name(get_last_name(&participant1), get_last_name(&participant2))
       && get_score(&participant2) == get_score(&participant1))
        return true;
    return false;
}

void free_participant(Participant *participant)
{
    free(participant->first_name);
    free(participant->last_name);
    free(participant);
}
