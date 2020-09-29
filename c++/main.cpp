//heap data structure (min heap)
#include <bits/stdc++.h>
using namespace std;

int left(int i) {
	return 2 * i;
}

int right(int i ) {
	return 2 * i + 1;
}

int parent(int i) {
	return i / 2;
}

//heapify
void max_heapify(int heap[], int heap_size, int i) {
	int l, r, largest, t;

	l = left(i); 
	r = right(i);

	if (l <= heap_size && heap[l] > heap[i]) {
		largest = l;
	} else {
		largest = i;
	}

	if (r <= heap_size && heap[r] > heap[largest]) {
		largest = r;
	}

	if(largest != i) {
		t = heap[i];
		heap[i] = heap[largest];
		heap[largest] = t;

		max_heapify(heap, heap_size, largest);
	}
}

void build_max_heap(int heap[], int heap_size) {
	for(int i = heap_size / 2; i >= 1; i--) {
		max_heapify(heap, heap_size, i);
	}
}

//driver program
int main() {
	int heap[] = {0, 10, 7, 17, 3, 5, 12, 10, 1, 2};
	int heap_size = sizeof(heap) / sizeof(int);

	build_max_heap(heap, heap_size);

	for(int i = 1; i <= heap_size; i++) {
		cout << heap[i] << " ,";
	} cout << endl;


	return 0;
}
