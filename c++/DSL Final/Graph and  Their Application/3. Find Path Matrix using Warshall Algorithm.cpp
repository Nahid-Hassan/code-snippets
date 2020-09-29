/**
 * Problem: Find out the Path Matrix of an adjacent matrix with m nodes using Warshall's Algorithm.
 * 
 * Solution: Calculate P(k) = (P(k-1)[i, j] | (P(k-1)[i, k] & P(k-1)[k, j])) # Here P is Adjacency Matrix
 */
/*
    # Demo Input Output:
        # Input:
         In your graph how many nodes or vertices you want to take input: 4
            Take input(Adjacency Matrix): 
            0 1 1 1
            0 0 0 1
            0 1 0 1
            0 0 1 0

        # Output:
            P^1: 
            0 1 1 1 
            0 0 0 1 
            0 1 0 1 
            0 0 1 0 


            P^2: 
            0 1 1 1 
            0 0 0 1 
            0 1 0 1 
            0 0 1 0 


            P^3: 
            0 1 1 1 
            0 0 0 1 
            0 1 0 1 
            0 1 1 1 


            Finally Path Matrix: P^4: 
            0 1 1 1 
            0 1 1 1 
            0 1 1 1 
            0 1 1 1 
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

    // Calculate P(k) -> adjMat[k][row][col], k = No of vertices - 1 (0-based index)
    for (int k = 1; k < vertices; k++) {
        for (int row = 0; row < vertices; row++) {
            for (int col = 0; col < vertices; col++) {
                adjMat[k][row][col] = adjMat[k-1][row][col] | (adjMat[k-1][row][k] & adjMat[k-1][k][col]);
            }
        }
    }
    for (int k = 0; k < vertices; k++) {
        if(k == vertices - 1) {
            cout << "\nFinally Path Matrix: P^" << (k + 1) <<": \n";
        } else {
            cout << "\nP^" << (k + 1) << ": " << endl;
        }  
        for (int row = 0; row < vertices; row++) {
            for (int col = 0; col < vertices; col++) {
                cout << adjMat[k][row][col] << " ";
            }
            cout << endl;
        } 
        cout << endl;
    }
    
    return 0;
}