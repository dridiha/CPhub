
#include <bits/stdc++.h>
using namespace std;

#define MAX 100000

vector<int> adj[MAX];
vector<int> res;
int nb;
int tailleT[MAX];
int visited[MAX];


int taille(int noeud)
{
    visited[noeud]=1;
  
    int s = 0;
    for (int fils : adj[noeud]){
        if (!visited[fils])
        {tailleT[fils] = taille(fils);
        s += tailleT[fils];
        }
    }
    visited[noeud]=0;
    return tailleT[noeud] = 1 + s;
}

int main(int argc, char const *argv[])
{

    cin >> nb;
    memset(tailleT, -1, sizeof(tailleT));
    memset(visited, 0, sizeof(visited));
    
    int v1, v2;
    for (int i = 0; i < nb - 1; i++)
    {
        cin >> v1 >> v2;
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }
    
    taille(0);
    for (int i = 0; i < nb; i++)
        for (int j : adj[i])
                res.push_back(min(tailleT[j], nb - tailleT[j]));
    
    cout << *max_element(res.begin(), res.end()) << '\n';

        return 0;
    
}