#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;

const int vide = 1;
const int rempli = 2;

void rempouvider(int n, int couleurprefixe)
{

    if (n > 0)
    {
        if (couleurprefixe == rempli)
            rempouvider(n - 2, rempli);
        else if (couleurprefixe == vide)
            rempouvider(n - 1, vide);

        printf("%d\n", n);
        rempouvider(n - 1, vide);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    rempouvider(n, rempli);

    return 0;
}