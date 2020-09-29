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

int max_heap[mx];

int input() {int n; cin >> n; return n;}

void max_heapify(int idx, int size) {
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;
    int largest = idx;

    if(left < size && max_heap[left] > max_heap[idx]) {
        largest = left;
    }
    if(right < size && max_heap[right] > max_heap[largest]) {
        largest = right;
    }

    if(largest != idx) {
        swap(max_heap[idx], max_heap[largest]);
        max_heapify(largest, size);
    }
}

void insert_item(int size) {
    int parent = (size - 1) / 2;
    
    if(max_heap[size] > max_heap[parent]) {
        swap(max_heap[size], max_heap[parent]);
        insert_item(parent);
    }
}

void delete_item(int idx, int size) {
    max_heap[idx] = max_heap[size];

    for(int i = size / 2 - 1; i >= 0; i--) {
        max_heapify(i, size);
    }
}

void print_heap(int size) {
    cout << "Heap: ";
    for(int i = 0; i < size; i++) {
        cout << max_heap[i] << " ";
    } cout << endl;
}

int main() {
    cout << "Enter how many element you want to insert: ";
    int size = input();

    cout << "Read data: ";
    for(int i = 0; i < size; i++) {
        max_heap[i] = input();
    }

    //heapify max_heap array
    for(int idx = size / 2 - 1; idx >= 0; idx--) {
        max_heapify(idx, size);
    }

    print_heap(size);

    cout << "How many data you want to insert: ";
    int tInsert = input();

    cout << "Read data: ";
    int temp_size = size;
    for(int i = 0; i < tInsert; i++) {
        temp_size++;
        max_heap[temp_size - 1] = input();
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
            if(max_heap[i] == item) {
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
