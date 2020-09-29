/**
 * Tower of Hanoi.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

void Toh(int n, char begin, char middle, char end) {
    if(n >= 1) {
        Toh(n - 1, begin, end, middle);
        cout << n << " disk is move " << begin << " to " << end << endl;
        Toh(n - 1, middle, begin, end); 
    }
}

int main() {
    cout << "Enter the number of disks: ";
    int disk = input();    

    Toh(disk, 'A', 'B', 'C');

    return 0;
}

