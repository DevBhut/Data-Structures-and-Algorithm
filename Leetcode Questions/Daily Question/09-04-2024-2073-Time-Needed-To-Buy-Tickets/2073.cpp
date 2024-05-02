#include<iostream>
#include<vector>
using namespace std;

int timeReqToBuy(vector<int>& tickets, int k) {
    int time = 0;
    for(int i=0; i<tickets.size(); i++)
        time += min((tickets[k] - (i>k)), tickets[i]);
    return time;
}

int main() {
    vector<int> tickets = {2, 7, 5, 5, 5, 3};
    cout<<timeReqToBuy(tickets, 3);
    return 0;
}