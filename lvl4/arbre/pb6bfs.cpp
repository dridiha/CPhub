
#include <bits/stdc++.h>
using namespace std;

#define MAX 100000

vector<int> adj[MAX];
vector<int> res;
int nb;
int tailleT[MAX];

void bfs(queue<int> &q)
{

    if (q.empty())
        return;

    int v = q.front();
    q.pop();

    for (int fils : adj[v])
    {
        if (fils != -1)
        {
            for (u_int i = 0; i < adj[fils].size(); i++)
                if (adj[fils][i] == v)
                    adj[fils][i] = -1;

            q.push(fils);
        }
    }
    bfs(q);
}

void maketree(int noeud)
{

    queue<int> q;
    q.push(noeud);
    bfs(q);
}

int taille(int noeud)
{
    if (noeud == -1)
        return 0;
    int s = 0;
    for (int fils : adj[noeud])
        s += taille(fils);
    return tailleT[noeud] = 1 + s;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> nb;
    memset(tailleT, -1, sizeof(tailleT));
    int v1, v2;
    for (int i = 0; i < nb - 1; i++)
    {
        cin >> v1 >> v2;
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }

    maketree(0);
    taille(0);
    for (int i = 0; i < nb; i++)
    {
        for (int j : adj[i])
            if (j != -1)
            {

                res.push_back(min(tailleT[j], nb - tailleT[j]));
            }
        cout << *max_element(res.begin(), res.end()) << '\n';

        return 0;
    }
