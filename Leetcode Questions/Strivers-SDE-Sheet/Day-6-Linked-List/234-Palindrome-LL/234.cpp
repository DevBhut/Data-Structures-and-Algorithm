#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;

struct Node {
    int data;
    Node* next;

    Node(int d): data(d), next(nullptr) {}
};


class LinkedList {

public:
    // Using Initializer List
    LinkedList(): head(nullptr), tail(nullptr) {}

    // // The above line can be achieved using a construtor as:
    // LinkedList() {
    //     head = nullptr;
    //     tail = nullptr;
    // }

    Node* insert_at_head(int data) {
        Node* temp = new Node(data);
        if (head == nullptr) {
            head = temp;
            tail = temp;
        }
        else {
            temp->next = head;
            head = temp;
        }
        return head;
    }


    Node* insert_at_tail(int data) {
        Node* temp = new Node(data);
        if (head == nullptr) {
            head = temp;
            tail = temp;
        }
        else {
            tail->next = temp;
            tail = temp;
        }
        return tail;
    }


    void insert_using_arr(vector<int> &arr) {
        if (arr.empty())
            return;
        for(int data: arr)
            insert_at_tail(data);
        return;
    }


    Node* find(int data) {
        Node* temp = head;
        int index = 0;
        while(temp) {
            if (temp->data == data) {
                cout<<data<<" found at index "<<index<<"."<<endl;
                return temp;
            }
            temp = temp->next;
            index++;
        }
        cout<<data<<" not found in linked list."<<endl;
        return nullptr;
    }


    void delete_node(int data) {
        Node* temp = head;
        if(temp && temp->data == data) {
            head = temp->next;
            delete temp;
            return;
        }
        Node* prev = nullptr;
        while (temp && temp->data != data) {
            prev = temp;
            temp = temp->next;
        }
        if (temp == nullptr) {
            cout<<data<<" not found in linked list."<<endl;
            return;
        }
        prev->next = temp->next;
        if (temp == tail)
            tail = prev;
        delete temp;
        cout<<data<<" deleted from linked list."<<endl;
        return;
    }


    int get_length() {
        int len = 0;
        Node* temp = head;
        while (temp) {
            temp = temp->next;
            len++;
        }
        return len;
    } 


    void print() {
        Node* temp = head;
        while (temp) {
            cout<<temp->data<<" -> ";
            temp = temp->next;
        }
        cout<<"None "<<endl;
    }


private:
    Node* head;
    Node* tail;
};


void print(Node* head) {
    Node* temp = head;
    while (temp) {
        cout<<temp->data<<" -> ";
        temp = temp->next;
    }
    cout<<"None "<<endl;
}



// Brute Force
bool ll_palindrome_brute(Node* head) {
    if(head == NULL || head->next == NULL)
        return true;
    
    vector<int> st;
    Node* temp = head;

    while(temp) {
        st.push_back(temp->data);
        temp = temp->next;
    }

    temp = head;
    while(temp) {
        if(temp->data != st.back()) 
            return false;
        st.pop_back();
        temp = temp->next;
    }
    return true;
}



// Optimal Solution
Node* reverse_ll(Node* head) {
    Node* prev = nullptr;
    Node* temp = head;
    while(temp) {
        Node* front = temp->next;
        temp->next = prev;
        prev = temp;
        temp = front;
    }
    return prev;
}


bool ll_palindrome_opti(Node* head) {
    if(head == NULL || head->next == NULL)
        return true;
    
    Node* temp = head;
    Node* slow = temp;
    Node* fast = temp;

    while(fast->next && fast->next->next) {
        fast = fast->next->next;
        slow = slow->next;
    }
    Node* new_head = slow->next;

    Node* head1 = head;
    Node* head2 = reverse_ll(slow->next);

    while(head1 && head2) {
        if( head1->data != head2->data) {
            reverse_ll(new_head);
            return false;
        }
        head1 = head1->next;
        head2 = head2->next;
    }
    reverse_ll(new_head);
    return true;
}



int main() {
    // vector<int> arr = {5, 4, 3, 2, 1};
    // LinkedList ll;
    // ll.insert_using_arr(arr);
    // Node* head = ll.insert_at_head(1);
    // ll.print();
    // cout<<endl;

    // Node* new_head = reverse_linked_list(head);
    // print(new_head);


    LinkedList ll1;
    vector<int> arr1 = {2, 2, 1};
    ll1.insert_using_arr(arr1);
    Node* h1 = ll1.insert_at_head(1);

    LinkedList ll2;
    vector<int> arr2 = {2, 3, 2, 1};
    ll2.insert_using_arr(arr2);
    Node* h2 = ll2.insert_at_head(1);

    LinkedList ll3;
    vector<int> arr3 = {2, 3, 3, 2, 1, 0};
    ll3.insert_using_arr(arr3);
    Node* h3 = ll3.insert_at_head(1);


    cout<<"Brute: "<<endl;
    printf("LL1: %d. LL2: %d. LL3: %d. \n", ll_palindrome_brute(h1), ll_palindrome_brute(h2), ll_palindrome_brute(h3));
    printf("Opti: \n");
    printf("LL1: %d. LL2: %d. LL3: %d. ", ll_palindrome_opti(h1), ll_palindrome_opti(h2), ll_palindrome_opti(h3));

    return 0;    

}