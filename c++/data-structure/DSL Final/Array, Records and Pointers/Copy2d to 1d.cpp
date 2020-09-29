/**
 * Problem: Copy elements of a 2d array into a 1d/linear array and print the elements of 
 * group 3 from the 1d array.
 * 
 * Solution: Simple array based solution.
 */

#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

int main() {
    cout << "Enter the dimension of 2d array: ";
    int row = input();
    int col = input();

    int array2d[row][col];

    cout << "Read 2d array: ";
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            cin >> array2d[i][j];
        }
    }

    // copy elements 2d array to 1d array
    int array1d[row * col];
    
    //main process
    int idx = 0;
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            array1d[idx++] = array2d[i][j];
        }
    }

    //print random group row based
    cout << "Enter the group number you want to print: ";
    int group_number = input();

    cout << "Group " << group_number << ":";
    for(int i = (group_number - 1) * col; i < group_number * col; i++) {
        cout << " " << array1d[i];
    } cout << endl;

    return 0;
}
