#include "DFS.h"

#include <iostream>
bool visitedDFS[10000]; //pot fi date ca parametrii daca nu vrem sa le facem globale
int resultDFS[10000], cntDFS;
void DFS(int n, bool** adj, int start)
{
    visitedDFS[start] = true;
    resultDFS[++cntDFS] = start;
    for(int i = 1; i <= n; i++)
        if(adj[start][i] && !visitedDFS[i])
            DFS(n, adj, i);
}

void printDFS(int n, bool** adj, int start)
{
    DFS(n, adj, start);
    std:: cout << "DFS:\n";
    for(int i = 1; i <= cntDFS; i++)
        std::cout << resultDFS[i] << ' ';
    std::cout << ' ';
}
