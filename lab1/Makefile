CC = g++ 

a1.out:
	$(CC)  ex1-2.cpp
a2.out:
	$(CC) ex3.cpp
run1: clean
	make a1.out
	./a.out
	make clean
run2: clean
	make a2.out
	./a.out
	make clean

clean:
	rm -f *.out
