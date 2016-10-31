#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define noinline __attribute__((noinline))

char dog[] = "dog";
char password[] = "secr3t";

noinline
char dog_letter(int nr)
{
        return dog[nr];
}

int main(int argc, char **argv)
{
        int max = sizeof(dog);
        int i;

        if (argc >= 2)
                max = atoi(argv[1]);

        for (i = 0; i < max; i++)
                printf("dog[%d]: '%c'\n", i, dog_letter(i));

        return 0;
}
