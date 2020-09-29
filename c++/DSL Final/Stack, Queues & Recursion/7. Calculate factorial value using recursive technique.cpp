/**
 * Calculate the factorial number of a given number using recursive technique.
 */
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;

int input() {int n; cin >> n; return n;}

ull fact(ull num) {
    if(num == 1) {
        return 1;
    } else {
        return num * fact(num - 1);
    }
}

int main() {
    cout << "Enter an integer value(less than 20): ";
    int num = input();

    cout << (fact(num)) << endl;

    return 0;
}
