/*
Exercicio 9
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio09;

public class Computador {

    public class Data{

        private Integer dia;
        private Integer mes;
        private Integer ano;

        public Data(Integer dia, Integer mes, Integer ano){
            this.dia = dia;
            this.mes = mes;
            this.ano = ano;
        }

    }
    
    private String nome;
    private String marca;
    private Data data;

    public Computador(){
        this.nome = "";
        this.marca = "";
        this.data = null;
    }

    public Computador setNome(String nome) {
        this.nome = nome;
        return this;
    }
    public Computador setMarca(String marca) {
        this.marca = marca;
        return this;
    }    
    public Computador setData(Integer dia, Integer mes, Integer ano) {
        this.data = new Data(dia, mes, ano);
        return this;
    }

    public String toString(){
        return "Nome: " + this.nome +
               "\nMarca: " + this.marca +
               "\nData: " + this.data.dia + "/" + this.data.mes + "/" + this.data.ano;
    }
    
}
