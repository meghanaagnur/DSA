#include <bits/stdc++.h>
using namespace std;

int main(){
    long long int n;
    cin >> n;
    long long sum= n*(n+1)/2;

    for(int i=0; i<n-1; i++){
        long long int x;
        cin >> x;
        sum -= x;
    }
    cout<<sum;
}