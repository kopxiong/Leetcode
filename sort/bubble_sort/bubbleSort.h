#ifndef _BUBBLE_SORT_H
#define _BUBBLE_SORT_H

#include <iostream>
#define MAX 10


class bubbleSort
{
private:
    int arr[MAX];
    int n;
public:
    void getData();
    void sortFunc();
    void showData();
};

#endif
