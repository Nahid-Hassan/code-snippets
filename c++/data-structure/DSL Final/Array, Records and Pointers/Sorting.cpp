/**
 * Problem: Sorting
 * 1) Sort integer data using Bubble sort.
 * 2) Sort string data using Bubble sort.
 * 
 * Solution: Using template
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

// implement bubble sort using template
template <class bubble> 
void bubbleSort(bubble arrayOfElemnt[], int size) {
    for(int i = 0; i < size - 1; i++) {
        for(int j = 0; j < size - i - 1; j++) {
            if(arrayOfElemnt[j] > arrayOfElemnt[j + 1]) {
                swap(arrayOfElemnt[j], arrayOfElemnt[j + 1]);
            }
        }
    }
}


//Driver function
int main() {
    cout << "Enter the total item number you want to insert: ";
    int totalItemNumber = input();

    cout << "Enter the " <<totalItemNumber <<" integer element: ";
    int arrayOfIntegerData[totalItemNumber];

    for(int i = 0; i < totalItemNumber; i++) {
        cin >> arrayOfIntegerData[i];
    }

    //call bubbleSort()
    bubbleSort(arrayOfIntegerData, totalItemNumber);

    //after sorting print the array of integer data
    cout << "After sorting the array of integer data:";
    for(int i = 0; i < totalItemNumber; i++) {
        cout << " " << arrayOfIntegerData[i];
    } cout << endl;

    cout << "Enter the element number(string) you want to insert: ";
    totalItemNumber = input();

    cout << "Enter the " << totalItemNumber << " string element: ";
    string arrayOfStringData[totalItemNumber];

    for(int i = 0; i < totalItemNumber; i++) {
        cin >> arrayOfStringData[i];
    }

    //call bubbleSort()
    bubbleSort(arrayOfStringData, totalItemNumber);
    cout << "After sorting the array of string data:";
    
    for(int i = 0; i < totalItemNumber; i++) {
        cout << " " << arrayOfStringData[i];
    } cout << endl;

    return 0;
}
