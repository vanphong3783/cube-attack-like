CC = gcc
CFLAGS = -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes

trivium.so: trivium-lib.o trivium-wrapper.o
	$(CC) -pthread -shared -Wl,-O3 -Wl,-Bsymbolic-functions -o $@ $^

trivium-lib.o: trivium.c
	$(CC) $(CFLAGS) -c -o $@ $^

trivium-wrapper.o: trivium-wrapper.c
	$(CC) $(CFLAGS) -fPIC -I/usr/include/python2.6 -c -o $@ $^
	

clean:
	rm -f *.o *.so
