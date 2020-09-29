/**
 * Problem: Matrix operation related.
 * Perform addition, subtraction, multiplication.
 * 
 * simple: 
 * 1) for addition ... dimension of two 2d array are same add element by element in
 * their respective position. same for subtraction.
 * 2) for multiplication ... dimension of two 2d array are not must be same-> but first
 * matrix col and 2nd matirx row must be same.
 * Equation for matrix multiplication: matrix_mul[row][col] += matrix_A[row1][inner->col1] * matrix_B[inner->col1][col2]
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
    
    bool flag = true;
    int matrix_mul[row1][col2];
    memset(matrix_mul, 0, sizeof(matrix_mul));

    if(col1 == row2) {
        //perform matrix multiplication
        for(int i = 0; i < row1; i++) {
            for(int j = 0; j < col2; j++) {
                for(int inner = 0; inner < col1; inner++) {
                    matrix_mul[i][j] += matrix1[i][inner] * matrix2[inner][j];
                }
            }
        }
    } else {
        cout << endl << "Matrix multiplication not possible." << endl;
        flag = false;
    }

    if(flag) {
        cout << "Matrix multiplication result: \n";
        for(int i = 0; i < row1; i++) {
            for(int j = 0; j < col2; j++) {
                cout << matrix_mul[i][j] << " ";
            } cout << endl;
        }
    }

    return 0;
}
