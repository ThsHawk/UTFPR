//Crie um processo para printar na tela uma lista de processos em execução no sistema.
//DICA : usar o programa ps

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(){
    execl("/bin/ps", "-aux", NULL);
    return 0;
}