#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}

//binary search
int binarySearch(string data[], int totalItem, string srcItem) {
    int low = 0, mid, high = totalItem - 1;

    while(low <= high) {
        mid = (low + high) / 2;

        if(data[mid] == srcItem) return ( mid + 1 );
        else if (data[mid] > srcItem) high = mid - 1;
        else if (data[mid] < srcItem) low = mid + 1;
    }

    return -1;
}

int main() {
    string data[100];

    cout << "How many input you want to take: ";
    int totalItem = input();
    for(int i = 0; i < totalItem; i++) {
        cin >> data[i];
    }

    //linear search
    cout << "Enter the element you want to search: ";
    string srcItem;
    cin >> srcItem;
    bool flag = true;

    cout << "------------------------------------\n";
    for(int i = 0; i < totalItem; i++) {
        if(data[i] == srcItem) {
            cout << "Fine item: " << data[i] <<" at position " << i + 1 << endl;
            flag = false;
            break;
        }
    }
    if(flag) {
        cout << "Not found\n";
    }

    //bubble sort
    for(int i = 0; i < totalItem - 1; i++) {
        for(int j = 0; j < totalItem - i - 1; j++) {
            if(data[j] > data[j + 1]) {
                string temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
            }
        }
    }

    //After sort print data
    cout << "\nAfter sorting data item:";
    for(int i = 0; i < totalItem; i++) {
        cout << " " << data[i];
    } cout << endl;
    cout << "\n------------------------------------\n";
    //binary search
    cout << "Enter the element you want to search: ";
    cin >> srcItem;

    int returnVal = binarySearch(data, totalItem, srcItem);

    if(returnVal == -1) {
        cout << "\nNot found\n";
    } else {
        cout << "\nFound at position " << returnVal << endl;
    }

    return 0;
}

