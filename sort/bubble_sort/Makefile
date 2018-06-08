
output: main.o bubbleSort.o
	g++ main.o bubbleSort.o -o output

main.o: main.cpp
	g++ -c main.cpp

bubbleSort.o: bubbleSort.cpp bubbleSort.h
	g++ -c bubbleSort.cpp

clean:
	rm *.o output
