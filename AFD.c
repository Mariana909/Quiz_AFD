#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void afd(const char *entrada) {
    int q = 0; // Estado inicial q0

    for (int i = 0; entrada[i] != '\0'; i++) {
        char n = entrada[i];

        if (q == 0) {
            if (isupper(n))      q = 3;
            else if (n == '+')   q = 1;
            else                 { q = 6; break; }
        }
        else if (q == 1) {
            if (n == '+')        q = 2;
            else                 { q = 6; break; }
        }
        else if (q == 3) {
            if (isupper(n))      q = 3;
            else if (islower(n)) q = 4;
            else if (isdigit(n)) q = 5;
            else                 { q = 6; break; }
        }
        else if (q == 4) {
            if (islower(n))      q = 4;
            else if (isdigit(n)) q = 4;
            else                 { q = 6; break; }
        }
        else if (q == 5) {
            if (islower(n))      q = 4;
            else if (isdigit(n)) q = 5;
            else                 { q = 6; break; }
        }
        else {
            q = 6;
            break;
        }
    }

    if      (q == 1)                    printf("SUMA\n");
    else if (q == 2)                    printf("INCR\n");
    else if (q == 3 || q == 4 || q == 5) printf("ID\n");
    else                                printf("NO ACEPTA\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("No se detectó archivo de entrada\n");
        return 1;
    }

    FILE *archivo = fopen(argv[1], "r");
    if (archivo == NULL) {
        printf("No se encontró el archivo\n");
        return 1;
    }

    char token[256];
    while (fscanf(archivo, "%255s", token) == 1) {
        afd(token);
    }

    fclose(archivo);
    return 0;
}
