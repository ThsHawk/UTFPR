/*
Exercicio 4
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio04;

public class Main {

    private static EmpresaViagem empresa;

    public static void main(String[] args) {

        empresa = new EmpresaViagem();

        empresa.setNome("Paloma");
        empresa.setEndereco("Perto do mercado Amigao");
        empresa.setProprietario("Um cara rico");
        empresa.setVendasMensais(666.6f);
        empresa.setQtdeMaxPassagens(100);
        empresa.setQtdeFuncionarios(7);
        empresa.setOnibus(40, "Grande");

        System.out.println("\nNome: " + empresa.getNome());
        System.out.println("Endereco: " + empresa.getEndereco());
        System.out.println("Dono: " + empresa.getProprietario());
        System.out.println("Vendas: " + empresa.getVendasMensais());
        System.out.println("Passagens: " + empresa.getQtdeMaxPassagens());
        System.out.println("Funcionarios: " + empresa.getQtdeFuncionarios());
        System.out.println("Passageiros: " + empresa.getOnibus().getQtdePassageiros());
        System.out.println("Tipo do onibus: " + empresa.getOnibus().getTipo());

    }    
}
