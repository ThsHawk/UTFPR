/*
Exercicio 7
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio07;

public class Time {
    
    private Integer hora;
    private Integer minuto;
    public final Integer timeInMinutes;

    public Time(){
        this.hora = 0;
        this.minuto = 0;
        this.timeInMinutes = 0;
    
    }

    public Time(Integer h, Integer m){
        this.hora = h;
        this.minuto = m;
        this.timeInMinutes = h * 60 + m;
    }

    public String toString(){
        return this.hora + "h" + this.minuto;
    }

}
