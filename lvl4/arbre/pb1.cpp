#include<iostream>
# define N 20000

using namespace std;

int tab[N];

void printpath(int noeud, int target){

    if(noeud == 0) return;
    printpath(tab[noeud],target);
    cout<<noeud;
    if(noeud != target)
    cout<<" ";
    else cout<<"\n";

}

int main(int argc, char const *argv[])
{
    int n,r;
    cin>>n;
    for(int i=1;i<=n;++i)
      cin>>tab[i];
    cin>>r;
    while(r--)
    {
      int a;
      cin>>a;
      printpath(a,a);
    
}

return 0;
}
