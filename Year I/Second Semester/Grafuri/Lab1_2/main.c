#include <stdio.h>
#include <stdlib.h>
#define inf 1000000000

void print_menu()
{
    printf("1.Afisare matrice adiacenta\n");
    printf("2.Afisare noduri izolate\n");
    printf("3.Verificare graf regulat\n");
    printf("4.Matrice distante\n");
    printf("5.Verificare conexitate\n");
    printf("6.Iesire\n>");
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

void print_distance_matrix(int n, int distance[][n + 1])
{
    int i, j;
    for(i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++)
            if (distance[i][j] != inf)
                printf("%d ", distance[i][j]);
            else printf("%c ", (char)236);
        printf("\n");
    }
}

void print_is_regular(bool is_reg)
{
    if(is_reg)
        printf("Graful este regulat\n");
    else printf("Graful nu este regulat\n");
    printf("\n");
}

void print_is_connected(bool is_connect)
{
    if(is_connect)
        printf("Graful este conex\n");
    else printf("Graful nu este conex\n");
    printf("\n");
}

void print_isolated_vertex(int number, int* vertex_list)
{
    if(number)
        for(int i = 0; i < number; i++)
            printf("%d", vertex_list[i]);
    else printf("Nu exista noduri izolate");
    printf("\n");
}

void isolated_vertex(int n, bool adj[][n + 1], int *vertex_list, int *number)
{
    int i, j;
    *number = 0;
    for(i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++)
            if (adj[i][j])
                break;
        if(j > n)
            vertex_list[(*number)++] = i;
    }
}

bool is_regular(int n, bool adj[][n + 1])
{
    int i, j, sum, neighbours = 0;
    for(j = 1; j <= n; j++)
        neighbours += adj[1][j];

    for(i = 2; i <= n; i++) {
        sum = 0;
        for (j = 1; j <= n; j++)
            sum += adj[i][j];
        if(sum != neighbours)
            return false;
    }
    return true;
}

void dfs(int n, bool adj[][n + 1], bool visited[], int current_vertex)
{
    ///nu memorez parcurgerea efectiva/ ordinea de parcurgere
    ///ne intereseaza doar nodurile parcurse
    visited[current_vertex] = 1;
    for(int i = 1; i <= n; i++)
        if(!visited[i] && adj[i][current_vertex])
            dfs(n, adj, visited, i);

}

bool is_connected(int n, bool adj[][n + 1])
{
    bool visited[n + 1] = {};
    dfs(n, adj, visited, 1);
    for(int i = 1; i <= n; i++)
        if(!visited[i])
            return false;
    return true;
}

void distance_matrix(int n, bool adj[][n + 1], int distance[][n + 1])
{
    int i, j, k;
    for(i = 1; i <= n; i++)
        for(j = i + 1; j <=n; j++)
            if(!adj[i][j])
                distance[i][j] = distance[j][i] = inf;
            else distance[i][j] = distance[j][i] = 1;

    for(k = 1; k <= n; k++)
        for(i = 1; i <= n; i++)
            for(j = 1; j <= n; j++)
                if(distance[i][j] > distance[i][k] + distance[k][j])
                    distance[i][j] = distance[i][k] + distance[k][j];
}

int main() {
    FILE* descriptor;
    char file_name[]="C:\\Users\\Bogdan Rebeles\\Desktop\\Grafuri\\Lab1_2\\regular.txt";
    descriptor = fopen(file_name,"r");
    if(descriptor == NULL)
    {
        perror("Eroare la deschiderea fisierului");
        return 1;
    }

    int n, m = 0;

    fscanf(descriptor, "%d", &n);

    bool adj[n + 1][n + 1] = {};
    int x,y;

    while(!feof(descriptor))
    {
        m++;
        fscanf(descriptor, "%d", &x);
        fscanf(descriptor, "%d", &y);
        adj[x][y] = adj[y][x] = 1;
    }

    fclose(descriptor);

    int option;
    int *vertex_list, number, distance[n + 1][n + 1] = {};

    while(true) {
        print_menu();
        scanf("%d", &option);
        switch (option) {
            case 1:
                print_adj_mat(n, adj);
                break;
            case 2:
                vertex_list = (int*)malloc(n* sizeof(int));
                isolated_vertex(n, adj, vertex_list, &number);
                print_isolated_vertex(number, vertex_list);
                free(vertex_list);
                break;
            case 3:
                print_is_regular(is_regular(n, adj));
                break;
            case 4:
                distance_matrix(n, adj, distance);
                print_distance_matrix(n, distance);
                break;
            case 5:
                print_is_connected(is_connected(n, adj));
                break;
            case 6:
                return 0;
            default:
                printf("Optiune invalida.\n\n");
                break;
        }
    }
}
