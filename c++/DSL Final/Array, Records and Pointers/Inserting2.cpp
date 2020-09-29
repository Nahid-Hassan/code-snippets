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

void swapString(string *s1, string *s2) {
    string temp = *s1;
    *s1 = *s2;
    *s2 = temp;
}

void bubbleSort(string data[], int totalItem) {
    for(int i = 0; i < totalItem - 1; i++) {
        for(int j = 0; j < totalItem - i - 1; j++) {
            if(data[j] > data[j + 1]) {
                swapString(&data[j], &data[j + 1]);
            }
        }
    }
}

int main() {
    cout << "How many word you want to insert: ";
    int totalItem = input();

    cout << "Enter " << totalItem << " word: ";
    string arrayOfData[totalItem + 5];

    for(int i = 0; i < totalItem; i++) {
        cin >> arrayOfData[i];
    }

    //sort the array of data
    //using bubble sort
    bubbleSort(arrayOfData, totalItem);

    cout << "Enter the word you want to insert: ";
    string insertData;
    cin >> insertData;

    //find position
    int pos = 0;
    while((insertData >= arrayOfData[pos]) && (pos < totalItem)) {
        pos++;
    }

    //insert data
    for(int idx = totalItem; idx > pos; idx--) {
        arrayOfData[idx] = arrayOfData[idx - 1];
    }
    arrayOfData[pos] = insertData;
    
    // after insert data print the array of data
    for(int i = 0; i <= totalItem; i++) {
        cout << arrayOfData[i] << " ";
    } cout << endl << endl;

    cout << "Enter the position where you insert data: ";
    int insertPosition = input();
    cout << "Enter the data you want to inset: ";
    string insertNewData;
    cin >> insertNewData;

    int idx = 0;
    for(idx = totalItem + 1; idx >= insertPosition; idx--) {
        arrayOfData[idx] = arrayOfData[idx - 1];
    }
    arrayOfData[idx] = insertNewData;

    //after insert element print array of data
    for(int i = 0; i <= totalItem + 1; i++) {
        cout << arrayOfData[i] << " ";
    } cout << endl << endl;

    cout << "--------------------------Thank You------------------" << endl;


    return 0;
}
