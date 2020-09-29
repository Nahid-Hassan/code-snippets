#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

int mn = numeric_limits<int>::max();
int mx = numeric_limits<int>::min();

typedef struct Node node;
struct Node {
    int data;
    node *next;
};

node* createLinkedList(node* root, int data) {
    node* newNode = new node();

    if(newNode == NULL) {
        cout << "Error!!!\n";
    }

    newNode->data = data;
    newNode->next = NULL;

    if(root == NULL) {
        return newNode;
    }

    node* currentNode = root;
    while(currentNode->next != NULL) {
        currentNode = currentNode->next;
    }

    currentNode->next = newNode;

    return root;
}

int processLinkedList(node* root) {
    int total = 0;
    while(root != NULL) {
        if(root->data > mx) {
            mx = root->data;
        }
        if(root->data < mn) {
            mn = root->data;
        }
        total += root->data;
        root = root->next;
    }

    return total;
}

int main() {
    cout << "How many element you want to append a linked list: ";
    int dataSet = input();

    node *root = NULL, *start = NULL;
    for(int i = 1; i <= dataSet; i++){
        int data = input();
        root = createLinkedList(root, data);
    }

    cout << "\nAll element you append in your linked list:";
    start = root;
    while(start != NULL) {
        cout << " " << start->data;
        start = start->next;
    } cout << endl;

    cout << "\nFind min, max, average, total Value\n";

    start = root;
    int total = processLinkedList(start);
    cout << "Min: " << mn << endl;
    cout << "Max: " << mx << endl;
    cout << "Total: " << total << endl;
    cout << "Average: " << ((double)total / dataSet) << endl;

    cout << "\nPrint Sin Value: ";
    start = root;
    while(start != NULL) {
        cout << "sin(" << start->data <<") degree: " << sin(M_PI*start->data/180.0) <<endl;
        start = start->next;
    }

    return 0;
}
