/**
 * Problem: Sparse matirx
 * Store the element of a Triangular matrix A into a 1D array B and locate the elements 
 * A32 int the array B
 * 
 * Solution: simple array based solution.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

int main() {
    cout << "Enter the dimension of Triangular(Upper) matrix: \n";
    int row = input();
    int col = input();

    //declare 2d upper triangular matrix
    int matrix_2d[row][col];

    cout << "Read Upper triangular matrix: \n";
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            matrix_2d[i][j] = input();
        }
    }

    //find the total element in upper triangular portion.
    int size = (row * (row+1)) / 2;
    //declare an 1d array
    int array_1d[size];

    // store upper triangular matrix into one dimension array
    int idx = 0;
    for(int i = 0; i < row; i++) {
        for(int j = i; j < row; j++) {
            array_1d[idx++] = matrix_2d[i][j];
        }
    }

    cout << "How many element you want to locate: ";
    int t_locate = input();

    
    cout << "Give element row and column: ";
    int control = 0;
    for(int i = 0; i < t_locate; i++) {
        int r = input(); int c = input();

        cout << "Located element: " << array_1d[(r * (r - 1)) / 2 + r - 1] << " ." << endl;
    }

    return 0;
}


