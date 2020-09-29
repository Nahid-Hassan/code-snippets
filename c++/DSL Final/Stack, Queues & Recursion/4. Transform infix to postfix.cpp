/**
 * Transform infix to postfix.
 */
#include <bits/stdc++.h>
using namespace std;

char Stack[100];
int top = 0;

void push(char item) {
    if(top == 100) {
        cout << "Overflow." << endl;
    } else {
        Stack[top] = item;
        top++;
    }
}

char pop() {
    if(top < 0) {
        cout << "Underflow" << endl;
        return '!';
    } else {
        char data = Stack[top - 1];
        top -= 1;
        return data;
    }
}

bool operatorChecking(char ch) {
    if(ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^') return true;
    else return false;
}

int precedence(char ch) {
    if(ch == '+' || ch == '-') return 1;
    else if(ch == '*' || ch == '/') return 2;
    else return 3;
}

int main() {
    string s;
    char p[100];

    cout << "Enter the expression in infix order: ";
    getline(cin, s);

    s = '(' + s + ')';
    int idx = 0;
    int len = s.length();
    cout << s << endl;

    for(int i = 0; i < len; i++) {
        cout << "s[" << i <<"] = " << s[i] << endl; 
        if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
            p[idx] = s[i];
            idx++; 
        } else if(s[i] == '(') {
            push(s[i]);
        } else if (operatorChecking(s[i])) {
            char com = pop();

            if(operatorChecking(com) && operatorChecking(s[i])) {
                if(precedence(com) < precedence(s[i])) {
                    push(com);
                } else {
                    p[idx] = com;
                    idx++;
                }
                push(s[i]);
            } else {
                push(com);
                push(s[i]);
            }
        } else if(s[i] == ')') {
            while(true) {
                char com = pop();
                if(com == '(') break;
                else { p[idx] = com; idx++;}    
            }
        }
        else continue;
    } 
    p[idx] = '\0';
    cout << p << endl;

    return 0;
}
