all: dia test2

dia: dia.o
	g++ -g -o dia dia.o 

test2:
	./dia | dot -Tpng -o showcase.png
	
clean:
	rm *.o
