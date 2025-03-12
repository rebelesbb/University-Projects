#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include "participants_functions.h"
#include "sort_function.h"
#include "participant.h"
#include "list.h"

///error messages
char* duplicate_participant_error()
{
    return "Participantul exista deja in lista.";
}

char* invalid_score_error()
{
    return "Scorul este invalid.";
}

char* invalid_fname_error()
{
    return "Prenumele trebuie sa contina doar litere.";
}
char* invalid_lname_error()
{
    return "Numele trebuie sa contina doar litere.";
}

char* participant_not_found_error()
{
    return "Participantul nu exista in lista.\n";
}

char* invalid_sort_key_error()
{
    return "Criteriu de sortare invalid. (Criterii valide: nume/scor)\n";
}

char* invalid_filter_key_error()
{
    return "Criteriu de filtrare invalid. (Criterii valide: scor/initiala)\n";
}

char* invalid_char_error()
{
    return "Valoarea introdusa nu este un caracter valid. (Caractere valide: A-Z)\n";
}

char* empty_list_error()
{
    return "Lista de participanti este goala.";
}

///validator

/**
 * Validates a participant while collecting the errors.
 * @param participants: a list of participants (ElementsList)
 * @param participant: a participant (Participant)
 * @param err: a list of errors (char**)
 * @param len: the length of the list of errors (int)
 * @return true if the participant hasn't been added to the list yet
 *                 the first and last name of the participant contain only letters
 *                  the score is between 0 and 100
 *          false otherwise
 *        : (bool)
 */
bool valid(ElementsList *participants, Participant new_participant, char err[5][100], int *len)
{
    (*len) = 0;
    for(int p = 0; p < participants->length ; p++)
        if(equal(*participants->nr[p], new_participant)) {
            strcpy(err[*len], duplicate_participant_error());
            (*len)++;
            break;
        }

    if(get_score(&new_participant) < 0 || get_score(&new_participant) > 100) {
        strcpy(err[*len],invalid_score_error());
        (*len)++;
    }

    char* first_name = get_first_name(&new_participant);
    for(int l = 0; l < strlen(first_name); l++)
        if(isalpha(first_name[l]) == 0)
        {
            strcpy(err[*len],invalid_fname_error());
            (*len)++;
            break;
        }

    char* last_name = get_last_name(&new_participant);
    for(int l = 0; l < strlen(last_name); l++)
        if(isalpha(last_name[l]) == 0)
        {
            strcpy(err[*len],invalid_lname_error());
            (*len)++;
            break;
        }

    if(*len)
        return false;
    return true;
}

///service functions

/**
 * Compares the last name of two participants
 * @param participant1: a participant (Participant)
 * @param participant2: a participant (Participant)
 * @param reversed: used in case of descending sort (bool)
 * @return the result of the comparison, based on reversed
 */
bool cmpLastName(Participant* participant1, Participant* participant2, bool reversed)
{
    bool result;
    if (strcmp(get_last_name(participant1), get_last_name(participant2)) > 0)
        result = true;
    else result = false;
    if(reversed)
        return !result;
    else return result;
}

/**
 * Compares the score of two participants
 * @param participant1: a participant (Participant)
 * @param participant2: a participant (Participant)
 * @param reversed: used in case of descending sort (bool)
 * @return the result of the comparison, based on reversed
 */
bool cmpScore(Participant* participant1, Participant* participant2, bool reversed)
{
    bool result;
    if (get_score(participant1) > get_score(participant2))
        result = true;
    else result = false;
    if(reversed)
        return !result;
    else return result;
}

/**
 * Checks if a participant's data meets certain criteria
 * @param key: the criteria: score/initial of last name (char*)
 * @param value: the value of the key (char*)
 * @return based on the key and its value, true if
 *      - score < value
 *      - initial == value
 *      : (bool)
 */
bool filter_key(Participant *participant, char key[], char value[])
{
    if(strcmp(key, "scor") == 0) {
        int score_key = atoi(value);
        if(get_score(participant) < score_key)
            return true;
        return false;
    }
    else{ /// key == initial
        value = strupr(value);
        if(get_last_name(participant)[0] == value[0])
            return true;
        return false;
    }
}

/**
 * Adds a valid participant to the list of participants
 * @param participants: the list of participants (ElementsList)
 * @param first_name: the first name of the participant to be deleted (char*)
 * @param last_name: the last name of the participant to be deleted (char*)
 * @param score: the score of the participant to be deleted (char*)
 * @param err: a list of errors (char**)
 * @param len: the length of the list of errors
 */
void add_participant(ElementsList *participants, char first_name[], char last_name[], int score , char err[5][100], int *len)
{
    Participant *new_participant;
    new_participant = create_participant(first_name, last_name, score);

    if(valid(participants,*new_participant, err, len))
        store(participants, new_participant);
    else free_participant(new_participant);
}

