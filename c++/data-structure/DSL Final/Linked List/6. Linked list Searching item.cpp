/**
 * Searching in linked list.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

typedef struct Node node;

struct Node {
    int data; 
    node *next;
};

node *createLinkedlist(node *root, int data) {
    node *newNode = new node();

    newNode->data = data;
    newNode->next = NULL;

    if(root == NULL) {
        return newNode;
    }

    root->next = newNode;

    return newNode;
}

int main() {
    node *root = NULL, *ptr = NULL;

    cout << "How many data you want to insert in your linked list: ";
    int tData = input();

    cout << "Read data: " << endl;
    for(int i = 0; i < tData; i++) {
        if(i == 0) {
            int data = input();
            root = createLinkedlist(root, data);
            ptr = root;
        } else {
            int data = input();
            ptr = createLinkedlist(ptr, data);
        }
    }

    cout << "After storing value: ";
    ptr = root;
    while(ptr != NULL) {
        cout << ptr->data << " ";
        ptr = ptr->next;
    } cout << endl;

    // seraching element
    cout << "Enter how many times you want to perform searching operation: ";
    int tSearch = input();

    cout << "Enter data one by one \n";
    for(int i = 0; i < tSearch; i++) {
        int item = input();

        ptr = root;
        bool flag = false;

        while(ptr != NULL) {
            if(ptr->data == item) {
                cout << item << " found." << endl;
                flag = true;
            }
             ptr = ptr->next;
        }
        if(!flag) {
            cout << item << " not found." << endl;
        }
    }

    return 0;
}
