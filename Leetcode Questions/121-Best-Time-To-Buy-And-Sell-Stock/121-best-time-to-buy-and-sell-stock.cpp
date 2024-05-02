#include<iostream>
#include<vector>
using namespace std;

int maxProfit(vector<int>& prices) {
    int max_profit = 0, min_price = INT16_MAX; 
    for(int x: prices) {
        min_price = min(x, min_price);
        max_profit = max(x - min_price, max_profit);
    }
    return max_profit;
}

int main() {
    vector<int> prices{7,1,5,3,6,4};
    cout<<maxProfit(prices);
    return 0; 
}