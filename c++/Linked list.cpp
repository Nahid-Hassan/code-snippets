#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}
typedef struct Node node;
struct Node {
    int data;
    node* next;
};

node* createLinkedList(node* root, int data) {
    node* newNode = new node();

    newNode->data = data;
    newNode->next = NULL;

    if(root == NULL) return newNode;

    root->next = newNode;
    return newNode;
}

int main() {
    node* root = NULL, *ptr = NULL;

    cout << "Enter how many items you want to insert: ";
    int dataSet = input();

    for(int i = 1; i <= dataSet; i++) {
        if(i==1) {
            int data = input();
            root = createLinkedList(root, data);
            ptr = root;
        } else {
            int data = input();
            ptr = createLinkedList(ptr, data);
        }
    }
    ptr = root;
    cout << "Show all the element you inserted:";
    while(ptr != NULL) {
        cout << " " << ptr->data ;
        ptr = ptr->next;
    }

    return 0;
}
