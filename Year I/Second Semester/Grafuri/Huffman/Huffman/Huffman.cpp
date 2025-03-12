#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <crtdbg.h>
using std::vector;
using std::string;
using std::map;
using std::cout;

map<char, string> codes;

struct node{
	int num;
	char ch;
	node* left;
	node* right;
};

/**
 * @brief Parcurge un arbore cu noduri de tip struct node pentru a gasi caracterul cu codul ascii cel mai mic
 * @param nd : nodul de pornire, radacina
 * @param min : parametru unde se memoreza codul ascii al caracterului gasit
 */
void getMinChar(node* nd, int& min)
{
	if (!nd)
		return;

	if ((int)nd->ch < min) min = (int)nd->ch;
	
	getMinChar(nd->left, min);
	getMinChar(nd->right, min);
}

node* extractMin(vector<node*>& Q)
{
	node* min_ = Q.front();
	int index = 0;

	for (int i = 0; i < Q.size(); ++i)
		if (Q.at(i)->num < min_->num)
			min_ = Q.at(i), index = i;
		else if (Q.at(i)->num == min_->num)
		{
			int minCh1 = 300, minCh2= 300;
			getMinChar(Q.at(i), minCh1);
			getMinChar(min_, minCh2);

			if (minCh1 < minCh2)
				min_ = Q.at(i), index = i;
		}

	Q.erase(Q.begin() + index);

	return min_;
}


void initQ(map<char, int> C, vector<node*>& Q)
{
	for (const auto& elem : C)
	{
		node* newN = new node;
		newN->left = nullptr;
		newN->right = nullptr;
		newN->num = elem.second;
		newN->ch = elem.first;
		Q.push_back(newN);
	}
}

node* huffman(map<char, int> C)
{
	vector<node*> Q;
	initQ(C, Q);
	int n = C.size();
	for (int i = 1; i <= n-1; ++i)
	{
		node* z = new node;
		z->left = extractMin(Q);
		z->right = extractMin(Q);
		z->num = z->left->num + z->right->num;
		z->ch = 0;
		Q.push_back(z);
	}

	return extractMin(Q);
}

void chCodes(node* first, string str) {
	if (!first)
		return;

	if (first->ch != 0)
		codes[first->ch] = str;

	chCodes(first->left, str + "0");
	chCodes(first->right, str + "1");
}

void freeNodes(node* first)
{
	if (!first)
		return;

	node* current = first;

	freeNodes(first->left);
	freeNodes(first->right);

	delete[] current;
}
/*
void doFreq(map<char, int>& C_, int totalChr)
{
	double fr = (float)(100.0 / totalChr);
	auto it = C_.begin();
	while (it != C_.end())
	{
		int f = it->second;
		double new_fr = fr * (float)(f);
		if (new_fr - floor(new_fr) > 0.5)
			it->second = (int)ceil(new_fr);
		else it->second = (int)floor(new_fr);
		it++;
	}
}
*/

int main(int argc, char* argv[])
{
	std::ifstream fin;
	std::ofstream fout;

	/*fin.open("input.txt");
	fout.open("output.txt");*/
	fin.open(argv[1]);
	fout.open(argv[2]);

	string str;
	
	char* aux = new char[10000];
	fin.getline(aux, 10000);
	str += aux;

	while (fin.getline(aux, 10000))
	{
		if (strlen(aux) != 0)
		{
			str += "\n";
			str += aux;
		}
	}

	cout << str << '\n';

	delete[] aux;

	//cout << str;

	map<char, int> C_;
	int totalChars = str.size();

	for(int i = 0; i < str.size(); ++i)
	{
		auto it = C_.find(str.at(i));
		if (it != C_.end())
			C_[str.at(i)]++;
		else C_.insert({ str.at(i), 1 });
	}

	fout << C_.size() << '\n';

	for (const auto& elem : C_)
	{
		if (elem.first == '\n')
			fout << "\\n" << " : " << elem.second << '\n';
		else fout << elem.first << " : " << elem.second << '\n';
	}
	/*
	doFreq(C_, totalChars);

	C_['e'] += 1;
	C_['f'] -= 1;
	*/
	//cout << '\n';
	
	node* first = huffman(C_);
	
	chCodes(first, "");

	for (const auto& elem : codes)
	{
		if (elem.first == '\n')
			cout << "\\n" << " : " << elem.second << '\n';
		else cout <<elem.first << " : " << elem.second << '\n';
	}

	
	for (int i = 0; i < str.size(); ++i)
		fout << codes[str.at(i)];
	fout << '\n';

	fin.close();
	fout.close();
	
	_CrtDumpMemoryLeaks();

	return 0;
}