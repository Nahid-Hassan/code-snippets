/**
 * Find the value of arithematic expression P written in postfix.
 */
#include <bits/stdc++.h>
using namespace std;

int Stack[100];
int top = 0;

int push(int item) {
    if(top == 100) {
        cout << "Overflow" << endl;
        return 0;
    } else {
        Stack[top] = item;
        top++;
    }
}

int pop() {
    if(top < 0) {
        cout << "Underflow" << endl;
    } else {
        int data = Stack[top-1];
        top -= 1;
        return data;
    }
}

int main() {
    string s;

    cout << "Enter a string of arithematic expression in postfix: " << endl;

    getline(cin, s);

    int len = s.length(); 
    int i, j;

    for(i = 0; i < len; i++) {
        if(s[i] >= '0' && s[i] <= '9') {
            int n = s[i] - '0';

            for(j = i + 1; ; j++) {
                if(s[j] >= '0' && s[j] <= '9') {
                    n = n * 10 + (s[j] - '0');
                } else {
                    break;
                }
            }
            push(n);
            i = j;
        } else if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' || s[i] == '^') {
            int a = pop();
            int b = pop();

            if(s[i] == '+') push(b + a);
            else if(s[i] == '-') push(b - a);
            else if(s[i] == '*') push(a * b);
            else if(s[i] == '/') push(b / a);
            else if(s[i] == '^') push(pow(b, a));
        } else {
            continue;
        }
    }
    int result = pop();
    cout << "The result is: " << result << endl;
}
