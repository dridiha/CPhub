//30 min nul
#include <bits/stdc++.h>
using namespace std;

#define MAX_CARTONS 20000
vector<int> contenu[MAX_CARTONS + 1];
queue<int> q;
string masque;
bool comparable(int noeud){
    string mys = to_string(noeud);
    if(mys.length()!=masque.length()) return false;
    for (u_int i=0;i<masque.length();i++)
            if(masque[i]!='?' && masque[i]!=mys[i])
                return false;
    return true;
}

void visit(){
    
    if(q.empty())return;
    
    int v = q.front();
    q.pop();
    if(comparable(v) && v!=0)
        cout<<v<<' ';
    
    for (int fils:contenu[v])
        q.push(fils);
        

    visit();
}



int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int nbCartons;
    cin>>nbCartons;
    for (int i=1;i<=nbCartons;i++)
        {
            int contenant;
            cin>>contenant;
            contenu[contenant].push_back(i);
        }
    cin>>masque;
    q.push(0);
    visit();
    return 0;
}
