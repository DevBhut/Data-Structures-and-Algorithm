#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    if(n <= 0)    return false;
    else    return (n & (n-1)) == 0;
}

int main() {
    cout<<"256 is a power of 2? --> "<<isPowerOfTwo(256)<<endl;
    cout<<"192 is a power of 2? --> "<<isPowerOfTwo(192)<<endl;
    return 0;
}