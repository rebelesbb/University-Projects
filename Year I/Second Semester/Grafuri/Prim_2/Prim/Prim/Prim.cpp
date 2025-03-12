#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
using std::vector;
using std::priority_queue;

#define NIL -1
#define INF 1001
int V, E;
int count;

struct Vertex {
    int w;
    int Pi;
    Vertex(int w, int Pi) {
        this->w = w;
        this->Pi = Pi;
    }
};

struct Edge {
    int u, v, w;
    Edge(int u, int v, int w)
    {
        this->u = u;
        this->v = v;
        this->w = w;
    }
};

bool isEmpty()
{
    if (count > 0)
        return false;
    return true;
}


int extractMin(vector<Vertex> mst, bool* Q)
{
    int min = NIL, minW = INF;
    for (int i = 0; i < V; ++i)
        if (Q[i] == true) // doar daca mai este in coada
            if (mst.at(i).w < minW)
            {
                minW = mst.at(i).w;
                min = i;
            }
    Q[min] = false;

    count--;

    return min;
}

const vector<Vertex> Prim(const vector<Edge>& graph)
{
    //initializez vectorul unde vom obtine arborele minim de parcurgere
    vector<Vertex> mst;

    mst.push_back(Vertex(0, NIL));
    for (int i = 1; i < V; ++i)
        mst.push_back(Vertex(INF, NIL));

    bool* Q = new bool[V];  // folosesc in locul cozii de prioritati
    for (int i = 0; i < V; ++i)
        Q[i] = true; // initial am introduce toate nodurile in coada, deci am sa marchez pozitia corespunzatoare fiecaruia cu true
        // pe parcurs, de cate ori terminam toate verificarile/operatiile pentru un nod (adica urmeaza sa il scoatem din coada) marchez cu false

    while (!isEmpty())
    {
        int u = extractMin(mst, Q);
        for (const auto& edge : graph)
            if (edge.u == u && Q[edge.v] == true)
                if (mst.at(edge.v).w > edge.w)
                {
                    mst.at(edge.v).w = edge.w;
                    mst.at(edge.v).Pi = u;
                }
    }

    delete[] Q;

    return mst;
}


int main()
{
    std::ifstream fin("input.txt");

    vector<Edge> graph;
    fin >> V >> E;
    count = V;

    int x, y, w;

    for (int i = 0; i < E; ++i)
    {
        fin >> x >> y >> w;
        graph.push_back(Edge(x, y, w));
        graph.push_back(Edge(y, x, w));
    }

    vector<Vertex> mst = Prim(graph);

    for (int i = 1; i < V; ++i)
        std::cout << mst.at(i).Pi << ' ' << i << '\n';

    fin.close();
    return 0;
}
