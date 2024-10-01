#include<iostream>
#include<vector>
#include<unordered_set>
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



Node* find_intersection_better(Node* head1, Node* head2) {
    unordered_set<Node*> st;
    while(head1) {
        st.insert(head1);
        head1 = head1->next;
    }
    while(head2) {
        if(st.find(head2) != st.end())
            return head2;
        head2 = head2->next;
    }
    return nullptr;
}



Node* find_intersection_opti(Node* head1, Node* head2) {
    Node* temp1 = head1;
    Node* temp2 = head2;
    while (temp1 != temp2) {
        temp1 = (temp1==nullptr) ? head2 : temp1->next;
        temp2 = (temp2==nullptr) ? head1 : temp2->next;
    }
    return temp1;
}



int main() {
    Node* com = new Node(5);
    com->next = new Node(7);

    Node* x = new Node(2);
    x->next = new Node(3);
    x->next->next = com;

    // Intersecting: 
    Node* y = new Node(4);
    y->next = com;

    // // Non intersecting:
    // Node* y = new Node(4);
    // y->next = new Node(6);
    // y->next = new Node(8);

    cout<<"List1: "<<endl;
    print(x);
    cout<<"List2: "<<endl;
    print(y);

    cout<<endl;

    Node* better = find_intersection_better(x, y);
    if(better == nullptr)
        cout<<"Better: nullptr or "<<better<<endl;
    else
        cout<<"Better: "<<better->data<<endl;

    Node* opti = find_intersection_opti(x, y);
    if(opti == nullptr)
        cout<<"Opti: nullptr or "<<opti<<endl;
    else
        cout<<"Better: "<<better->data<<endl;

    return 69;  
}