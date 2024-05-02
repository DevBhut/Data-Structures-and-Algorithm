#include<iostream>
using namespace std;

double pow(double x, int n) {
    double ans = 1.0;
    long long nn = n;
    if(nn < 0)     nn = nn*(-1);
    while(nn) {
        if(nn % 2 == 0){
            x = x * x;
            nn = nn / 2;
        }
        else {
            ans = ans * x;
            nn--;
        }
    }
    if(n<0)     ans = double(1.0)/double(ans);
    return ans;
}


int main(){
    cout<<pow(2, 10)<<endl;
}