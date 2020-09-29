/**
 * Problem: Insert and delete element from Queue
 */
#include <bits/stdc++.h>
using namespace std;

#define mx 10

int input() {int n; cin >> n; return n;}

int top = 0;
int ctrl = 0;

int Queue[mx];

void display(int control) {
    for(int i = control; i < top; i++) {
        cout << Queue[i] << " ";  
    } cout << endl;
}

void Insert() {
    if(top == mx - 1) {
        cout << "Queue is overflow." << endl;
    } else {
        cout << "Enter the data you want to insert: ";
        Queue[top++] = input();
    }
    cout << "After insert data, Queue contains: ";
    display(ctrl);
}

void Delete() {
    ctrl++;
    if(ctrl > top) {
        cout << "Queue is empty." << endl;
        return;
    }
    cout << "After delete data, Queue contains: ";
    display(ctrl);
}


int main() {
    bool flag = true;
    
    while(flag) {
        cout << "1. Insert: " << endl;
        cout << "2. Delete: " << endl;
        cout << "3. Exit: " << endl;

        cout << "Enter your choice: ";
        int choice = input();

        switch (choice) {
            case 1: 
                Insert();
                break;
            case 2: 
                Delete();
                break;
            case 3:
                flag = false;
                break;
            default:
                cout << "You enter the wrong choice." << endl;
                break;
        }
    }

    return 0;
}
