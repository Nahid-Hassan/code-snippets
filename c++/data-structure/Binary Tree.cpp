#include <bits/stdc++.h>
using namespace std;

typedef struct Node node;
struct Node {
    int data;
    node *left, *right;
}

node* insertBinaryTree(node* root, int data) {
    node *newNode = new node();
    newNode->left = newNode->right = NULL;

    node parent = NULL;
    node current = root;

    while(current != NULL)
}

int main() {

}
