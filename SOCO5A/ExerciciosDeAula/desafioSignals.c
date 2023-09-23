/*
 A partir da rotina main descrita a seguir;

int main(int argc, char* argv[])
{ 
  while(1)   
  return 0;
}

faça:
Um procedimento para contar o número de vezes que o usuário enviou o sinal
SIGINT para o processo em execução. Pressionar Ctl-C no teclado envia esse
sinal. Quando o processo recebe o sinal SIGTSTP (Ctl-Z), ele deve imprimir
no terminal o número de sinais SIGINT que recebeu. Depois de receber 3 sinais
SIGINT, o programa deve perguntar se o usuário deseja sair do programa. Se
o usuário não responder em 20 segundos, um sinal SIGALRM deve forçar a saída
do programa.
*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int ctrlC = 0;

void alarme(int signum){
    write(1, "E a demora?\n", 12);
    exit(0);
}

void ctrl_c(int signum){
    ctrlC++;
    
    if (ctrlC == 3){
        ctrlC = 0;
        signal(SIGALRM, alarme);
        alarm(20);
        
        write(1, "\nDeseja Sair? (s/n)", 19);
        char *c = (char *)malloc(1 * sizeof(char));
        read(0, c, 1);
        //read(0, c, 1);
        
        alarm(0);
        if(*c != 'n'){
            write(1, "Saindo", 6);
            exit(0);
        }
    }
}

void ctrl_z(int signum){
    char *c = (char *)malloc(1 * sizeof(char));
    *c = ctrlC + '0';
    write(1, "\n\nCtrl C digitado ", 18);
    write(1, c, 1);
    write(1, " vezes\n", 7);    
}

int main(int argc, char* argv[])
{ 
    signal(SIGINT, ctrl_c);
    signal(SIGTSTP, ctrl_z);
    
    while(1);
    return 0;
}
