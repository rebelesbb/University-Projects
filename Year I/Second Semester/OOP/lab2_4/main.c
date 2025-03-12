#include <stdio.h>
#include "participants_functions.h"
#include "participants_tests.h"
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#include <stdbool.h>
#include <string.h>

void print_menu()
{
    printf("1.%s\n2.%s\n3.%s\n4.%s\n5.%s\n6.%s\n7.%s\n","Afisare lista participanti","Adaugare participant",
           "Stergere participant", "Actualizare date participant", "Filtrare lista",
           "Sortare lista", "Iesire");
}

/**
 * Prints the error messages.
 */
void print_errors(char err[5][100], int len)
{
    for(int l = 0; l < len; l++)
        printf("%s\n", err[l]);
}

/**
 * Prints a participant
 */
void print_participant(Participant* participant, int position)
{
    printf("%d. %s %s | %d\n", position, get_last_name(participant), get_first_name(participant),
           get_score(participant));
}

/**
 * Prints the list of participants
 */
void print_participants_list(ElementsList participants)
{
    if(get_size(&participants) > 0)
        for(int index = 0; index < get_size(&participants); index ++)
            print_participant(get_element(&participants, index), index + 1);
            //printf("%s %s | %d\n", get_first_name(&participants.nr[index]), participants.nr[index].last_name, participants.nr[index].score);
    else printf("Nu exita participanti.\n");
}

void add_participant_ui(ElementsList *participants)
{
    char first_name[30], last_name[30], err[5][100];
    int score, len = 0;

    printf("Introduceti numele:");
    scanf("%s", last_name);

    printf("Introduceti prenumele:");
    scanf("%s", first_name);

    printf("%s", "Introduceti scorul:");
    scanf("%d", &score);

    add_participant(participants, first_name, last_name, score, err, &len);
    if(len)
        print_errors(err, len);
}

void delete_participant_ui(ElementsList *participants)
{
    char first_name[30], last_name[30], err[5][100];
    int score, len = 0;

    printf("Introduceti numele:");
    scanf("%s", last_name);

    printf("Introduceti prenumele:");
    scanf("%s", first_name);

    printf("%s", "Introduceti scorul:");
    scanf("%d", &score);

    delete_participant(participants, first_name, last_name, score, err, &len);
    if(len)
        print_errors(err, len);
}

void update_participant_ui(ElementsList *participants)
{
    char err[5][100];
    int len = 0, position;

    print_participants_list(*participants);

    printf("Introduceti numarul participantului");
    scanf("%d", &position);

    char new_first_name[30], new_last_name[30];
    int new_score;

    printf("Introduceti datele noi sau '-1' daca nu doriti modificarea.\n");
    printf("Introduceti numele nou:");
    scanf("%s", new_last_name);

    printf("Introduceti prenumele nou:");
    scanf("%s", new_first_name);

    printf("%s", "Introduceti scorul nou:");
    scanf("%d", &new_score);

    update_participant(participants, position - 1, new_first_name, new_last_name, new_score, err, &len);
    if(len)
        print_errors(err, len);
}

void sort_list_ui(ElementsList *participants)
{
    char key[10], reversed[3], err[5][100];
    int len = 0;

    printf("Introduceti criteriul de sortare (nume/scor):\n>");
    scanf("%s", key);
    printf("Efectuare sortare\n0.Crescatoare     1.Descrescatoare\n>");
    scanf("%s", reversed);

    if(reversed[0] == '0')
        sort_list(participants, key, false, err, &len);
    else sort_list(participants, key, true, err, &len);

    if(len)
        print_errors(err, len);
    else print_participants_list(*participants);
}

void filter_participants_ui(ElementsList *participants)
{
    char key[10], err[5][100], value[4] ="\n";
    int len = 0;
    ElementsList filtered_list = create_list();

    printf("Introduceti criteriul de filtrare (scor/initiala):\n>");
    scanf("%s", key);

    if(strcmp(key,"scor") == 0)
        printf("Introduceti scorul:");
    else if(strcmp(key, "initiala") == 0)
        printf("Introduceti initiala:");

    scanf("%s", value);

    filter_participants(participants, &filtered_list, key, value, err, &len);

    if(len)
        print_errors(err, len);
    else
    {
        if(strcmp(key, "scor") == 0)
        {
            if(get_size(&filtered_list)) {

                printf("%s%d%s\n", "Participantii cu scorul mai mic decat ", atoi(value), " sunt:");
                print_participants_list(filtered_list);

            } else printf("%s%d\n", "Nu exista participanti cu scorul mai mic decat ", atoi(value));
        }
        else if(strcmp(key, "initiala") == 0)
        {
            if(get_size(&filtered_list)){

                printf("%s%s%s\n", "Participantii a caror nume are initiala ", value, " sunt:");
                print_participants_list(filtered_list);

            } else printf("%s%s\n", "Nu exista participanti a caror nume are initiala ", value);
        }
    }
    free_list(&filtered_list);
}

int run()
{
    ElementsList participants = create_list();

    int option;
    while(true)
    {
        print_menu();
        printf("Introduceti optiunea:");
        scanf("%d", &option);
        switch (option) {
            case 1:
                print_participants_list(participants);
                break;
            case 2:
                add_participant_ui(&participants);
                break;
            case 3:
                delete_participant_ui(&participants);
                break;
            case 4:
                update_participant_ui(&participants);
                break;
            case 5:
                filter_participants_ui(&participants);
                break;
            case 6:
                sort_list_ui(&participants);
                break;
            case 7:
                free_list(&participants);
                _CrtDumpMemoryLeaks();
                return 0;
            default:
                printf("Optiune invalida.\n");
                break;
        }
        printf("\n");
    }
}

int main() {

    test_functions();
    _CrtDumpMemoryLeaks();

    run();

    return 0;
}
