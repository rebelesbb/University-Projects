#include "ListaAdiacenta_MatriceAdiacenta.h"
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;

void listaAdiacenta_matriceAdiacenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j;
    file>>n;

    map<int, vector<int>> lista;
    bool a[n + 1][n + 1];

    for(i = 1; i <= n; i++)
        for(j = i; j <= n; j++)
            a[i][j] = a[j][i] = false;

    while(file >> i >> j) {
        lista[i].push_back(j);
        lista[j].push_back(i);
    }

    file.close();

    for(i = 1; i <= n; i++)
        for(int vecin: lista[i])
            if(vecin > i)
                a[i][vecin] = a[vecin][i] = true;

    for(i = 1; i <= n; i++, cout << '\n')
        for(j = 1; j <= n; j++)
            cout << a[i][j] << ' ';
    cout << '\n';
}