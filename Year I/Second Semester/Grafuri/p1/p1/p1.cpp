#include <iostream>
#include <fstream>
#include <climits>
using namespace std;

int minCosts[100], parent[100];
bool selected[100];
int max_ = 1000;

void print_path(int dest)
{
    if (dest != 0)
        print_path(parent[dest]);
    cout << dest << ' ';
}

void dijkstra(int start, int n, int graph[][100])
{
    int min;
    int i, j, k;
    for (i = 0; i < n; i++)
    {
        minCosts[i] = graph[start][i];
        if (i != start && minCosts[i] != max_)
            parent[i] = start;
    }
    selected[start] = true;

    for (k = 1; k < n; ++k)
    {
        min = max_;
        for (i = 0; i < n; i++)
            if (!selected[i] && minCosts[i] < min)   ///extract min
            {
                min = minCosts[i];
                j = i;
            }

        for (i = 0; i < n; i++)
            if (!selected[i])
                if (minCosts[i] > minCosts[j] + graph[j][i])
                {
                    minCosts[i] = minCosts[j] + graph[j][i];
                    parent[i] = j;
                }

        selected[j] = true;
    }

}

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    //ifstream fin("file.txt");
    //ofstream fout("file_out.txt");

    int n, m, source;

    fin >> n >> m >> source;

    int costs[100][100] = {};

    int x, y, w;

    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            costs[i][j] = costs[j][i] = max_;

    while (fin >> x >> y >> w)
    {
        costs[x][y] = w;
    }


    dijkstra(0, n, costs);

    for (int index = 0; index < n; index++)
        if (minCosts[index] != max_)
            fout << minCosts[index] << ' ';
        else fout << "INF" << " ";
    fout << '\n';

    //print_path(4);

    fin.close();
    fout.close();
}