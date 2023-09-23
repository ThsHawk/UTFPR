/*
Exibe msg na posição x e y do console
Utilize os caracteres de escape "\033[ B\033[ C" para montar as mensagens a serem escritas:
*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

void myPrint(int x, int y, char *msg){
    char escape[] = "\033[ B\033[ CS";
    escape[2] = x + '0';
    escape[6] = y + '0';

    write(1, escape, 9);
    write(1, msg, 50);
}

int main()
{
    char msg[50];
    write(1, "Digite algo: ", 13);
    read(0, msg, 50);
    myPrint(5, 5, msg);
    return 0;
}
