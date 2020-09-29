/**
 * Sort the content of linked list.
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
    }
    cout << endl;
}

void sortLinkedlist(node *root) {
    if(root == NULL) {
        cout << "Empty linked list." << endl;
    } else {
        node *firstLoop, *secondLoop;
        
        firstLoop = root;
      
        while(firstLoop != NULL) {
            secondLoop = firstLoop->next;
            while(secondLoop != NULL) {
                if(firstLoop->data > secondLoop->data) {
                    int temp = firstLoop->data;
                    firstLoop->data = secondLoop->data;
                    secondLoop->data = temp;
                }
                secondLoop = secondLoop->next;
            }
            firstLoop = firstLoop->next;
        }
    }
}

int main() {
    cout << "How many data you want to store in your linked list: ";
    int tData = input();

    cout << "Read data(Given random order): ";
    for(int i = 0; i < tData; i++) {
        if(i == 0) {
            start = createLinkedList(start, input());
            ptr = start;
        } else {
            ptr = createLinkedList(ptr, input());
        }
    }
    cout << "Before sorting: ";
    display(start);

    sortLinkedlist(start);

    cout << "After sorting: ";
    display(start);
}
