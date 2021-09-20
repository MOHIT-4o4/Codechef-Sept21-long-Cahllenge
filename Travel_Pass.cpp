#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int t,i,n,a,b;
    int tt=0;
    cin>>t;
    while(t--){
        cin>>n>>a>>b;
        char s[n];
        if(a<b){
            tt= a*b + a*(a+b);
        }
        else{
            tt=a*b;
        }
        cout<<s;
    }

    return 0;
}