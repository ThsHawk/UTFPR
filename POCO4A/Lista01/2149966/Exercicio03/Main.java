/*
Exercicio 3
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio03;

public class Main {

    private static EmpresaViagem empresa1;
    private static EmpresaViagem empresa2;

    public static void main(String[] args) {

        empresa1 = new EmpresaViagem();

        empresa1.setNome("Paloma");
        empresa1.setEndereco("Perto do mercado Amigao");
        empresa1.setProprietario("Um cara rico");
        empresa1.setVendasMensais(666.6f);
        empresa1.setQtdeMaxPassagens(100);
        empresa1.setQtdeFuncionarios(7);
        Onibus onibus1 = new Onibus();
        onibus1.setQtdePassageiros(40);
        onibus1.setTipo("Grande");
        empresa1.setOnibus(onibus1);

        empresa2 = new EmpresaViagem();
        
        empresa2.setNome("Paloma2");
        empresa2.setEndereco("Perto do mercado Amigao2");
        empresa2.setProprietario("Um cara rico2");
        empresa2.setVendasMensais(666.2f);
        empresa2.setQtdeMaxPassagens(200);
        empresa2.setQtdeFuncionarios(8);
        Onibus onibus2 = new Onibus();
        onibus2.setQtdePassageiros(42);
        onibus2.setTipo("Maior");
        empresa2.setOnibus(onibus2);

        
        System.out.println("\nNome: " + empresa1.getNome());
        System.out.println("Endereco: " + empresa1.getEndereco());
        System.out.println("Dono: " + empresa1.getProprietario());
        System.out.println("Vendas: " + empresa1.getVendasMensais());
        System.out.println("Passagens: " + empresa1.getQtdeMaxPassagens());
        System.out.println("Funcionarios: " + empresa1.getQtdeFuncionarios());
        System.out.println("Passageiros: " + empresa1.getOnibus().getQtdePassageiros());
        System.out.println("Tipo do onibus: " + empresa1.getOnibus().getTipo()); 
        System.out.println(empresa1.getClass());
        
        
        System.out.println("\nNome: " + empresa2.getNome());
        System.out.println("Endereco: " + empresa2.getEndereco());
        System.out.println("Dono: " + empresa2.getProprietario());
        System.out.println("Vendas: " + empresa2.getVendasMensais());
        System.out.println("Passagens: " + empresa2.getQtdeMaxPassagens());
        System.out.println("Funcionarios: " + empresa2.getQtdeFuncionarios());
        System.out.println("Passageiros: " + empresa2.getOnibus().getQtdePassageiros());
        System.out.println("Tipo do onibus: " + empresa2.getOnibus().getTipo());
        System.out.println(empresa2.getClass());

    }    
}
