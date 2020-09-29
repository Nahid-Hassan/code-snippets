/**
 * Problem: Traversing
 * Perform operation-> find max, min, average, total, and sin value.
 * 
 * Solution: simple just like array traversing. 
 * first create a linked list and store some value then perform traversing operation
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

typedef struct Node node;

struct Node {
    int data;
    node *next;
};

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

int main() {
    node *root = NULL, *ptr = NULL;
    int i = 4;
    double j = 2.5;
    cout << (i + j) << endl;

    cout << "Enter how many data you want to store in your linked list: ";
    int tData = input();

    cout << "Read data: ";

    for(int i = 0; i < tData; i++) {
        if(i == 0) {
            root = createLinkedList(root, input());
            ptr = root;
        } else {
            ptr = createLinkedList(ptr, input());
        }
    }
    cout << "You entered the value are:";
    ptr = root;

    while(ptr != NULL) {
        cout << " " << ptr->data;
        ptr = ptr->next;
    }
    cout << endl << endl;
    cout << "--------------Perform Traversing opetaion-------------" << endl;

    ptr = root;
    int mx = -1000;
    int mn = 1000;
    int total = 0;
    double avg = 0.0;

    while(ptr != NULL) {
        if(ptr->data > mx) {
            mx = ptr->data;
        } 
        if(ptr->data < mn) {
            mn = ptr->data;
        } 
        total += ptr->data;

        ptr = ptr->next;
    }
    cout << "Max = " << mx << endl;
    cout << "Min = " << mn << endl;
    cout << "Avg = " << ((double) total / tData) << endl;
    cout << "Total = " << total << endl;

    cout << "Print sin value: \n";
    
    ptr = root;
    
    while(ptr != NULL) {
        cout << sin(M_PI * ptr-> data / 180.0) << endl;
        ptr = ptr->next;
    }

    return 0;
}
