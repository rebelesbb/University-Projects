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
string decodedMessage;


struct node {
	int num;
	char ch;
	node* left;
	node* right;
};

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
			int minCh1 = 300, minCh2 = 300;
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
	int n = (int)C.size();
	for (int i = 1; i <= n - 1; ++i)
	{
		node* z = new node;
		z->left = extractMin(Q);
		z->right = extractMin(Q);
		z->num = z->left->num + z->right->num;
		z->ch = '#';
		Q.push_back(z);
	}

	return extractMin(Q);
}

void chCodes(node* first, string str) {
	if (!first)
		return;

	if (first->ch != '#')
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

char getCharFromCode(const string& code)
{
	for (const auto& elem : codes)
		if (code == elem.second)
			return elem.first;
	return '\0';
}

void decodeHuffman(const string& huffCode)
{
	int x = 0, y = 0;
	while (x < huffCode.size())
	{
		y = 1;
		while (y < huffCode.size() - x + 1)
		{
			string subCode = huffCode.substr(x, y);
			char chr = getCharFromCode(subCode);
			if (chr != '\0')
			{
				decodedMessage += chr; 
				break;
			}
			y++;
		}
		x = x + y;
	}
}


int main(int argc, char* argv[])
{
	std::ifstream fin;
	std::ofstream fout;

	//fin.open("input.txt");
	//fout.open("output.txt");
	
	fin.open(argv[1]);
	fout.open(argv[2]);

	int n, num;
	char ch;
	map<char, int> C;

	fin >> n;

	for (int i = 0; i < n; ++i)
	{
		fin >> ch >> num;
		C.insert({ ch, num });
	}

	char* s = new char[10000];

	fin.get();
	fin.getline(s, 10000);

	string str = s;
	//cout << s << '\n';

	delete[] s;

	//cout << n;
	//cout << str << '\n';

	chCodes(huffman(C),"");
	/*
	for (const auto& elem : codes)
	{
		cout << elem.first << " : " << elem.second << '\n';
	}
	*/
	decodeHuffman(str);
	fout << decodedMessage << '\n';

	fin.close();
	fout.close();

	return 0;
}