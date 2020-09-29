//for integer number only
#include<bits/stdc++.h>
using namespace std;

int input() {int n; cin >> n; return n;}
int data[100];

//For assending order
int findPos(int data[], int n, int item) {
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

void insert(int data[], int pos, int item, int & n) {
    int i = n;

    while(i >= pos) {
        data[i + 1] = data[i];
        i--;
    }
    data[pos] = item;
    n++;
}

int main() {
    cout << "How many input take?  ";
    int n = input();

    cout << "Read input: ";
    for(int i = 0; i < n; i++) {
        cin >> data[i];
    }
    cout << "Enter an integer item you want to insert: ";
    int item = input();

    cout << "Are you want to say insert  positon? Enter 1 or 0\n";
    int key = input();
    int pos;

    if(!key)  pos = findPos(data, n, item);
    else{ cout << "Enter position: ";  pos = input();}
    
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
