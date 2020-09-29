/**
 * Calculate the Fn of a Fibonacci sequence using recursive technique.
 */
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;

ull input() {ull n; cin >> n; return n;}

ull fibonacci(ull num) {
    if(num <= 1) return num;
    else return fibonacci(num - 1) + fibonacci(num - 2);
}

int main() {
    cout << "Enter a number: ";
    ull num = input();

    cout << (fibonacci(--num)) << endl; //fibonacci series start from zero.
}
