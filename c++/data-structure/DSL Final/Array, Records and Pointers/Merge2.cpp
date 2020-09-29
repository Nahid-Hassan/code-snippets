/**
 * Merging:
 * a) Add two character type arrays
 * 
 * Solution: Very simple. Let's see the code.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

int main() {
    cout << "Enter the number of element you want to insert in array1: ";
    int size1 = input();

    string array1[size1];

    cout << "Read data for array1: ";
    for(int i = 0; i < size1; i++) {
       cin >> array1[i];
    }

    cout << "Enter the number of element you want to insert in array2: ";
    int size2 = input();

    string array2[size2];

    cout << "Read data for array2: ";
    for(int i = 0; i < size2; i++) {
        cin >> array2[i];
    }

    //merge two character type arrays
    int tSize = (sizeof(array1)/sizeof(array1[0])) + (sizeof(array2)/sizeof(array2[0]));
    string array3[tSize];

    int idx = 0;
    for(int i = 0; i < tSize; i++) {
        if(i < (sizeof(array1)/sizeof(array1[0]))) {
            array3[i] = array1[i];
        } else {
            array3[i] = array2[idx++];
        }
    }
    
    cout << "After merging print the merging array:";
    for(int i = 0; i < tSize; i++) {
        cout << " " << array3[i];
    } cout << endl;

    return 0;
}