/**
 * Deletes a participant previously added in the list of participants
 * participants: the list of participants (ElementsList)
 * @param first_name: the first name of the participant to be deleted (char*)
 * @param last_name: the last name of the participant to be deleted (char*)
 * @param score: the score of the participant to be deleted (char*)
 * @param err: a list of errors (char**)
 * @param len: the length of the list of errors
 */
void delete_participant(ElementsList *participants, char first_name[], char last_name[], int score, char err[5][100], int* len)
{
    Participant *participant = create_participant(first_name, last_name, score);
    int index = find(participants, *participant);
    free_participant(participant);

    if(get_size(participants) == 0)  // if the list is empty
    {
        strcpy(err[*len], empty_list_error());
        (*len)++;
    }
    else if(index == -1){  // if the participant can't be found
        strcpy(err[*len],participant_not_found_error());
        (*len)++;
    }
    else
        delete(participants,index);
}

/**
 * Updates a participant previously added in the list, only if the
 * updated data is valid
 * @param participants: the list of participants  (ElementsList)
 * @param position: the position of the participant in the list (int)
 * @param new_first_name: updated first name (char*)
 * @param new_last_name: updated last name   (char*)
 * @param new_score: updated score (int)
 * @param err: a list of errors (char**)
 * @param len: the length of the error list (int)
 */
void update_participant(ElementsList *participants, int position,
                        char new_first_name[], char new_last_name[], int new_score, char err[5][100], int *len)
{
    if(!get_size(participants)) // if the list is empty
    {
        strcpy(err[*len], empty_list_error());
        (*len)++;
    }
    else {
        Participant *participant, *updated_participant;
        participant = get_element(participants, position);
        char first_name[50], last_name[50];
        int score;

        ///checks which data needs to be updated
        if (strcmp(new_first_name, "-1") == 0)
            strcpy(first_name, get_first_name(participant));
        else strcpy(first_name, new_first_name);

        if (strcmp(new_last_name, "-1") == 0)
            strcpy(last_name, get_last_name(participant));
        else strcpy(last_name, new_last_name);

        if (new_score == -1)
            score = get_score(participant);
        else score = new_score;

        updated_participant = create_participant(first_name, last_name, score);

        if (!equal(*updated_participant, *participant)) {
            if (valid(participants, *updated_participant, err, len)) {
                update(participants, updated_participant, position);
            } else free_participant(updated_participant);
        } else free_participant(updated_participant);
    }
}

/**
 * Sorts the list of participants based on key (name/score)
 * ascending or descending
 * !!Modifies the list
 * @param participants: the list of participants (ElementsList)
 * @param key: the sorting key: name/score (char*)
 * @param reversed: if true, the list is sorted descending (bool)
 * @param err: a list of errors (char**)
 * @param len: the length of the list od errors (int)
 */
void sort_list(ElementsList *participants, char key[], bool reversed, char err[5][100], int* len)
{
    if(!get_size(participants)) // if the list is empty
    {
        strcpy(err[*len], empty_list_error());
        (*len)++;
    }
    else if (!(strcmp(key,"nume") == 0 || strcmp(key, "scor") == 0)) { // if the key isn't valid
        strcpy(err[*len], invalid_sort_key_error());
        (*len)++;
    }
    else{
        if(strcmp(key, "nume") == 0)
            sort(participants, cmpLastName, reversed);
        else sort(participants, cmpScore, reversed);
    }

}

/**
 * Filters a list of participants, returning a list of the participants that meet certain criteria
 * !!Doesn't modify the list
 * @param participants: a list of participants (ElementsList)
 * @param filtered_list: the list of filtered participants (ElementsList)
 * @param key: the criterion (char*)
 * @param value: the key's value (char*)
 * @param err: a list of errors (char*)
 * @param len: the length of the error list (int*)
 */
void filter_participants(ElementsList* participants, ElementsList *filtered_list, char key[], char value[], char err[][100], int *len)
{

    if(!get_size(participants)) // if the list is empty
    {
        strcpy(err[*len], empty_list_error());
        (*len)++;
    }
    else if(strcmp(key,"scor") == 0 || strcmp(key,"initiala") == 0) {
         if(strcmp(key, "scor") == 0 && (atoi(value) < 0 || atoi(value) > 100)) // if the score isn't valid
         {
             strcpy(err[*len], invalid_score_error());
             (*len)++;
         } else if(strcmp(key, "initiala") == 0 && !isalpha(value[0])) // if the initial isn't valid
         {
             strcpy(err[*len], invalid_char_error());
             (*len)++;
         }
        else {
             for (int index = 0; index < get_size(participants); index++)
                 if (filter_key(get_element(participants, index), key, value)) {

                     Participant *participant_copy, *participant = get_element(participants, index);

                     participant_copy = create_participant(get_first_name(participant),
                                                           get_last_name(participant),
                                                           get_score(participant));

                     store(filtered_list, participant_copy);
                 }
         }
     }
     else // if the key isn't valid
     {
         strcpy(err[*len], invalid_filter_key_error());
         (*len)++;
     }
}