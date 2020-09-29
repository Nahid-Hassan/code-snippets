/**
 * Traversing: Carry out the following operations on an Array.
 * Maximum Value, Minimum Value, Average Value, Total Value, Sin Value.
 */
#include<bits/stdc++.h>
using  namespace std;

int input() {int n; cin >> n; return n;}

void process(int data[], int arraySize, int & sum, int & maxValue, int & minValue) {
    maxValue = std::numeric_limits<int>::min();
    minValue = std::numeric_limits<int>::max();

    for(int i = 0; i < arraySize; i++) {
        sum += data[i];
        if(data[i] > maxValue) maxValue = data[i];
        if(data[i] < minValue) minValue = data[i]; 
    }
}

int main( ) {
    cout << "How many elements you want to take: ";
    int arraySize = input();
    int data[arraySize];

    cout << "Read Data: ";
    for(int i = 0; i < arraySize; i = i + 1) {
        cin >> data[i];
    }
    
    int maxValue, minValue, sum = 0;

    process(data, arraySize, sum, maxValue, minValue);

    cout << "Min value : " << minValue << endl; //min Value
    cout << "Max Value : " << maxValue << endl; //max Value
    cout << "Avg Value : " << ((double)sum / arraySize) << endl; //average value

    //sin value 
    for(int i = 0; i < arraySize; i++) {
        cout << "sin(" << data[i] <<") degree: " << sin(M_PI*data[i]/180.0) <<endl;
    }

    return 0;
}