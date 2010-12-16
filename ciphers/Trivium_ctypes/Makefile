CC = gcc
CFLAGS = -g -Wall -O3

trivium-api.so: trivium.o trivium-api.o
	$(CC) $(CFLAGS) -shared -o $@ $^

trivium.o: trivium.c
	$(CC) $(CFLAGS) -o $@ -c $^

trivium-api.o: trivium-api.c
	$(CC) $(CFLAGS) -fPIC -o $@ -c $^
	

clean:
	rm -f *.o *.so
