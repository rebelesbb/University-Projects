#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
using std::map;
using std::vector;
using std::cout;
std::ifstream fin;
std::ofstream fout;

struct Graph {
	int V, E;
	map<int, vector<int>> adj;
};

void removeEdge(Graph& g, int u, int v)
{
	/*
	for (auto& i : g.adj[u])
		if (i == v)
		{
			i = -1;
			break;
		}

	for (auto& i : g.adj[v])
		if (i == u)
		{
			i = -1;
			break;
		}
		*/
	auto iv = std::find(g.adj[u].begin(), g.adj[u].end(), v);
	*iv = -1;

	auto iu = std::find(g.adj[v].begin(), g.adj[v].end(), u);
	*iu = -1;
}

// numara nodurile adiacente/muchiile accesibile din u
int DFSCount(Graph& g, int u, bool* visited)
{
	visited[u] = true;
	int count = 1;

	for (const auto& i : g.adj[u])
		if (i != -1 && !visited[i])
			count += DFSCount(g, i, visited);

	return count;
}

bool isValidNextE(Graph g, int u, int v)
{
	// verificam daca v este singurul nod adiacent lui u
	int cnt = 0;
	for (const auto& i : g.adj[u])
		if (i != -1)
		{
			cnt++;
			if (cnt == 2)
				break;
		}
	if (cnt == 1) return true; // daca este singurul, atunci muchia este valida

	// daca avem mai multe noduri adiacente
	// verificam daca muchia este sau nu punte

	//numaram nodurile accesibile din u (vf adiacente)

	bool* visited = new bool[g.V];
	for (int i = 0; i < g.V; ++i)
		visited[i] = false;
	int cntAccesible1 = DFSCount(g, u, visited);

	// eliminam muchia
	removeEdge(g, u, v);

	// numaram din nou
	for (int i = 0; i < g.V; ++i)
		visited[i] = false;
	int cntAccesible2 = DFSCount(g, u, visited);


	// adaugam inapoi muchia
	g.adj[u].push_back(v);
	g.adj[v].push_back(u);

	delete[] visited;

	// daca numarul obtinut la prima numarare e mai mare decat al doilea => e punte
	if (cntAccesible1 > cntAccesible2)
		return false;

	return true;
}


void printNextE(Graph& g, int u)
{
	for (const auto& v : g.adj[u])
	{
		int x = v;
		// daca muchia u-v nu a fost eliminata si daca este o muchie valida
		if (x != -1 && isValidNextE(g, u, x))
		{
			fout << x << ' ';
			removeEdge(g, u, x);
			printNextE(g, x);
		}
	}
}


void eulerCircuit(Graph g)
{
	int u = 0, cnt = 0;
	for (int i = 0; i < g.V; i++)
		if (g.adj[i].size() & 1) {
			cnt++;
			if (cnt > 2) break;
		}
	// daca sunt mai mult de doua muchii de grad impar => graful nu e eulerian
	if (cnt > 2)
	{
		fout << "Graful nu este eulerian\n";
		return;
	}

	for (int i = 0; i < g.V; i++)
		if (g.adj[i].size() & 1) {
			u = i;
			break;
		}

	// Incepem de la una din muchiile de grad impar
	//fout << u;

	printNextE(g, u);
}



int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "Numar invalid de argumente";
		exit(EXIT_FAILURE);
	}

	fin.open(argv[1]);
	if (fin.fail())
	{
		perror("ifstream::open()");
		exit(EXIT_FAILURE);
	}
	fout.open(argv[2]);

	Graph graph;

	fin >> graph.V >> graph.E;

	int u, v;
	for (int i = 0; i < graph.E; ++i)
	{
		fin >> u >> v;
		graph.adj[u].push_back(v);
		graph.adj[v].push_back(u);
	}
	/*
	for (int i = 0; i < graph.V; ++i)
	{
		cout << i << " : ";
		for (const auto& el : graph.adj[i])
			cout << el << ' ';
		cout << '\n';
	}
	*/
	eulerCircuit(graph);

	fin.close();
	fout.close();

	return 0;
}
