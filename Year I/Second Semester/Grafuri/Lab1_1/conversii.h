#ifndef LAB1_CONVERSII_H
#include <stdlib.h>
struct nd{
    int node;
    struct nd *next;
};

typedef struct nd Node;


void print_menu()
{
    printf("1.Afisare matrice adiacenta\n");
    printf("2.Matrice adiacenta -> Matrice incidenta\n");
    printf("3.Matrice adiacenta -> Lista adiacenta\n");
    printf("4.Matrice incidenta -> Lista adiacenta\n");
    printf("5.Matrice incidenta -> Matrice adiacenta\n");
    printf("6.Lista adiacenta -> Matrice adiacenta\n");
    printf("7.Lista adiacenta -> Matrice incidenta\n");
    printf("8.Iesire\nIntroduceti optiunea:\n");
}

void reset_mat(int n, int m, bool mat[][m+1])
{
    int i, j;
    for(i = 1; i <= n; i++)
        for(j = 1; j <= m; j++)
            mat[i][j] = 0;
}

void print_adj_mat(int n, bool adj[][n + 1])
{
    int i,j;
    for(i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++)
            printf("%d ", adj[i][j]);
        printf("\n");
    }
    printf("\n");
}

void print_inc_mat(int n, int m, bool inc[n + 1][m + 1])
{
    int i,j;
    for(i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++)
            printf("%d ", inc[i][j]);
        printf("\n");
    }
    printf("\n");
}

void free_one(Node* head)
{
    if(head != NULL)
    {
        free_one(head->next);
        free(head);
    }
}

void print_adj_list(int n, Node* list[])
{
    Node* current;
    int i;
    for(i = 1; i <= n; i++)
    {
        printf("%d: ", i);
        current = list[i]->next;
        while(current) {
            printf("%d ", current->node);
            current = current->next;
        }
        printf("\n");
    }
    printf("\n");
}

void convert_adj_inc(int n, int m, bool adj[][n + 1], bool inc[n + 1][m + 1])
{
    int i, j, current = 1;
    for(i = 1; i <= n;i++)
        for(j = i + 1; j<=n; j++)
        {
            if(adj[i][j] == 1)
                inc[i][current] = inc[j][current] = 1, current++;
        }
}

void convert_adj_lst(int n, bool adj[][n + 1], Node* list[])
{
    int i, j;
    Node *current, *first;

    for(i = 1; i <= n; i++)
        if(list[i]!=NULL)
            free_one(list[i]);

    for(i = 1; i <= n; i++) {
        list[i] = (Node*)malloc(sizeof(Node));
        list[i]->node = i;
        list[i]->next = NULL;
    }

    for(i = n; i >= 1; i--) {
        first = NULL;
        for (j = n; j >= 1; j--) {
            if (adj[i][j] == 1) {
                current = (Node*) malloc(sizeof(Node));
                current->node = j;
                current->next = first;
                first = current;
            }
        }
        list[i]->next = first;
    }
}


#pragma clang diagnostic push
#pragma ide diagnostic ignored "MemoryLeak"
void convert_inc_lst(int n, int m, bool inc[][m+1], Node *list[])
{
    int i, x, y;
    Node *new_node;

    for(i = 1; i <= n; i++)
        if(list[i])
            free_one(list[i]);

    for(i = 1; i <= n; i++)
    {
        list[i] = (Node*) malloc(sizeof(Node));
        list[i] = NULL;
    }

    for(i = m; i >= 1; i--)
    {
        for(x = 1; x <= n; x++)
            if(inc[x][i])
                break;
        for(y = x + 1; y <= n; y++)
            if(inc[y][i])
                break;

        new_node = (Node*)malloc(sizeof(Node));
        new_node->node = y;
        new_node->next = list[x];
        list[x] = new_node;

        new_node = (Node*)malloc(sizeof(Node));
        new_node->node = x;
        new_node->next = list[y];
        list[y] = new_node;
    }

    for(i = 1; i <= n; i++) {
        new_node = (Node *)malloc(sizeof(Node));
        new_node->node = i;
        new_node->next = list[i];
        list[i] = new_node;
    }
}
#pragma clang diagnostic pop

void convert_inc_adj(int n, int m, bool adj[][n + 1], bool inc[][m + 1])
{
    int i, x, y;

    reset_mat(n,n,adj);

    for(i = 1; i <= m; i++)
    {
        for(x = 1; x <= n; x++)
            if(inc[x][i])
                break;

        for(y = x + 1; y <= n; y++)
            if(inc[y][i])
                break;

        adj[x][y] = adj[y][x] = 1;
    }
}

void convert_lst_adj(int n, bool adj[][n + 1], Node* list[])
{
    int i, j;
    reset_mat(n, n, adj);
    Node *current;

    for(i = 1; i <= n; i++)
    {
        current = list[i]->next;
        while(current)
        {
            j = current->node;
            adj[i][j] = adj[j][i] = 1;
            current = current->next;
        }
    }
}

void convert_lst_inc(int n, int m, Node* list[] ,bool inc[][m + 1])
{
    int i, j, x = 0;
    Node* current;

    reset_mat(n, m, inc);

    for(i = 1; i <= n; i++)
    {
        current = list[i]->next;
        while (current)
        {
            j = current->node;
            if(i < j)
            {
                x++;
                //printf("%d %d %d\n", i, j, x);
                inc[i][x] = inc[j][x] = 1;
            }
            current = current->next;
        }
    }

}
#define LAB1_CONVERSII_H

#endif //LAB1_CONVERSII_H
