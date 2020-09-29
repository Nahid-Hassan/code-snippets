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

bool sameBinaryTree(node* root1, node* root2) {
    if(root1 == NULL && root2 == NULL) {
        return true;
    }
    if(root1 == NULL || root2 == NULL) {
        return false;
    }

    return root1->data == root2->data &&
        sameBinaryTree(root1->left, root2->left) &&
        sameBinaryTree(root1->right, root2->right);
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

    node *root2 = NULL;

    root2 = insertBST(root2, 10);
    insertBST(root2, 5);
    insertBST(root2, 0);
    insertBST(root2, -4);
    insertBST(root2, 20);
    insertBST(root2, 21);
    insertBST(root2, 17);
    insertBST(root2, 7);
    insertBST(root2, 3);

    if(sameBinaryTree(root1, root2)) {
        cout << "Yes.\n";
    } else {
        cout << "False.\n";
    }

    cout << sizeOfBinaryTree(root1) << endl;

    return 0;
}

