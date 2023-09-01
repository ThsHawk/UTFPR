/*
Exercicio 7
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio07;

import java.util.Random;

public class Descobrir {

    private Integer bound;
    
    public Descobrir(Integer i){
        this.bound = i;
    }

    public Integer genFuncionarioDoMes(){
        return (new Random()).nextInt(this.bound);
    }
    
}
