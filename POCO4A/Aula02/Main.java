package POCO4A.Aula02;

public class Main {

    public static void main(String[] args) {
        
        Calc calc1 = new Calc();

        System.out.println(calc1.add(2, 1));//3
        System.out.println(calc1.sub(2, 1));//1
        System.out.println(calc1.mul(2, 2));//4
        System.out.println(calc1.div(10, 2));//5

    }
    
}
