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

    long int inteiro;
    char * msg = (char *) malloc(20*sizeof(char));

    //Teste read/write
    read(0, msg, 20);
    write(1, msg, 20);
   
    //para os alunos estudarem os tamanhos dos tipos de dados pedir nome
    //e RA por exemplo
    write(1, "Digite seu primeiro nome: ", 26);
    read(0, msg, 15);
    write(1, "Digite seu RA: ", 15);
    read(0, &inteiro, 7);

    //Print
    write(1, "\n\n", 2);    
    write(1, "Nome: ", 6);    
    write(1, msg, 15);    
    write(1, "RA: ", 4);    
    write(1, &inteiro, 7);   
}