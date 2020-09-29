/**
 * Deleting an element from sorted linked list.
 * solution: 1st create a sorted linked list. then search element you want to delete and delete them.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

typedef struct Node node;

struct Node {
    int data;
    node *next;
};

node *start = NULL, *ptr = NULL;
node *ctrl = NULL;
node *another_ctrl = NULL;

node *createLinkedList(node *root, int data) {
    node *newNode = new node();

    newNode->data = data;
    newNode->next = NULL;

    if(root == NULL) {
        return newNode;
    }

    root->next = newNode;

    return newNode;
}

void display(node *root) {
    while(root != NULL) {
        cout << root->data << " ";
        root = root->next;
    } cout << endl;
}

int deleteNode() {
    cout << "Enter the data you want to delete: ";
    int item = input();

    ctrl = start;
    bool flag = false;

    while(ctrl != NULL) {
        if(ctrl->data == item) {
            another_ctrl = ctrl;
            flag = true;
            break;
        }
        ptr = ctrl;
        ctrl = ctrl->next;
    }
    if(!flag) {
        cout << "Data not found." << endl;
    } else {
        if(ctrl == start) {
            start = ctrl->next;
        } else if (ctrl == NULL) {
            ptr->next = NULL;
        } else {
            ptr->next = another_ctrl->next;
        }
        cout << "After delete item " << item << " now linked list contains: ";
        display(start);
    }
}

int main() {
    cout << "Enter how many element you want insert: ";
    int tData = input();

    cout << "Read assending order sorted input(): ";
    for(int i = 0; i < tData; i++) {
        if(i == 0) {
            start = createLinkedList(start, input());
            ptr = start;
        } else {
            ptr = createLinkedList(ptr, input());
        }
    }

    cout << "Now linked list contains: ";
    display(start);

    cout << "How many items you want to delete: ";
    int dData = input();

    cout << "Read data: ";
    for(int i = 0; i < dData; i++) {
        deleteNode();
    }
}
