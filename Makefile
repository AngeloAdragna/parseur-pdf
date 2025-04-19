all: parser.exe

parser.exe: parser.cpp
	g++ -o parser.exe parser.cpp

clean:
	rm -f parser.exe
