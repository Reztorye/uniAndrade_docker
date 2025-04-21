CC = gcc
CFLAGS = -Wall -Werror -Wno-unused-result -O2
O = ./obj
SRC = ./src/*.c
EXEC = $(O)/strings

all:
	$(CC) $(CFLAGS) -o $(EXEC) $(SRC)

run:
	$(EXEC)

asm:
	for file in $(SRC); do \
		$(CC) $(CFLAGS) -S -o $(O)/$$(basename $$file .c).s $$file; \
	done

clear:
	rm -f $(O)/*
