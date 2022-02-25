// pb2_treelength
//30 min nul
#include <bits/stdc++.h>
using namespace std;

#define MAX_CARTONS 100000
list<int> filsde[MAX_CARTONS + 1];

void visit(list<int>& racine){
    for (auto fils:racine)
        {cout<<'A'<<' '<<fils<<'\n';
        visit(filsde[fils]);
        cout<<'R'<<' '<<fils<<'\n';
        }
    return;
}



int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int nbCartons;
    cin>>nbCartons;
    int nbInscriptions;
    for (int i=0;i<=nbCartons;i++)
        {
            cin>>nbInscriptions;
            for (int j=0;j<nbInscriptions;j++)
                {
                    int ident;
                    cin>>ident;
                    filsde[i].push_back(ident);

                }

        }
    visit(filsde[0]);
    return 0;
}
