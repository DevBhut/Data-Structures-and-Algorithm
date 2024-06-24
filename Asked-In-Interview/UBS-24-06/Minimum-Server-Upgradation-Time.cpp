#include<iostream>
using namespace std;

int min_upgrade_time(int t1, int req1, int t2, int req2) {
    int time = 1;
    t1--;
    while (true) {
        time++;
        if(time%req1 !=0 && t1>0)
            t1--;
        else if(time%req2 != 0 && t2>0)
            t2--;
        if (t1==0 && t2==0)
            break;
    }
    return time;
}


int main() {
    int time = min_upgrade_time(3, 2, 1, 3);
    cout<<time;
    return 0;
}