#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 1;
    }

    int max_len, k = 0;

    while (argv[++k])
    {
    max_len = 0;
    char *cpy = strdup(argv[k]);
    char *word = strtok(cpy, " ");
    while (word != NULL) {
        int len = strlen(word);
        if (len > max_len) {
            max_len = len;
        }
        word = strtok(NULL, " ");
    }
    free(cpy);
    for (int i = 0; i < max_len + 4; i++) {
        printf("*");
    }
    printf("\n");
    strtok(NULL, " ");
    cpy = strdup(argv[k]);
        char *word2 = strtok(cpy, " ");
        while (word2 != NULL) {
            int len = strlen(word2);
            printf("* %s", word2);
            for (int k = 0; k < max_len - len; k++) {
                printf(" ");
            }
            printf(" *\n");
            word2 = strtok(NULL, " ");
        }
    free(cpy);
    for (int i = 0; i < max_len + 4; i++) {
        printf("*");
    }
    printf("\n");
    }
    return 0;
}
