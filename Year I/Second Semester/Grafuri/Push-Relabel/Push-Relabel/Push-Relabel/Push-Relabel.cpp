#include <iostream>
#include <fstream>
#include <vector>
using std::vector;

struct Edge {
	int flow, capacity;
	int u, v;
	Edge(int flow, int capacity, int u, int v)
	{
		this->flow = flow;
		this->capacity = capacity;
		this->u = u;
		this->v = v;
	}
};

struct Vertex {
	int h, eFlow;

	Vertex(int h, int eFlow)
	{
		this->h = h;
		this->eFlow = eFlow;
	}
};

struct Graph {
	vector<Edge> edge;
	vector<Vertex> vertex;
};

void preflow(Graph& g, int source)
{
	g.vertex[source].h = (int)g.vertex.size();

	for (int i = 0; i < g.edge.size(); ++i)
	{
		// daca arcul porneste din sursa
		if (g.edge[i].u == source)
		{
			g.edge[i].flow = g.edge[i].capacity;
			// initializam excesul de flux
			g.vertex[g.edge[i].v].eFlow += g.edge[i].flow;

			// adaugam arc de la v la s in graful rezidual
			// cu capacitatea egala cu 0
			g.edge.push_back(Edge(-(g.edge[i].flow), 0, g.edge[i].v, source));
		}
	}

}

int overFlowVertex(vector<Vertex>& vertex)
{
	for (int i = 1; i < vertex.size() - 1; i++)
		if (vertex[i].eFlow > 0)
			// returnam indexul varfului cu exces de flux
			return i;

	// daca nu gasim niciun varf
	return -1;
}

void updateReverseEdgeFlow(Graph& g, int i, int flow)
{
	int u = g.edge[i].v, v = g.edge[i].u;
	for (int j = 0; j < g.edge.size(); ++j)
	{
		if (g.edge[j].v == v && g.edge[j].u == u)
		{
			g.edge[j].flow -= flow;
			return;
		}
	}

	//adaugam la graful rezidual
	g.edge.push_back(Edge(0, flow, u, v));
}

// pompare
bool push(Graph& g, int u)
{
	// parcurgem varfurile adiacente lui u, la care acesta poate pompa flux
	for (int i = 0; i < g.edge.size(); ++i)
	{
		if (g.edge[i].u == u)
		{
			// daca nu putem pompa flux la acest varf
			if (g.edge[i].flow == g.edge[i].capacity)
				continue;


			if (g.vertex[u].h > g.vertex[g.edge[i].v].h)
			{
				// putem pompa min { cantitatea disponibila de flux care poate fi pompata la nod, excesul de flux}
				int flow = std::min(g.edge[i].capacity - g.edge[i].flow, g.vertex[u].eFlow);

				// se reduce excesul de flux
				g.vertex[u].eFlow -= flow;

				// crestem excesul pentru nodul adiacent
				g.vertex[g.edge[i].v].eFlow += flow;

				// adaugam flux rezidual
				g.edge[i].flow += flow;
				updateReverseEdgeFlow(g, i, flow);

				return true;
			}
		}
	}
	return false;
}

// inaltare
void relabel(Graph& g, int u)
{
	int minH = INT_MAX; // inaltimea minima a vf adj
	for (int i = 0; i < g.edge.size(); ++i)
	{
		if (g.edge[i].u == u)
		{
			// daca flux = capacitate nu se face inaltare
			if (g.edge[i].flow == g.edge[i].capacity)
				continue;

			if (g.vertex[g.edge[i].v].h < minH)
			{
				minH = g.vertex[g.edge[i].v].h;

				// crestem inaltimea lui u
				g.vertex[u].h = minH + 1;
			}
		}
	}
}

int pushRelabel(Graph g, int source, int dest)
{
	preflow(g, source);

	//int overFlowV;

	while (overFlowVertex(g.vertex) != -1)
	{
		//std::cout << "i\n";
		int u = overFlowVertex(g.vertex);
		if (!push(g, u))
			relabel(g, u);
	}

	return g.vertex.back().eFlow;
}


int main(int argc, char* argv[])
{

	if (argc != 3)
	{
		std::cout << "Numar insuficient de argumente\n";
		exit(EXIT_FAILURE);
	}
	std::ifstream fin;
	std::ofstream fout;

	fin.open(argv[1]);
	if (fin.fail())
	{
		perror("ifstream::open()");
		exit(EXIT_FAILURE);
	}
	fout.open(argv[2]);

	int n, m;
	Graph graph;

	int u, v, c;

	fin >> n >> m;
	for (int i = 0; i < n; ++i)
		graph.vertex.push_back(Vertex(0,0));

	for (int i = 0; i < m; ++i)
	{
		fin >> u >> v >> c;
		graph.edge.push_back(Edge(0, c, u, v));
	}
/*
	for (int i = 0; i < m; ++i)
	{
		std::cout << graph.edge.at(i).u << ' ' << graph.edge.at(i).v << '\n';
	}
*/
	int source = 0, dest = n - 1;

	fout << pushRelabel(graph, source, dest);

	fin.close();
	fout.close();

	return 0;
}