#include "MatriceAdiacenta_ListaAdiacenta.h"
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;
void  matriceAdiacenta_listaAdiacenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j;
    file>>n;

    bool a[n + 1][n + 1];

    for(i = 1; i <= n; i++)
        for(j = i; j <= n; j++)
            a[i][j] = a[j][i] = false;

    while(file >> i >> j)
        a[i][j] = a[j][i] = true; //neorientat, neponderat

    file.close();

    map<int,vector<int>> lista;

    for(i = 1; i <= n; i++)
        for(j = i + 1; j <= n; j++)
            if(a[i][j])
            {
                lista[i].push_back(j);
                lista[j].push_back(i);
            }

    for(i = 1; i <= n; i++, cout << '\n') {
        cout << i << ':';
        for (int vecin: lista[i])
            cout <<' '<< vecin;
    }

    cout << '\n';

}