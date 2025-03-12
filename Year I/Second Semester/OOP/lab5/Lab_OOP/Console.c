#include "Console.h"
#include <stdio.h>
#include "Medicament.h"
#include "List.h"
#include "Undo.h"
#include <crtdbg.h>

void print_list(MyList* list) {
    /*
     * Printeaza medicamentele din lista data
     */
     printf("\n");
     if(!list->lungime)
         printf("Lista este goala!\n");
     else {
         for (int i = 0; i < list->lungime; i++)
             printf("cod:%d, nume:%s, concentratie:%lf, cantitate:%d\n", get_cod(list->elems[i]),
                    get_nume(list->elems[i]), get_concentratie(list->elems[i]), get_cantitate(list->elems[i]));
     }
     printf("\n");
}

void print_menu() {
    /*
     * Printeaza meniul principal
     */
    printf("0. Print\n");
    printf("1. Add\n");
    printf("2. Modify\n");
    printf("3. Delete\n");
    printf("4. View sorted\n");
    printf("5. Filter\n");
    printf("6. Undo\n");
    printf("7. Exit\n");

}

void run() {
/*
 * Programul principal
 */
 MyList* list = createList();
 MyList* undo_list = createList();
 int option = 0;

 while (1) {

     print_menu();

     printf("Option: ");
     scanf_s("%d", &option);

     if (option == 0)
     {
         print_list(list);
     }
     else if (option == 1) {
         int cod, cantitate;
         double concentratie;
         char nume[50];

         printf("Cod:");
         scanf_s("%d", &cod);

         printf("Nume:");
         scanf_s("%s", nume, 50);

         printf("Concentratie:");
         scanf_s("%lf", &concentratie);

         printf("Cantiate:");
         scanf_s("%d", &cantitate);

         Medicament* med = createMed(cod, nume, concentratie, cantitate);

         if (validateMed(med) == 0) {
             store_current_state(list, undo_list);
             add_medicament(med, list);
         }
         else {
             printf("Date invalide\n\n");
             destroyMed(med);
         }

     }
     else if (option == 2) {

         int cod = 0;
         printf("Cod:");
         scanf_s("%d", &cod);


         double concentratie;
         char nume[50];

         printf("Nume:");
         scanf_s("%s", nume, 50);

         printf("Concentratie:");
         scanf_s("%lf", &concentratie);

         store_current_state(list, undo_list);
         modify_medicament(cod, concentratie, nume, list);
     }
     else if (option == 3) {
         int cod = 0;
         printf("Cod:");
         scanf_s("%d", &cod);

         store_current_state(list, undo_list);
         delete_medicament(cod, list);
     }
     else if (option == 4) {
         printf("\n1. Dupa Nume\n");
         printf("2. Dupa Cantitate(crescator)\n");
         printf("3. Dupa Cantitate(descrescator)\n");
         printf("4. Dupa cantitate si concentratie, crescator\n");
         printf("Option: ");
         int opt = 0;
         scanf_s("%d", &opt);

         printf("Sortat: ");
         MyList* res;

         if (opt == 1) {
             res = sort_meds(list, (CompareFunction) compare_nume);
         }
         else if (opt == 2) {
             res = sort_meds(list, (CompareFunction) compare_cantitate_cresc);
         }
         else if (opt == 3){
             res = sort_meds(list, (CompareFunction) compare_cantitate_descresc);

         }
         else{
             res = sort_meds(list, (CompareFunction) compare_cantitate_concentratie);
         }

         print_list(res);
         destroyList(res, (DestroyFunction) destroyMed);

     }
     else if (option == 5) {
         printf("\n1. Cantitate mai mica \n");
         printf("2. Incepe cu litera data\n3. Cantitate mai mare\n");
         printf("Option: ");
         int opt = 0;
         scanf_s("%d", &opt);
         char some;
         scanf_s("%c", &some, 1);

         MyList* res = NULL;

         if (opt == 1) {
             int a = 0;
             printf("Cantitate: ");
             scanf_s("%d", &a);

             res = filter_meds(list, opt, a);
         }
         else if(opt == 2){
             char a = ' '; //??
             printf("Litera: ");
             scanf_s("%c", &a, 1);

             res = filter_meds(list, opt, a);
         } else if(opt == 3)
         {
             int a = 0;
             printf("Cantitate: ");
             scanf_s("%d", &a);

             res = filter_meds(list, opt, a);
         } else printf("%s", "Optiune invalida");

        if(res) {
            printf("Filtrat: ");
            print_list(res);
            destroyList(res, (DestroyFunction) destroyMed);
        }
     }
     else if (option == 6) {
         if(undo_list->lungime) {
             //destroyList(list, (DestroyFunction) destroyMed);
             //list = undo_list->elems[undo_list->lungime - 1];
             //undo_list->lungime--;
             list = undo(list, undo_list);  ///????
             printf("Undo realizat cu succes.\n");
         } else printf("Nu se poate realiza undo.\n");
     }
     else if(option == 7){
         destroyList(list, (DestroyFunction) destroyMed);
         /*for(int index = 0; index < undo_list->lungime; index++) {
             destroyList(undo_list->elems[index], (DestroyFunction) destroyMed);
         }
         free(undo_list);*/
         destroyList(undo_list, (DestroyFunction) destroyUndoMeds);
         _CrtDumpMemoryLeaks();
         break;
     }
     else {
         printf("Invalid option\n");
     }
     //print_list(undo_list->elems[undo_list->lungime - 1]);
     //print_list(list);
 }
}