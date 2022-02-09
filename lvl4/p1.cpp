#include <bits/stdc++.h>
using namespace std;
int m, n;
int lengths[350][350];

int dp(int i, int j, vector<vector<int>> &G)
{
    if (lengths[i][j] != -1)
        return lengths[i][j];
    if (G[i][j])
        return lengths[i][j] = 0;
    if (i == n - 1 || j == m - 1)
        return lengths[i][j] = 1;
    return lengths[i][j] = 1 + min({dp(i + 1, j, G), dp(i + 1, j + 1, G), dp(i, j + 1, G)});
}

int main(int argc, char const *argv[])
{

    memset(lengths, -1, sizeof(lengths));
    cin >> n >> m;
    vector<vector<int>> G(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> G[i][j];

    int max = -1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            if (lengths[i][j] == -1)
                lengths[i][j] = dp(i, j, G);

            if (lengths[i][j] > max)
                max = lengths[i][j];
        }

    cout << max;

    return 0;
}
