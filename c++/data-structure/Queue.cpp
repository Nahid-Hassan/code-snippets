#include <bits/stdc++.h>
using namespace std;

#define READ() freopen("in.txt", "rt", stdin)
int input() {int n; cin >> n; return n;}

#define maxSize 10

int Queue[maxSize];
int Rear = -1;
int Front = -1;

void push() {
    if((Front == 0 && Rear ==  maxSize - 1) || Front == Rear + 1) {
        cout << "Overflow\n";
        exit(0);
    }
    if(Front == -1) {
        Rear = Front = 0;
    } else {
        if(Rear == maxSize - 1) {
            Rear = 0;
        } else {
            Rear++;
        }
    }
    cout << "Enter the element you want to push: ";
    Queue[Rear] = input();
}

void pop() {
    if(Front == -1) {
        cout << "Queue is underflow\n";
        exit(0);
    }
    cout << "Element is deleted from queue is: " << Queue[Front] << endl;
    if(Front == Rear) {
        Front = Rear = -1;
    } else {
        if(Front == maxSize - 1) {
            Front = 0;
        } else {
            Front++;
        }
    }
}

void display() {
    int front_pos = Front, rear_pos = Rear;
    if (Front == -1) {
        cout<<"Queue is empty\n";
        return;
    }
    cout<<"Queue elements :\n";
    if (front_pos <= rear_pos) {
        while (front_pos <= rear_pos) {
            cout<<Queue[front_pos]<<"  ";
            front_pos++;
        }
    } else {
        while (front_pos <= maxSize - 1) {
            cout<<Queue[front_pos]<<"  ";
            front_pos++;
        }
        front_pos = 0;
        while (front_pos <= rear_pos) {
            cout<<Queue[front_pos]<<"  ";
            front_pos++;
        }
    } cout<<endl;
}


int main() {
    cout << "Enter the value How many times operate push and pop: ";
	int testCase = input();

	int choice;
	while(testCase--){
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

	cout << "Stack Contains: ";
	display();

    return 0;
}
