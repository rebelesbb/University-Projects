///In cazul celorlalte reprezentari singura chestie care difera e ca nu mai
///face dubla atribuire

#include "GOrientat_MatriceIncidenta.h"
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void orientatMatriceIncidenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf_orientat.txt)");
    int n, i, j, m = 0;
    file>>n;

    int inc[n + 1][10000];

    for(i = 1; i <= n; i++)
        for(j = 1; j < 10000; j++)
            inc[i][j]  = 0;

    while(file >> i >> j)
    {
        m++;
        inc[i][m] = 1;
        inc[j][m] = -1;
    }

    file.close();

    for(i = 1; i <= n; i++, cout << '\n')
        for(j = 1; j <=m; j++)
            cout << setw(4) << inc[i][j];
    cout << '\n';
}