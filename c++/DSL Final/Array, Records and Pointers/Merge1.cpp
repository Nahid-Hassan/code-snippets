/**
 * Merging:
 * a) Add two integer type arrays.
 * 
 * Solution: Very simple. Let's see the code.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

int main() {
    cout << "Enter the number of element you want to insert in array1: ";
    int size1 = input();

    int array1[size1];

    cout << "Read data for array1: ";
    for(int i = 0; i < size1; i++) {
        array1[i] = input();
    }

    cout << "Enter the number of element you want to insert in array2: ";
    int size2 = input();

    int array2[size2];

    cout << "Read data for array2: ";
    for(int i = 0; i < size2; i++) {
        array2[i] = input();
    }

    //merge two integer type arrays
    int tSize = (sizeof(array1)/sizeof(int)) + (sizeof(array2)/sizeof(int));
    int array3[tSize];

    int idx = 0;
    for(int i = 0; i < tSize; i++) {
        if(i < (sizeof(array1)/sizeof(int))) {
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
