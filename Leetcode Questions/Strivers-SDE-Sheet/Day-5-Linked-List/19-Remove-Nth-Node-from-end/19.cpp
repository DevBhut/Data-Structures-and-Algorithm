#include<iostream>
#include<vector>
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



// Optimal approach
Node* delete_n_from_back_opti(Node* head, int n) {
    Node* slow = head;
    Node* fast = head;
    for(int i=0; i<n; i++) 
        fast = fast->next;
    if(fast == nullptr) {
        Node* temp = slow->next;
        delete slow;
        return temp;
    }
    while(fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next;
    }
    Node* temp = slow->next;
    slow->next = slow->next->next;
    delete temp;
    return head;
}


void print(Node* head) {
    Node* temp = head;
    while (temp) {
        cout<<temp->data<<" -> ";
        temp = temp->next;
    }
    cout<<"None "<<endl;
}


int main() {
    vector<int> arr1 = {2, 3, 4, 5};
    LinkedList ll;
    ll.insert_using_arr(arr1);
    Node* head = ll.insert_at_head(1);
    cout<<"Linked List: "<<endl;
    ll.print();
    Node* new_head = delete_n_from_back_opti(head, 3);
    cout<<"Linked List after deletion: "<<endl;
    print(new_head);
    return 0;    
}