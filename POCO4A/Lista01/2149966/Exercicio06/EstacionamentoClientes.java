/*
Exercicio 6
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio06;

public class EstacionamentoClientes {
    
    private String tipoVeiculo;
    private String placa;
    private Time timeIn;
    private Time timeOut;

    public EstacionamentoClientes(){
        this.tipoVeiculo = "";
        this.placa = "";
        this.timeIn = new Time();
        this.timeOut = new Time();
    }
    
    public EstacionamentoClientes(String tipo, String p){
        this.tipoVeiculo = tipo;
        this.placa = p;
        this.timeIn = new Time();
        this.timeOut = new Time();
    }

    public void opIn(Time t){
        this.timeIn = t;
    }

    public void opOut(Time t){
        this.timeOut = t;
        this.calcPrice();
    }

    private void calcPrice(){
        System.out.println("\n" + this.tipoVeiculo + ", Placa: " + this.placa);
        System.out.println("Entrada: " + this.timeIn.toString());
        System.out.println("Saida: " + this.timeOut.toString());
        Integer time = this.timeOut.timeInMinutes - this.timeIn.timeInMinutes;
        if (time > 60) {
            System.out.println("Total a Pagar: RS20.00");
        } else if (time > 30){
            System.out.println("Total a Pagar: RS10.00");
        } else {
            System.out.println("Total a Pagar: RS00.00");
        }
    }





    

    
}
