/* Implemente uma calculadora em POO */

package POCO4A.Aula03;

public class Calc{

    private String brand;
    private String model;

    Calc(){
        this.brand = "";
        this.model = "";
    }

    public float add(float a, float b){
        return a + b;
    }
    public float sub(float a, float b){
        return a - b;
    }
    public float mul(float a, float b){
        return a * b;
    }
    public float div(float a, float b){
        return a / b;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getBrand() {
        return brand;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getModel() {
        return model;
    }

}