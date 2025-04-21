#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "../lib/menu.h"
#include "../lib/strings_func.h"
#include <limits.h>
#include <float.h>

#define MAX_STRING CHAR_MAX

void showMenu() {
    printf("Dentro menu...\n");
    char input[MAX_STRING + 1] = {0};
    bool rodando = true;

    while (rodando) {
        printf("\n--- Menu ---\n");
        printf("1. Inserir uma string\n");
        printf("2. Transformar em maiúsculas\n");
        printf("3. Transformar em minúsculas\n");
        printf("4. Remover espaços extras\n");
        printf("5. Capitalizar palavras\n");
        printf("6. Exibir limites da linguagem C\n");
        printf("7. Sair\n");
        printf("Escolha uma opção: ");

        int opcao;
        if (scanf("%d", &opcao) != 1) {
            printf("Entrada inválida!\n");
            while (getchar() != '\n');
            continue;
        }
        getchar();

        switch (opcao) {
            case 1:
                printf("Digite sua string (máx. %d caracteres): ", MAX_STRING);
                fgets(input, sizeof(input), stdin);
                input[strcspn(input, "\n")] = '\0';
                break;
            case 2:
                uppercase(input);
                printf("Resultado: %s\n", input);
                break;
            case 3:
                lowercase(input);
                printf("Resultado: %s\n", input);
                break;
            case 4:
                trimSpaces(input);
                printf("Resultado: %s\n", input);
                break;
            case 5:
                capitalize(input);
                printf("Resultado: %s\n", input);
                break;
            case 6:
                exibirLimites();
                break;
            case 7:
                rodando = false;
                break;
            default:
                printf("Opção inválida!\n");
        }
    }
}

void exibirLimites() {
    printf("\n--- Limites Inteiros ---\n");
    printf("INT_MAX: %d\n", INT_MAX);
    printf("INT_MIN: %d\n", INT_MIN);
    printf("CHAR_MAX: %d\n", CHAR_MAX);
    printf("CHAR_MIN: %d\n", CHAR_MIN);

    printf("\n--- Limites de Ponto Flutuante ---\n");
    printf("FLT_MAX: %e\n", FLT_MAX);
    printf("FLT_MIN: %e\n", FLT_MIN);
    printf("DBL_MAX: %e\n", DBL_MAX);
    printf("DBL_MIN: %e\n", DBL_MIN);
}
