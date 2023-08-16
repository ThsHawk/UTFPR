package POCO4A.Aula03;

public class Main {

    public static void main(String[] args) {

        Calc hp = new Calc();
        Calc samsung = new Calc();

        hp.setBrand("HP");
        hp.setModel("51g");

        samsung.setBrand("Samsung");
        samsung.setModel("X");
        
        System.out.println("Calculadora: " + hp.getBrand());
        System.out.println("Modelo: " + hp.getModel());
        System.out.println("2 + 2 = " + hp.add(2, 2));
        
        System.out.println("Calculadora: " + samsung.getBrand());
        System.out.println("Modelo: " + samsung.getModel());
        System.out.println("2 + 2 = " + samsung.add(2, 2));
        
    }
    
}
