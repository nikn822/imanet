.PHONY: all clean

all: imanet

imanet:
	mkdir -p build && cd build && cmake -G Ninja .. && ninja

clean:
	rm -rf build
