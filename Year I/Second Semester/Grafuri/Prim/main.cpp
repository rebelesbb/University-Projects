#include <iostream>
#include <fstream>
#include <iomanip>
int MAX = 1000;
int key[1000], Pi[1000];
bool vis[1000];
int n, adj[1000][1000];

using namespace std;

int extractMin()
{
    int max_key = MAX;
    int min = -1;
    for(int index = 0; index < n; index++)
        if(!vis[index] && key[index] < max_key)
            min = index, max_key = key[index];
    return min;
}

void prim(int r) ///r = radacina
{
    int visited = 0;
    for(int index = 0; index < n; index++)
    {
        key[index] = MAX; ///cost initial
        Pi[index] = -1;  ///parinte
    }
    key[r] = 0;

    while(visited < n - 1) {
        int u = extractMin();
        visited++;
        vis[u] = true;
        for(int v = 0; v < n; v++)
            if(!vis[v] && key[v] > adj[u][v])
            {
                Pi[v] = u;
                key[v] = adj[u][v];
            }
    }

}

int main()
{
    ifstream file4("prim.txt");

    file4 >> n;
    int i,j, cost;

    for(i = 0; i < n; i++)
        for(j = i; j < n; j++)
            if(i == j)
                adj[i][j] = 0;
            else adj[i][j] = adj[j][i] = MAX;

    while(file4 >> i >> j >> cost)
        adj[i][j] = adj[j][i] = cost;

    cout << n << '\n';
    for(i = 0; i < n; i++, cout << '\n')
        for(j = 0; j < n; j++)
            if(adj[i][j] == MAX)
                cout << setw(5) << "INF";
            else cout << setw(5) << adj[i][j];

    prim(2);

    cout<<'\n';
    for(int index = 0; index < n; index ++)
        cout << Pi[index] << ' ';

    cout<<"\n ";
    for(int index = 0; index < n; index ++)
        cout << key[index] << ' ';

    return 0;
}