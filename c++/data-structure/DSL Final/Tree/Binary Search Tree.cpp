//Author: nahid.cseru@gmail.com
/**
 * Problem: Write a progarm to insert an element in a Binary Search Tree. If the element already inserted 
 * before then display the location.
 * 
 * Solution: Simple Recursion Based solution.
 * This problem is also solution for -> Tree Problem No. - 4, 5, 6(Traversing Tree)
 */

#include <bits/stdc++.h>
using namespace std;

//define array size
#define BSTSize 100

//declare global variable
//declare globaly because it decrease complexity of code
int arrayOfBST[BSTSize]; 

// Take integer input()
int input() {int n; cin >> n; return n;}

// create Binary Search Tree
void createBST(int data, int idx) {
    // if idx is greater than array size of print No space Availabe in the array.
    if(idx > BSTSize) {
        cout << "No space Available in the Array." << endl;
    } else { 
        // if arrayOfBST[idx] == -1, that means in this place no element is not inserted yet
        if(arrayOfBST[idx] == -1) {
            arrayOfBST[idx] = data;
        } else {
            // if data == arrayOfBST[idx], then print this element is already inserted.
            if(data == arrayOfBST[idx]) {
                cout << "The element already inserted at location: " << idx << "." << endl;
            } else if (data < arrayOfBST[idx]) {
                /**
                 * if data is less then arrayOfBST[idx], then data inserted in it's(root,subroot) left subtree
                 * else right subtree.
                 */
                int leftChild = idx * 2;
                createBST(data, leftChild); 
            } else {
                int rightChild = (idx * 2) + 1;
                createBST(data, rightChild);
            }
        }
    }
}

//print your BST on preorder
void preOrder(int idx) {
    /**
     * Visit->Left->Right
     */
    if(arrayOfBST[idx] != -1) {
        cout << arrayOfBST[idx] << " ";
        preOrder(idx * 2);
        preOrder((idx * 2) + 1);
    }
}

//print your BST on inorder
void inOrder(int idx) {
    /**
     * Left->Visit->Right
     */
    if(arrayOfBST[idx] != -1) {
        inOrder(idx * 2);
        cout << arrayOfBST[idx] << " ";
        inOrder((idx * 2) + 1);
    }
}

// print your BST on postorder
void postOrder(int idx) {
    /**
     * Left->Right->Visit
     */
    if(arrayOfBST[idx] != -1) {
        postOrder(idx * 2);
        postOrder((idx * 2) + 1);
        cout << arrayOfBST[idx] << " "; 
    }
}

int main() {
    cout << "How many data you want to insert in BST: ";
    int tData = input();
    
        //using memeset for fill block of memory using specified valu
    memset(arrayOfBST, -1, sizeof(arrayOfBST));

    //Take input one by one
    cout << "Enter elements you want to insert: " << endl;
    cout << "----------- Warnning you cannot insert (-1) ----------------" << endl;
    
    int rootIdx = 1;
    for(int i = 1; i <= tData; i++) {
        int data = input();

        createBST(data, rootIdx); //root index allways 1
    }
    cout << "-----------------------------------------------------\n";
    //print your BST array -> InOrder, preOrder, postOrder
    cout << "Preorder: ";
    preOrder(rootIdx);
    cout << endl << endl;

    cout << "Inorder: ";
    inOrder(rootIdx);
    cout << endl << endl;

    cout << "Postorder: ";
    postOrder(rootIdx);
    cout << endl << endl;

    return 0;
}