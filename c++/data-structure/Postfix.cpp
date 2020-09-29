#include <bits/stdc++.h>
using namespace std;

#define maxSize  100

int Stack[maxSize];
int top = -1;

int input() {int n; cin >> n; return n;}

void push(int data) {
	if(top == maxSize - 1) {
		cout << "Stack is full." << endl;
		exit(0);
	} else {
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
    string s, s1;
    int num;
    char ch;

    getline(cin, s);

    istringstream is(s);

    while(is >> s1) {
        if(s1.size() > 1) {
            num = stoi(s1);
            push(num);
        } else if (s1.size() == 1) {
            if(s1[0] == '+' || s1[0] == '-' || s1[0] == '*' || s1[0] == '/') {
                if(s1[0] == '+') {
                    int a = pop();
                    int b = pop();

                    push((a+b));
                } else if(s1[0] == '-') {
                    int a = pop();
                    int b = pop();

                    push((b-a));
                } else if(s1[0] == '*') {
                    int a = pop();
                    int b = pop();

                    push((a*b));
                } else if(s1[0] == '/') {
                    int a = pop();
                    int b = pop();

                    push((b/a));
                }
            } else  {
                num = stoi(s1);
                push(num);
            }
        }
    }
    cout <<pop() << endl;

	return 0;
}
