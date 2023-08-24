/*
Pesquise o funcionamento das funções read e write da API posix do linux
e faça um programa, usando apenas essas funções para I/O, que receba o
nome e o ra de um aluno e imprima na tela.

OBS: RA não pode ser  uma string
*/

#include <unistd.h> //biblioteca do write
#include <stdbool.h>
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

int main()
{

    //int inteiro;
    char * msg = (char *) malloc(20*sizeof(char));

    read(0, msg, 20);
    //write(1, "Alou Syscall!\n\n",15);

    write(1, msg, 20);
   
    /*//para os alunos estudarem os tamanhos dos tipos de dados pedir nome
    //e RA por exemplo
    read(0, &inteiro , 0);
    read(0, msg , 20);

    write(1, "\n\n",2);    
    
    write(1, &inteiro, 4);    
    
    write(1, "\n\n",2);
    write(1, msg, 20);
*/
    write(1, "\n\n",2);    
    char c;
    while (read(0, c, sizeof(char)) > 0);
    //msg = "teste";
    read(0, msg, 20);
    write(1, msg, 20);
}