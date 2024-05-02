/*
Sum of 2 integers without using the operator + and -
*/

#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int n1, n2;
    n1 = -3;
    n2 = 2;
    bitset<8> bit1(n1);
    bitset<8> bit2(n2);
    cout<<"bit1: "<<bit1<<endl;
    cout<<"bit2: "<<bit2<<endl;
    return 0;
}