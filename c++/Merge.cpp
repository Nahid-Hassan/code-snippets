#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

int main() {
    cout << "How many inptut you want to take for data set 1: ";
    int totalItem1 = input();

    int data1[totalItem1];
    for(int i = 0; i < totalItem1; i++) {
        data1[i] = input();
    }

    cout << "How many inptut you want to take for data set 2: ";
    int totalItem2 = input();

    int data2[totalItem2];
    for(int i = 0; i < totalItem2; i++) {
        data2[i] = input();
    }

    int data3[totalItem1 + totalItem2 + 5];
    int j = 0;
    for(int i = 0; i < totalItem2 + totalItem1; i++) {
        if(i < totalItem1) data3[i] = data1[i];
        else {
            data3[i] = data2[j++];
        }
    }

    cout << "\n----------------------------------\n";
    cout << "After merging two data set:";
    for(int i = 0; i < (totalItem1 + totalItem2); i++) {
        cout << " " << data3[i];
    }cout << endl;


    return 0;
}


