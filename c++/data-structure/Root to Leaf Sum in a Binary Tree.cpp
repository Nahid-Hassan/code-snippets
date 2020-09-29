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

vector <int> result;

bool rootToLeafSum(node* root, int sum) {
    if(root == NULL) return false;
    if(root->left == NULL && root->right == NULL) {
        if(root->data == sum) {
            result.push_back(root->data);
            return true;
        } else return false;
    }

    if(rootToLeafSum(root->left, sum - root->data)) {
        result.push_back(root->data);
        return true;
    }
    if(rootToLeafSum(root->right, sum - root->data)) {
        result.push_back(root->data);
        return true;
    }

    return false;
}

int main() {
    node *root = NULL;

    root = insertBST(root, 10);
    insertBST(root, 5);
    insertBST(root, 16);
    insertBST(root, -3);
    insertBST(root, 6);
    insertBST(root, 11);

    int sum = 12;
    if(rootToLeafSum(root, sum)) {
        cout << "Found!!\n";
        reverse(result.begin(), result.end());
        for(int i = 0; i < result.size(); i++) {
            cout << result[i] << " ";
        } cout << endl;
    } else {
        cout << "Not Found!!\n";
    }

    return 0;
}




