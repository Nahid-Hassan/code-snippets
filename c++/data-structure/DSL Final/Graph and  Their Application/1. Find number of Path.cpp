// Author: nahid.cseru@gmail.com
/**
 * **** Graph and their application****
 *
 * Write a program that takes an Adjacent matrix A with m vertices as input and output the following:
 * Adjacent of V1, V2, ..... , Vm
 * no of paths of length 2 form Vi to Vj.
 * no of paths of length 3 form Vi to Vj.
 * no of paths of length vertices form Vi to Vj.
 */

//solution:
/**
 * The solution is simple for the given adjacency matrix A of the graph G find out A^k-1 and A^k and then count
 *  number of the 1s in the elements above the diagonal.
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
    //Take input for How many vertices in your graph.
    cout << "Vertices/Nodes/Row Number: ";
    int vertices;
    cin >> vertices;
    
    //Declare Adjacent Matrix
    int adjMat[vertices][vertices][vertices];
    //using memeset for fill block of memory using specified value
    memset(adjMat, 0, sizeof(adjMat));
    
    //Take Input(Adjacency Matrix)
    cout << "Take input(Adjacency Matrix): \n";
    for(int row = 0; row < vertices; row++) {
        for(int col = 0; col < vertices; col++) {
            cin >> adjMat[0][row][col];
        }
    }

    // Matrix Multiplication 
    for(int outer = 1; outer < vertices; outer++) { //outer variable control 3-D matrix
        for(int row = 0; row < vertices; row++) {
            for(int col = 0; col < vertices; col++) {
                for(int inner = 0; inner < vertices; inner++) {
                    adjMat[outer][row][col] += adjMat[outer-1][row][inner] * adjMat[0][inner][col];
                }
            }
        } 
    } 
    
    // Calculate No. of paths Matrix of length 2/3/4 form Vi to Vj.
    int calLenghtMat[vertices-1][vertices][vertices];
    
    for(int k = 1; k < vertices; k++) {
        for(int row = 0; row < vertices; row++) {
            for(int col = 0; col < vertices; col++) {
                calLenghtMat[k][row][col] = adjMat[k][row][col] - adjMat[k-1][row][col]; 
            }
        }
    }

    // calLengthMat[k == 1] means calLenghtMat = adjMat^2 - adjMat^1; assumed 1-based array index, actually 0-based; 
    // calLengthMat[k == 2] means calLenghtMat = adjMat^3 - adjMat^2; 
    // calLengthMat[k == 3] means calLenghtMat = adjMat^4 - adjMat^2; 
    
    //Calculate No. of Path(Store all result)
    int path[3];
    int idx = 2;
    
    for(int k = 1; k < vertices; k++) {
        int countPath = 0;
        for(int row = 0; row < vertices; row++) {
            for(int col = row + 1; col < vertices; col++) {
                if(calLenghtMat[k][row][col] == 1) {
                    countPath++;
                }
            }
        }
        cout << "Number of paths of length " << idx++ << " form Vi to Vj: " << countPath << endl;
    }

    return 0;
}