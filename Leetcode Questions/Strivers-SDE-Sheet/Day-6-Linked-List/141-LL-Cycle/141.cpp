#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

struct Node {
    int data;
    Node* next;

    Node(int d): data(d), next(nullptr) {}
};



bool has_cycle_brute(Node* head) {
    unordered_set<Node*> st;
    while (head) {
        if (st.find(head) != st.end())
            return true;
        st.insert(head);
        head = head->next;
    }
    return false;
}


bool has_cycle_opti(Node* head) {
    Node* slow = head;
    Node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return true;
    }
    return false;
}


int main() {
    return 69;
}