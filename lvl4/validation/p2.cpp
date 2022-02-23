#include <bits/stdc++.h>
using namespace std;


int fact[12] = {0};

int facto(int n) {
   if (fact[n]) return fact[n];
   
      fact[0] = 1;
      for (int i = 1; i <= n; ++i) {
         fact[i] = i * fact[i - 1];
      }
      return fact[n];
   
}

int main(int argc, char const *argv[])
{
    int nbPetitsPois;
    cin>>nbPetitsPois;

   //biggest fact less than nbPetitsPois
   int p = 1;
   while(facto(p)<nbPetitsPois){
       p++;
   }
   if (facto(p)>nbPetitsPois)
    p--;
   int bigf = p;
   cout<<p<<'\n';
   int res[p+1];
   memset(res,0,sizeof(res));
    while(p>0){
    while(nbPetitsPois-facto(p)>=0)
    {
        res[p]++;
        nbPetitsPois-=facto(p);
    }
    p--;
    }
    for (int i=1;i<=bigf;i++)
    cout<<res[i]<<" ";



    return 0;
}

