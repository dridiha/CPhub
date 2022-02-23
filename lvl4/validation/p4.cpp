#include<bits/stdc++.h>
using namespace std;
const int MAX_NB_SEGMENTS = 100 * 1000;

int rangDebFinInd[MAX_NB_SEGMENTS], rangFinDebInd[MAX_NB_SEGMENTS];
int main(int argc, char const *argv[])
{

    int N;
    int x,y;
    cin>>N;
    vector<pair<pair<int,int>,int>>intervalle;
    for (int i=0;i<N;i++){
        cin>>x>>y;
        intervalle.push_back(make_pair(make_pair(x,y),i));
    }
//indice = intervalle[i].second

     sort(begin(intervalle), 
         end(intervalle), 
         [](pair<pair<int,int>,int> a, pair<pair<int,int>,int> b) {
             if (a.first.first!=b.first.first) return a.first.first<b.first.first;
             else return a.first.second>b.first.second; });
       
    for(auto segment:intervalle)
        rangDebFinInd[] = ; 

    sort(begin(intervalle), 
         end(intervalle), 
         [](pair<int,int> a, pair<int,int> b) {
             if (a.second!=b.second) return a.second>b.second;
             else return a.first<b.first; });

    return 0;
}
