/*
Exercicio 5
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio05;

import java.util.Scanner;

public class Main {

    private static EmpresaViagem empresa;

    public static void main(String[] args) {

        empresa = new EmpresaViagem();

        Scanner scan = new Scanner(System.in);

        System.out.print("Nome da empresa: ");
        empresa.setNome(scan.nextLine());        
        System.out.print("Onde fica: ");
        empresa.setEndereco(scan.nextLine());
        System.out.print("Quem é o dono: ");
        empresa.setProprietario(scan.nextLine());
        System.out.print("Qual é a receita mensal: ");
        empresa.setVendasMensais(scan.nextFloat());
        System.out.print("Quantas passagens a empresa vende: ");
        empresa.setQtdeMaxPassagens(scan.nextInt());
        System.out.print("Tem quantos fucionarios: ");
        empresa.setQtdeFuncionarios(scan.nextInt());
        System.out.print("Quantos passageiros cabem no onubus: ");
        Integer i = scan.nextInt();
        System.out.print("Qual o tipo do onibus: ");
        String s = scan.nextLine();
        s = scan.nextLine();
        scan.close();
        empresa.setOnibus(i, s);

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
