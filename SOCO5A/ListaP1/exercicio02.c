/*A partir da rotina main descrita a seguir;

int main(int argc, char *argv[])
{

    while (1)
        return 0;
}

faça Um procedimento para contar o número de vezes que o usuário enviou o sinal
SIGINT para o processo em execução.Pressionar Ctl - C no teclado envia esse sinal.
Quando o processo recebe o sinal SIGTSTP(Ctl - Z), ele deve imprimir no terminal
o número de sinais SIGINT que recebeu.Depois de receber 3 sinais SIGINT, o programa
deve perguntar se o usuário deseja sair do programa.Se o usuário não responder em
20 segundos, um sinal SIGALRM deve forçar a saída do programa.

Faça o programa de acordo com o exemplo de saída a seguir :

bash >./ ex ^ C ^ C ^ C Realmente deseja sair
? [Y / n]
: n

Continuando... ^
C ^ Z

Você apertou Ctl
- C '1' vezes

^ C ^ Z

Você apertou Ctl
- C '2' vezes

^ C Realmente deseja sair
? [Y / n]
: n

Continuando... ^
C ^ C ^ C Realmente deseja sair
? [Y / n]
: Demorou muito para responder.Saindo......*/

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int count;

void ctrlC(int signum){
    count++;
    if(count == 3){
        write(1, "Deseja sair?\n", 13);
        alarm(20);
        char *opt = (char *)malloc(1 * sizeof(char));
        read(0, opt, 1);
        if(*opt == 'y'){
            exit(0);
        }else{
            count = 0;
        }
    }
}

void ctrlZ(int signum){
    write(1, "CTRL-C pressionado ", 19);
    char c = count + '0';
    write(1, &c, 1);
    write(1, " vezes.\n", 8);
}

void alarme(int signum){
    if(count == 3){
        write(1, "Saindo...", 9);
        exit(0);
    }
}

int main(){
    count = 0;

    signal(SIGINT, ctrlC);
    signal(SIGTSTP, ctrlZ);
    signal(SIGALRM, alarme);

    while(1);
    return 0;
}