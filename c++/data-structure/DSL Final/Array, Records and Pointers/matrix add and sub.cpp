/**
 * Problem: Matrix operation related.
 * Perform addition, subtraction, multiplication.
 * 
 * simple: 
 * 1) for addition ... dimension of two 2d array are same add element by element in
 * their respective position. same for subtraction.
 * 2) for multiplication ... dimension of two 2d array are not must be same-> but first
 * matrix col and 2nd matirx row must be same.
 * Equation for matrix multiplication: 
 */

#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

int main() {
    cout << "Enter the row and column number for matrix1: ";
    int row1 = input();
    int col1 = input();

    cout << "Read matrix1: \n";
    int matrix1[row1][col1];

    for(int i = 0; i < row1; i++) {
        for(int j = 0; j < col1; j++) {
            matrix1[i][j] = input();
        }
    }

    cout << "Enter the row and column number for matrix2: ";
    int row2 = input();
    int col2 = input();

    cout << "Read matrix2: \n";
    int matrix2[row2][col2];

    for(int i = 0; i < row2; i++) {
        for(int j = 0; j < col2; j++) {
            matrix2[i][j] = input();
        }
    }
    //declare 2 another matrix for perform matrix addition and matrix subtraction.
    int matrix_add[row1][col1];
    int matrix_sub[row1][col1];

    //perform matrix addition
    cout << "Perform addtion and subtraction for Matrix1 +- Matrix2: \n\n";
    if(row1 == row2 && col1 == col2) {
        for(int i = 0; i < row1; i++) {
            for(int j = 0; j < col1; j++) {
                matrix_add[i][j] = matrix1[i][j] + matrix2[i][j];
                matrix_sub[i][j] = matrix1[i][j] - matrix2[i][j];
            }
        }
    } else {
        cout << "Matrix addition and matrix subtraction is not possible.";
    }
    if(row1 == row2 && col1 == col2) {
        cout << "After perform matrix addition: \n";
        for(int i = 0; i < row1; i++) {
            for(int j = 0; j < col1; j++) {
                cout << matrix_add[i][j] << " ";
            } cout << endl;
        } cout << endl << endl;

        cout << "After perform matrix subtraction: \n";
        for(int i = 0; i < row1; i++) {
            for(int j = 0; j < col1; j++) {
                cout << matrix_sub[i][j] << " ";
            } cout << endl;
        } cout << endl << endl;
    }

    return 0;
}
