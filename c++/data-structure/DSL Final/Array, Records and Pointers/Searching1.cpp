/**
 * Problem: Searching
 * 1) Search for 77 using linear/binary search
 * 2) Search for karim using linear/binary search
 * 
 * Solution:
 * create 3 function using template-> 1)bubbleSort() 2) linearSearch() 3) binarySearch()
 */

#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

//implement linear Search
template <class linear>
int linearSearch(linear arrayOfElement[], linear size, linear item)  {
    for(int i = 0; i < size; i++) {
        if(item == arrayOfElement[i]) {
            return (i + 1);
        }
    }
    return -1;
}

//implement BubbleSort
template <class bubble>
void bubbleSort(bubble arrayOfElement[], bubble size) {
    for(int i = 0; i < size; i++) {
        for(int j = 0; j < size  - i - 1; j++) {
            if(arrayOfElement[j] > arrayOfElement[j + 1]) {
                swap(arrayOfElement[j], arrayOfElement[j + 1]);
            }
        }
    }
}

// implemnet binary search
template <class binary>
int binarySearch(binary arrayOfElement[], binary size, binary item) {
    binary low = 0, high = size - 1;

    while(low <= high) {
        binary mid = (low + high) / 2;
        if(arrayOfElement[mid] == item) {
            return mid;
        } else if (arrayOfElement[mid] > item) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return -1;
}

//driver program
int main() {
    cout << "----------------- For integer Data--------------------\n";
    cout << "Enter the element number you want to insert(int): ";
    int totalElementNumber = input();

    cout << "Enter the " << totalElementNumber << " integer element: ";
    int arrayOfIntegerData[totalElementNumber];

    for(int i = 0; i < totalElementNumber; i++) {
        cin >> arrayOfIntegerData[i];
    }

    // perform linear search
    cout << "Enter the element you want to search: ";
    int searchItem = input();

    int position = linearSearch(arrayOfIntegerData, totalElementNumber, searchItem);
    
    if(position == -1) {
        cout << "No match data found." << endl;
    } else {
        cout << "Data found at position " << position << endl; 
    }

    // before using binary search you need to sort the array
    bubbleSort(arrayOfIntegerData, totalElementNumber);

    // perform binary Search
    position = binarySearch(arrayOfIntegerData, totalElementNumber, searchItem);

    if(position == -1) {
        cout << "No match data found." << endl;
    } else {
        cout << "Data found at position " << (position + 1) << endl; 
    }

    return 0;
}   
