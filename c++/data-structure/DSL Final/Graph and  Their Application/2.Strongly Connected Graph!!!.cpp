/*
 * Problem: Take adjacency matrix(A) with m nodes as input and calculate B = A + A ^ 1 + .... + A^nodes and from
 * that calculate Path matrix and tell whether the matrix is strongly connected or not.  
 * 
 * Solution:
 * Take your adjacent matrix(suppose A)
 * Calculate A^2, A^3, ..... , A^Nodes
 * Then add all A, A^2, A^3, ..... , A^Nodes Matrix in Another Matrix(suppose B)
 * Then check all the element value of matrix B is greater then or equal 1. If all the element of Matrix B 
 * is greter than or equat 1 then this Graph is fully connected otherwise not.
 *  
 */
/**
 ## Example:
    In your graph how many nodes or vertices you want to take input: 4
    0 0 0 1
    1 0 1 1
    1 0 0 1
    0 0 1 0

    1 0 1 1 
    1 0 1 1 
    1 0 1 1 
    1 0 1 1 

    Not Strongly connected Graph.
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
    //Take input for How many vertices in your graph.
    cout << "In your graph how many nodes or vertices you want to take input: ";
    int vertices;
    cin >> vertices;
    
    //Declare Adjacent Matrix
    int adjMat[vertices][vertices][vertices];
    //using memeset for fill block of memory using specified value
    memset(adjMat, 0, sizeof(adjMat));
    
    //Take Input(Adjacency List)
    cout << "Take input(Adjacency Matrix): \n";
    for(int row = 0; row < vertices; row++) {
        for(int col = 0; col < vertices; col++) {
            cin >> adjMat[0][row][col];
        }
    }

    // Matrix Multiplication (Calculate A^2, A^3, ..... , A^Nodes)
    for(int outer = 1; outer < vertices; outer++) { //outer variable control 3-D matrix
        for(int row = 0; row < vertices; row++) {
            for(int col = 0; col < vertices; col++) {
                for(int inner = 0; inner < vertices; inner++) {
                    adjMat[outer][row][col] += adjMat[outer-1][row][inner] * adjMat[0][inner][col];
                }
            }
        } 
    } 

    //Declare 2D matrix to add and store A, A^2, A^3, ..... , A^Nodes Matrix
    int pathMat[vertices][vertices];
    memset(pathMat, 0, sizeof(pathMat));

    for(int k = 0; k < vertices; k++) {
        for(int row = 0; row < vertices; row++) {
            for(int col = 0; col < vertices; col++) {
                pathMat[row][col] += adjMat[k][row][col];
            }
        }
    }

    //print path matrix and check all the elements of pathMat is greater than or equal 1??? 
    int count = 0;
    //print newline
    cout << endl;

    for(int row = 0; row < vertices; row++) {
        for(int col = 0; col < vertices; col++) {
            if(pathMat[row][col] >= 1) {
                count++;
                pathMat[row][col] = 1;
            }
            cout << pathMat[row][col] <<" ";
        } cout << endl;
    } cout << endl;

    if(count == vertices * vertices) {
        cout << "Strongly connected Graph." << endl << endl;
    } else {
        cout << "Not Strongly connected Graph." << endl << endl;
    }

    return 0;
}