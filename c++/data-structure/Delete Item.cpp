//Deleting Data from array
//Delete Rahim from array
#include <bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}


string data[20];

int findPos(string data[], int totalDataItem, string item) {
    int i = 0;

    while(data[i] <= item) {
        i++;
    }

    return i;
}

int deleteItem(string data[], int totalDataItem, string item, int pos) {
    for(int i = pos; i < totalDataItem - 1; i++) {
        data[i] = data[i + 1];
    }
    totalDataItem--;

    return totalDataItem;
}

int main() {
    cout << "How many data you want to take: ";
    int totalDataItem = input();

    for(int i = 0; i < totalDataItem; i++) {
        cin >> data[i];
    }

    cout << "Enter the data you want to delete: ";
    string item;
    cin >> item;

    int pos;
    if(totalDataItem > 0) {
        pos = findPos(data, totalDataItem, item);
    } else cout << "Run this program and enter some data!!!\n";

    cout << "Pos = " << pos << endl;

    //delete
    totalDataItem = deleteItem(data, totalDataItem, item, pos-1);

    cout << "\nAfter deleting item: ";
    cout << "\--------------------------\n";
    int i;
    for(i = 0; i < totalDataItem - 1; i++) {
        cout << data[i] << ", ";
    } cout << data[i] << endl;

    return 0;
}

