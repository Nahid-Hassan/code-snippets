/**
 * Problem: Find out the shortest path of a Weighted Graph G with m nodes V1, V2, .. , Vm
 * and weight of each edge is W(e) using Warshall's Algorithm.
 * 
 * Solution: Calculate P(k)[i, j] = min(P(k-1)[i, j], (P(k-1[i, k] + P(k-1)[k, j])))
 */
/**
 * Demo Input-Output:
      In your graph how many nodes or vertices you want to take input: 4
      Take input(Adjacency Matrix): 
      7 5 0 0
      7 0 0 2
      0 3 0 0
      4 0 1 0
      
      P^1: 
      7 5 10000 10000 
      7 10000 10000 2 
      10000 3 10000 10000 
      4 10000 1 10000 
      
      
      P^2: 
      7 5 10000 7 
      7 10000 10000 2 
      10 3 10000 5 
      4 10000 1 10000 
      
      
      P^3: 
      7 5 10000 7 
      7 10000 10000 2 
      10 3 10000 5 
      4 4 1 6 
      
      
      Finally Shortest Path Matrix: P^4: 
      7 5 8 7 
      6 6 3 2 
      9 3 6 5 
      4 4 1 6 
      
 */
#include <bits/stdc++.h>
using namespace std;

//int inf = std::numeric_limits<int>::max();
int inf = 10000;

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
            int weight;
            cin >> weight;
            if(weight != 0) {
                adjMat[0][row][col] = weight;
            } else {
                adjMat[0][row][col] = inf;
            }
        }
    }

    // Calculate P(k)[i, j] = min(P(k-1)[i, j], (P(k-1[i, k] + P(k-1)[k, j])))
    for (int k = 1; k < vertices; k++) {
        for (int row = 0; row < vertices; row++) {
            for (int col = 0; col < vertices; col++) {
                adjMat[k][row][col] = min(adjMat[k-1][row][col], (adjMat[k-1][row][k] + adjMat[k-1][k][col]));
            }
        }
    }
    for (int k = 0; k < vertices; k++) {
        if(k == vertices - 1) {
            cout << "\nFinally Shortest Path Matrix: P^" << (k + 1) <<": \n";
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