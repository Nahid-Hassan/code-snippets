//for integer number only
#include<bits/stdc++.h>
using namespace std;

string data[100];

//For assending order
int findPos(string data[], int n, string item) {
    int pos = 0;
    if(n > 1) {
        int i = 0;
        while(data[i] <= item && i < n) {
            i++; pos = i;
        }
    } else {
        if(data[0] <= item) {pos = 1; return pos;}
        else {pos = 0; return pos;}
    }

    return pos;
}

void insert(string data[], int pos, string item, int & n) {
    int i = n;

    while(i >= pos) {
        data[i + 1] = data[i];
        i--;
    }
    data[pos] = item;
    n++;
}

int main() {
    cout << "How many word you want to take?  ";
    int n;
    cin >> n;

    cout << "Read input: ";
    for(int i = 0; i < n; i++) {
        cin >> data[i];
    }
    cout << "Enter a word you want to insert: ";
    string item; cin >> item;

    cout << "Are you want to say insert  positon? Enter 1 or 0\n";
    int key; cin >> key;
    int pos;

    if(!key)  pos = findPos(data, n, item);
    else{ cout << "Enter position: ";  cin >> pos;}
    
    insert(data, pos, item, n);

    cout << "\nAfter insert item in the array list: \n";
    cout << "------------------------------------\n";
    cout << "Total item = " << n << endl;
    cout << "Contains all the items in the array: ";
  
    for(int i = 0; i < n; i++) {
        cout << data[i] << " ";
    } cout << endl;

    return 0;
}
