/*
Excrever um programa C que cria uma árvore de 3 processos, onde o processo A
faz um fork() criando um processo B, o processo B, por sua vez, faz um fork()
criando um processo C.Cada processo deve exibir uma mensagem "Eu sou o processo
XXX, filho de YYY", onde XXX e YYY são PIDs de processos.Utilizar wait() para
garantir que o processo C imprima sua resposta antes do B, e que o processo B
imprima sua resposta antes do A.Utilizar sleep()(man 3 sleep) para haver um
intervalo de 1 segundo entre cada mensagem impressa.
*/

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(){

    int pid, status;
    
    printf("iniciando...\n\n");
    pid = fork();

    if (pid < 0){
        printf("\n\nerro\n\n");
        exit(0);
    }else if(pid == 0){
        pid = fork();
        if (pid == 0){
            printf("proc %d filho de %d\n", getpid(), getppid());
        }else if(pid > 0){
            wait(&status);
            printf("proc %d filho de %d\n", getpid(), getppid());
        }
    }else{
        wait(&status);
        printf("proc %d - i am yor fader\n", getpid());
        return 0;
    }
}