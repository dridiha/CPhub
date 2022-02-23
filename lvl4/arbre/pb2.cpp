// pb2_treelength

#include <bits/stdc++.h>
using namespace std;

#define N 20000
int tab[N];
int lengths[N];
int length(int noeud)
{

    if (noeud == 0)
        return 0;
    if (lengths[noeud]!=-1)
        return lengths[noeud];
    return lengths[noeud]=length(tab[noeud])+1;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    memset(lengths, -1, sizeof(lengths));
    for (int i = 1; i <= n; ++i)
        cin >> tab[i];

    int maxi = -1;
    for (int i = 1; i <= n; ++i)
        maxi = max(maxi, length(i));

    cout << maxi << endl;
    return 0;
}
