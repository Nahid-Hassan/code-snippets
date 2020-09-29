#include <bits/stdc++.h>
using namespace std;

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

int sizeOfBinaryTree(node* root) {
    if(root == NULL) return 0;
    return sizeOfBinaryTree(root->left) + sizeOfBinaryTree(root->right) + 1;
}

int main() {
    node *root1 = NULL;

    root1 = insertBST(root1, 10);
    insertBST(root1, 5);
    insertBST(root1, 0);
    insertBST(root1, -4);
    insertBST(root1, 20);
    insertBST(root1, 21);
    insertBST(root1, 17);
    insertBST(root1, 7);
    insertBST(root1, 3);

    cout << sizeOfBinaryTree(root1) << endl;

    return 0;
}


