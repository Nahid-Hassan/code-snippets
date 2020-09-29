/**
 * Inserting Problem: 
 * 1) 54 tor sorted array. 2) Rahim to a sorted array
 * 3) 99 at postion 5 4) Karim at postion 5
 * 
 * Solution: Simple array Inserting problem. All solution here
 * is generalized solution.
 */
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

// implementation of swap data function for integer type data
void swapIntData(int *data1, int *data2) {
    int temp = *data1;
    *data1 = *data2;
    *data2 = temp;
}

// implementation of bubble sort for integer type data
void bubbleSort(int data[], int totalData) {
    for(int i = 0; i < totalData - 1; i++) {
        for(int j = 0; j < totalData - i - 1; j++) {
            if(data[j] > data[j + 1]) {
                swapIntData(&data[j], &data[j + 1]);
            }
        }
    }
}

int main() {
    cout << "How many data you want to insert(Please insertat least 5 data): ";
    int totalData = input();

    cout << "Enter your data(integer type): ";
    int arrayOfData[totalData + 5];

    for(int i = 0; i < totalData; i++) {
        cin >> arrayOfData[i];
    }

    // sort the array of data
    // using bubble sort(Assending order)
    bubbleSort(arrayOfData, totalData);
    
    cout << "Enter the data you want to insert: ";
    int insertData = input();

    // find position where data insert
    int pos = 0;
    while((insertData >= arrayOfData[pos]) && (pos < totalData)) {
        // increment pos
        pos++;
    }
    // insert data
    for(int idx = totalData; idx > pos; idx--) {
        arrayOfData[idx] = arrayOfData[idx - 1];
    }
    arrayOfData[pos] = insertData;

    // after insert value print the full array of data
    for(int i = 0; i <= totalData; i++) {
        cout << arrayOfData[i] << " ";
    } cout << endl << endl;

    // insert value x at postion y 
    cout << "Enter which position you enter the data: ";
    int insertPostion = input();

    cout << "Enter the value you want to insert: ";
    int posInsertValue = input();

    int idx;
    for(idx = totalData + 1; idx >= insertPostion; idx--) {
        arrayOfData[idx] = arrayOfData[idx - 1];
    }
    arrayOfData[idx] = posInsertValue;

    //after insert value x at position y print the full array of data
    for(int i = 0; i <= totalData + 1; i++) {
        cout << arrayOfData[i] << " ";
    } cout << endl << endl;
    cout << "---------------------Thank You------------------------" << endl;

    return 0;
}
