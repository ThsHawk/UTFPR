/*
Exercicio 7
Autor: Thales Alves 
Data: 31/08/23
*/

package Exercicio07;

public class EmpresaViagem {

    private String nome;
    private String proprietario;
    private String endereco;
    private Float vendasMensais;
    private Integer qtdeMaxPassagens;
    private Integer qtdeFuncionarios;
    private Onibus onibus;

    public EmpresaViagem(){
        this.nome = "";
        this.proprietario = "";
        this.endereco = "";
        this.vendasMensais = 0f;
        this.qtdeMaxPassagens = 0;
        this.qtdeFuncionarios = 0;
        this.onibus = null;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setProprietario(String proprietario) {
        this.proprietario = proprietario;
    }
    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
    public void setVendasMensais(Float vendasMensais) {
        this.vendasMensais = vendasMensais;
    }
    public void setQtdeMaxPassagens(Integer qtdeMaxPassagens) {
        this.qtdeMaxPassagens = qtdeMaxPassagens;
    }
    public void setQtdeFuncionarios(Integer qtdeFuncionarios) {
        this.qtdeFuncionarios = qtdeFuncionarios;
    }
    public void setOnibus(Onibus onibus) {
        this.onibus = onibus;
    }
    public void setOnibus(Integer qtdePassageiros, String tipo) {
        this.onibus = new Onibus(qtdePassageiros, tipo);
    }

    public String getNome() {
        return nome;
    }
    public String getProprietario() {
        return proprietario;
    }
    public String getEndereco() {
        return endereco;
    }
    public Float getVendasMensais() {
        return vendasMensais;
    }
    public Integer getQtdeMaxPassagens() {
        return qtdeMaxPassagens;
    }
    public Integer getQtdeFuncionarios() {
        return qtdeFuncionarios;
    }
    public Onibus getOnibus() {
        return onibus;
    }
}
