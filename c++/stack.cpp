#include <bits/stdc++.h>
using namespace std;

#define maxSize  100

int Stack[maxSize];
int top = -1;

int input() {int n; cin >> n; return n;}

void push() {
	if(top == maxSize - 1) {
		cout << "Stack is full." << endl;
		exit(0);
	} else {
		cout << "Enter the element you want to inserted: ";
		int data = input();
		top++;
		Stack[top] = data;
	}
}

int pop() {
	int item;

	if(top == -1) {
		cout << "Stack is empty." << endl;
	} else {
		item = Stack[top];
		top--;
	}
	return item;
}

int main() {
	cout << "Enter the value How many times operate push and pop: ";
	int testCase = input();

	int choice;

	while(testCase--) {
		cout << "1. Push: " << endl;
		cout << "2. Pop: " << endl;

		cout << "Enter the choice: ";
		choice = input();

		switch(choice) {
			case 1: push();
				break;
			case 2: pop();
				break;
			default:
				cout << "You enter the wrong choice!!" << endl;
		}
	}

    //print the element that are in now stack
    cout << "\nStack contains(top to bottom): ";
    for(int i = top; i >= 0; i--) {
		cout << "-->" << Stack[i];
    } cout << endl;



	return 0;
}
