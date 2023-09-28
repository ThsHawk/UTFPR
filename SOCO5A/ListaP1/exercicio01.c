//Faça um programa para disparar uma mensagen de bons estudos
//a cada 10 segundos utilizando a API posix do linux.

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

void alarme(int signum){
    write(1, "Bons Estudos!!\n", 15);
}

void sair(int signum){
    write(1, "Saindo...\n", 10);
    exit(0);
}

int main(){
    signal(SIGALRM, alarme);
    signal(SIGINT, sair);
    while(1){
        alarm(10);
        pause();
    }
}