/**
 * Inserting data in sorted linked list.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

typedef struct Node node;

struct Node {
    int data;
    node *next;
};

node *start = NULL, *temp = NULL, *ptr = NULL, *ctrl = NULL, *anotherTemp = NULL;

node* insertNode(int data) {
    node *newNode = new node();

    newNode->data = data;
    newNode->next = NULL;

    if(start == NULL) {
        return newNode;
    } else {
        ctrl = start;
        while(ctrl != NULL) {
            if(ctrl->data >= data) {
                temp = ctrl;
                break;
            }
            ptr = ctrl;
            cout << ptr->data << endl;
            ctrl = ctrl->next;
        }
    }

    if(ctrl == start) {
        newNode->next = start;
        start = newNode;
        return newNode;
    } else if (ptr->next == NULL) {
        ptr->next = newNode;
        return start;
    } else {
        ptr->next = newNode;
        newNode->next = temp;
        return start;
    }
}

int main() {
    cout << "Enter how many data you want to insert in sorted linked list: ";
    int tData = input();

    cout << "Read data: ";
    for(int i = 0; i < tData; i++) {
        int item = input();

        start = insertNode(item);
        
        anotherTemp = start;

        cout << "After inserting data in sorting linked list: ";
        while(anotherTemp != NULL) {
            cout << anotherTemp->data << " ";
            anotherTemp = anotherTemp->next;
        } cout << endl;
    }

    cout << endl;
}
