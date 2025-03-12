#include <iostream>
#include <fstream>
using namespace std;
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

void printDFS(int n, bool** adj)
{
    for(int j = 1; j <= n; j++) {
        cntDFS = 0;
        if(!visitedDFS[j]) {
            cout << '\n';
            DFS(n, adj, j);
        }
        for (int i = 1; i <= cntDFS; i++) {
            cout << resultDFS[i] << ' ';
        }
    }
}

int main() {
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Prieteni\input.txt)");
    int n, m, i, j;
    file>>n>>m;

    bool** a = new bool * [n+1]; // nu ii placea ceva cand o faceam statica
    //posibil sa mearga daca e int

    for(i = 1; i <= n; i++)
        a[i] = new bool[n + 1];

    for(i = 1; i <= n; i++) {
        for (j = i; j <= n; j++)
            a[i][j] = a[j][i] = false;
    }

    while(file >> i >> j)
        a[i][j] = a[j][i] = true; //neorientat, neponderat

    printDFS(n, a);

    for(i =1 ; i <= n ;i++)
        delete[] a[i];
    delete[] a;

    return 0;
}
