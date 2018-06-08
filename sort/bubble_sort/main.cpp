#include <iostream>
#include <typeinfo>
#include "bubbleSort.h"


int main()
{
    std::cout << "******Bubble Sort******" << std::endl;

    bubbleSort bubble;

    bubble.getData();
    bubble.sortFunc();
    bubble.showData();

    return 0;
}
