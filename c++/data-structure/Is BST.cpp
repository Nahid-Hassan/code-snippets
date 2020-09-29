#include <bits/stdc++.h>
using namespace std;

int mn = numeric_limits<int>::min();
int mx = numeric_limits<int>::max();

typedef struct Node node;
struct Node {
    int data;
    node *left;
    node *right;
};

node* insertBST(node* root, int data) {
    node *newNode = new node();
    newNode->data = data;
    newNode->left = newNode->right = NULL;

    if(root == NULL) {
        return newNode;
    }

    node *parent = NULL, *current = root;
    while(current != NULL) {
        parent = current;

        if(parent->data <= data) {
            current = current->right;
        } else {
            current = current->left;
        }
    }

    if(parent->data <= data) {
        parent->right = newNode;
    } else {
        parent->left = newNode;
    }

    return root;
}

bool isBST(node* root, int mn, int mx) {
    if(root == NULL) return true;
    if(root->data <= mn || root->data > mx) return false;

    return isBST(root->left, mn, root->data) && isBST(root->right, root->data, mx);
}

int main() {
    node *root = NULL;

    root = insertBST(root, 10);
    insertBST(root, 5);
    insertBST(root, 0);
    insertBST(root, -4);
    insertBST(root, 20);
    insertBST(root, 21);
    insertBST(root, 17);
    insertBST(root, 7);
    insertBST(root, 3);

    if(isBST(root, mn, mx)) {
        cout << "Yes!!! This is Binary Search Tree.\n";
    } else cout << "No!!! This is Binary Tree.\n";
}
