#include<iostream>
#include<vector>
using namespace std;

int countStudents(vector<int>& students, vector<int>& sandwiches) {
    int circle_lovers = 0, square_lovers = 0;
    
    for(int i: students) {
        if(i==0)    
            circle_lovers++;
        else    
            square_lovers++;
    }
    
    // cout<<"Circle Lovers: "<<circle_lovers<<", Square Lovers: "<<square_lovers<<endl;

    for(int i: sandwiches) {
        if(i==0) {
            if(circle_lovers==0)
                return square_lovers;
            circle_lovers--;
        }
        else {
            if(square_lovers==0)
                return circle_lovers;
            square_lovers--;
        }
    }
    return 0;
}

int main(){
    vector<int> students = {1,1,1,0,0,1};
    vector<int> sandwiches = {1,0,0,0,1,1};
    cout<<"Students left: "<<countStudents(students, sandwiches);
    return 0;
}