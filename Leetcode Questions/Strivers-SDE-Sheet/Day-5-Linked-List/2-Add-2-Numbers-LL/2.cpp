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


void print(Node* head) {
    Node* temp = head;
    while (temp) {
        cout<<temp->data<<" -> ";
        temp = temp->next;
    }
    cout<<"None "<<endl;
}


Node* add_numbers(Node* head1, Node*head2) {
    Node* head = new Node(-1);
    Node* temp = head;
    int carry = 0;
    while ((head1 || head2) || carry) {
        int sum = 0;
        if (head1) {
            sum += head1->data;
            head1 = head1->next;
        }
        if (head2) {
            sum += head2->data;
            head2 = head2->next;
        }
        if (carry) {
            sum += carry;
        }
        carry = sum / 10;
        temp->next = new Node(sum%10);
        temp = temp->next;
    }
    return head->next;
}


int main() {
    vector<int> arr1 = {4, 3}, arr2 = {6, 8, 9};
    LinkedList ll1, ll2;
    ll1.insert_using_arr(arr1);
    ll2.insert_using_arr(arr2);
    Node* head1 = ll1.insert_at_head(2);
    Node* head2 = ll2.insert_at_head(5);
    cout<<"Linked List1: "<<endl;
    ll1.print();
    cout<<"Linked List2: "<<endl;
    ll2.print();
    Node* head = add_numbers(head1, head2);
    cout<<"Linked List after addition: "<<endl;
    print(head);
    return 0;
}
