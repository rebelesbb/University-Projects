#include "BFS.h"
#include "DFS.h"
#include <fstream>
#include <crtdbg.h>
using namespace std;

int main() {
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Parcurgeri\graf.txt)");
    int n, i, j;
    file>>n;

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

    file.close();

    bfs(n, a, 5);
    printDFS(n, a, 5);

    for(i =1 ; i <= n ;i++)
        delete[] a[i];
    delete[] a;

    _CrtDumpMemoryLeaks();

    return 0;
}
