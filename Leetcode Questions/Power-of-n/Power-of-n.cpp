#include <iostream>
#include <cmath>
using namespace std;

bool isPowOfMath(int n, int b) {
    if(n<=0 || b<=0)    return false;
    else {
        float result = log(n) / log(b);
        return abs(result - round(result)) < 1e-9; 
    }
}


int main() {
    cout<<"Is 81 a power of 3? --> "<< isPowOfMath(81, 3)<< endl;
    cout<<"Is 123 a power of 3? --> "<< isPowOfMath(123, 3)<< endl;
}