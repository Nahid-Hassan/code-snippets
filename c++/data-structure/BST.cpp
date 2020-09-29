//nahid.cseru@gmail.com
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

bool search(node* root, int item) {
    if(root == NULL) {
        return false;
    }
    if(root->data = item) {
        printf("\n%p\n", root);
        return true;
    }
    else if(root->data < item) {
        search(root->right, item);
    } else {
        search(root->left, item);
    }
}

void preOrderDisplay(node *root) {
    if(root != NULL) {
        cout << root->data << " ";
        preOrderDisplay(root->left);
        preOrderDisplay(root->right);
    }
}

void inOrderDisplay(node *root) {
    if(root != NULL) {
        inOrderDisplay(root->left);
        cout << root->data << " ";
        inOrderDisplay(root->right);
    }
}

void postOrderDisplay(node *root) {
    if(root != NULL) {
        postOrderDisplay(root->left);
        postOrderDisplay(root->right);
        cout << root->data << " ";
    }
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

    preOrderDisplay(root);
    cout << endl;
    inOrderDisplay(root);
    cout << endl;
    postOrderDisplay(root);

    if(search(root, 17)) {
        cout << "Node Found\n";
    }
    
    return 0;
}