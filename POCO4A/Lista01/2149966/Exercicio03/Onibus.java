/*
Exercicio 3
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio03;

public class Onibus {
    
    private Integer qtdePassageiros;
    private String tipo;

    public Onibus(){
        this.qtdePassageiros = 0;
        this.tipo = "";
    }

    public void setQtdePassageiros(Integer qtdePassageiros) {
        this.qtdePassageiros = qtdePassageiros;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public Integer getQtdePassageiros() {
        return qtdePassageiros;
    }
    public String getTipo() {
        return tipo;
    }
}
