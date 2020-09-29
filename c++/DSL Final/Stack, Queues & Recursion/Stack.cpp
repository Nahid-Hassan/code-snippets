/**
 * Problem: Push an item onto a Stack
 * Problem: Delete the top elements of Satck
 * 
 * Solution: Very simple. Array based solution.
 */
#include <bits/stdc++.h>
using namespace std;

#define mx 10

int Stack[mx];
int top = -1;

int input() {int n; cin >> n; return n;}

void display(int size) {
    while(size != -1) {
        cout << Stack[size] << " ";
        --size;
    }
    cout << endl;
}

void push() {
    if(top == mx - 1) {
        cout << "Stack is full." << endl;
        exit(0);
    } else {
        cout << "Enter the data you want to insert: ";
        Stack[++top] = input(); 
    }
    cout << "After push data stack contains: ";
    display(top);
}

void pop() {
    if(top == -1) { cout << "Stack is emtpy." << endl; exit(0);}
    else --top;

    cout << "After pop data stack contains: ";
    display(top);
}

int main() {
    bool flag = true;
    
    while(flag) {
        cout << "1. Push: " << endl;
        cout << "2. Pop: " << endl;
        cout << "3. Exit: " << endl;

        cout << "Enter your choice: ";
        int choice = input();

        switch (choice) {
            case 1: 
                push();
                break;
            case 2: 
                pop();
                break;
            case 3:
                flag = false;
            default:
                cout << "You enter the wrong choice." << endl;
        }
    }

    return 0;
}

