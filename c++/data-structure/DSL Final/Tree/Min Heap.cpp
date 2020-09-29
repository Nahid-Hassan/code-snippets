/**
 * Write a program that insert an element into the heap.
 * Write a program that delete an element into the heap.
 * 
 * To understand heap insertion deletion procedure you can show that tutorial:
 * https://www.youtube.com/watch?v=eZjwUCgzhMc
 * 
 * Solution: Very simple!!! Let's do the Code....!
 */
#include <bits/stdc++.h>
using namespace std;

#define mx 100

int min_heap[mx];

int input() {int n; cin >> n; return n;}

void min_heapify(int idx, int size) {
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;
    int largest = idx;

    if(left < size && min_heap[left] < min_heap[idx]) {
        largest = left;
    }
    if(right < size && min_heap[right] < min_heap[largest]) {
        largest = right;
    }

    if(largest != idx) {
        swap(min_heap[idx], min_heap[largest]);
        min_heapify(largest, size);
    }
}

void insert_item(int size) {
    int parent = (size - 1) / 2;
    
    if(min_heap[size] < min_heap[parent]) {
        swap(min_heap[size], min_heap[parent]);
        insert_item(parent);
    }
}

void delete_item(int idx, int size) {
    min_heap[idx] = min_heap[size];

    for(int i = size / 2 - 1; i >= 0; i--) {
        min_heapify(i, size);
    }
}

void print_heap(int size) {
    cout << "Heap: ";
    for(int i = 0; i < size; i++) {
        cout << min_heap[i] << " ";
    } cout << endl;
}

int main() {
    cout << "Enter how many element you want to insert: ";
    int size = input();

    cout << "Read data: ";
    for(int i = 0; i < size; i++) {
        min_heap[i] = input();
    }

    //heapify min_heap array
    for(int idx = size / 2 - 1; idx >= 0; idx--) {
        min_heapify(idx, size);
    }

    print_heap(size);

    cout << "How many data you want to insert: ";
    int tInsert = input();

    cout << "Read data: ";
    int temp_size = size;
    for(int i = 0; i < tInsert; i++) {
        temp_size++;
        min_heap[temp_size - 1] = input();
        insert_item(temp_size - 1);
        cout << "After insertion ";
        print_heap(temp_size);
    }
    
    cout << "How many data you want to delete: ";

    int tDelete = input();
    size = size + tInsert;
    int position = -1;

    cout << "Read data: ";
    for(int i = 0; i < tDelete; i++) {
        int item = input();
        bool flag = false;
        
        if(size == 0) {
            cout << "Heap tree is empty!" << endl;
            break;
        }

        for(int i = 0; i < size; i++) {
            if(min_heap[i] == item) {
                position = i;
                break;
            }
        }

        if(position == -1) {
            cout << "This item is not in the heap tree." << endl;
            continue;
        } else {
            size--;
            delete_item(position, size);
        }
        cout << "After delete item: ";
        print_heap(size);
    }


    return 0;
}
