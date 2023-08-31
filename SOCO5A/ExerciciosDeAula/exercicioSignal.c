/*
Elabore um programa que a cada 5 segundos exiba na tela a mensagem
"dentro de um loop". Quando o usuáro digitar CTRL_C o programa deverá
exibir uma mensagem "saindo..." e sair do programa. OBS: Não use nada
que não seja da API POSX.
 */

#include <unistd.h> //biblioteca do write
#include <stdbool.h>
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

void alarme(int signum){
    write(1, "Dentro de um loop!\n", 19);
}

void ctrl_c(int signum){
    write(1, "Parando!\n", 9);
    exit(0);
}

int main()
{
    
    signal(SIGALRM, alarme);
    signal(SIGINT, ctrl_c);

    while(1){
        alarm(1);
        pause();
    }

}
