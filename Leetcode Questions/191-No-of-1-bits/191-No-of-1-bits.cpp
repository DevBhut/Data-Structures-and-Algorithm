#include<iostream>
using namespace std;

int hm(int n) {
    int w = 0;
    while(n!=0) {
        w += n & 1;
        n >>= 1;
    }
    return w;
}


int main() {
    cout<<hm(356);
    return 0;
}