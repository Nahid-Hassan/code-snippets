#include<bits/stdc++.h>
using  namespace std;

int input() {int n; cin >> n; return n;}

int process(int data[], int arraySize, int & sum, int & maxValue, int & minValue) {
    maxValue = -0xfffffff;
    minValue = 0xfffffff;

    for(int i = 0; i < arraySize; i++) {
        sum += data[i];
        if(data[i] > maxValue) maxValue = data[i];
        if(data[i] < minValue) minValue = data[i]; 
    }
    return sum;
}

int main( ) {
    int arraySize = input();
    int data[arraySize];

    cout << "Read Data: ";
    for(int i = 0; i < arraySize; i = i + 1) {
        cin >> data[i];
    }
    int sum = 0;
    int maxValue, minValue;

    sum = process(data, arraySize, sum, maxValue, minValue);

    cout << "Min value : " << minValue << endl; //min Value
    cout << "Max Value : " << maxValue << endl; //max Value
    cout << "Avg Value : " << ((double)sum / arraySize) << endl; //average value

    //sin value 
    for(int i = 0; i < arraySize; i++) {
        cout << "sin(" << data[i] <<") degree: " << sin(M_PI*data[i]/180.0) <<endl;
    }

    return 0;

