// Bubble Sort in C++

#include <iostream>
#include <new>
#include "bubbleSort.h"


void bubbleSort::getData(){
    std::cout << "How many elements are required: ";
    std::cin >> n;
    std::cout << "Please enter the origin array: ";
    for (int i = 0; i < n; i++){
        std::cin >> arr[i];
    }
}

void bubbleSort::sortFunc(){
    int temp;
    for (int i = 0; i < n; i++){
        bool flag = true;
        for (int j = 0; j < n-1-i; j++){
            if (arr[j] > arr[j+1]){
                temp     = arr[j];
                arr[j]   = arr[j+1];
                arr[j+1] = temp;
                flag     = false;
            }
        }
        if (flag){
            break;
        }
    }
}

void bubbleSort::showData(){
    std::cout << "\n****show data****\n";
    for (int i = 0; i < n; i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}
