#include <stdio.h>
#include "conversii.h"

int main() {

    int n, m=0, option;
    FILE *descriptor;
    char file_name[]= "C:/Users/Bogdan Rebeles/Desktop/Grafuri/Lab1_1/in.txt"; //????
    descriptor = fopen(file_name,"r+");

    if (descriptor == NULL) {
        printf("Eroare la deschiderea fisierului.\n");
        return 1; // Ieșire din program cu cod de eroare
    }

    fscanf(descriptor, "%d", &n);

    bool adj[n + 1][n + 1] = {};
    Node *list[n + 1];
    int x,y;

    for(x = 1; x <= n; x++)
        list[x] = NULL;


    while(!feof(descriptor))
    {
        m++;
        fscanf(descriptor, "%d", &x);
        fscanf(descriptor, "%d", &y);
        adj[x][y] = adj[y][x] = 1;
    }

    bool inc[n + 1][m + 1]= {};

    fclose(descriptor);

    convert_adj_inc(n, m, adj, inc);
    convert_adj_lst(n, adj, list);

    print_menu();

    while(true)
    {

        //printf(">");
        scanf("%d", &option);
        switch (option) {
            case 1:
                print_adj_mat(n, adj);
                break;
            case 2:
                convert_adj_inc(n, m, adj, inc);
                print_inc_mat(n, m, inc);
                break;
            case 3:
                convert_adj_lst(n, adj, list);
                print_adj_list(n, list);
                break;
            case 4:
                convert_inc_lst(n, m, inc, list);
                print_adj_list(n, list);
                break;
            case 5:
                convert_inc_adj(n, m, adj, inc);
                print_adj_mat(n, adj);
                break;
            case 6:
                convert_lst_adj(n, adj, list);
                print_adj_mat(n, adj);
                break;
            case 7:
                convert_lst_inc(n, m, list, inc);
                print_inc_mat(n, m, inc);
                break;
            case 8:
                for(int i = 1; i <= n; i++)
                    if(list[i]!=NULL)
                        free_one(list[i]);
                return 0;
            default:
                printf("Optiune invalida.\n\n");
                break;
        }
    }

}

