#include<iostream>
#include<vector>
using namespace std;

struct Node {
    int data;
    Node* next;

    // Initializer List to initialize the member `variables` of the Node struct.
    Node(int d): data(d), next(nullptr) {}

    // // The above line can also be written as:
    // // Here we assign the member variables `data` and `next` value inside the constuctor body
    // Node(int d) {
    //     data = d;
    //     next = nullptr;
    // }
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



int main() {
    LinkedList ll;
    cout<<"Linked List initialized."<<endl;
    ll.insert_at_head(1);
    ll.insert_at_head(2);
    ll.insert_at_head(3);
    ll.print();
    ll.insert_at_tail(2);
    ll.insert_at_tail(3);
    ll.print();
    vector<int> arr = {4, 5, 6};
    ll.insert_using_arr(arr);
    ll.print();
    ll.find(5);
    ll.find(7);
    ll.delete_node(5);
    ll.print();
    ll.delete_node(5);
    std::cout << "Length: " << ll.get_length() << std::endl;
    return 0;
}