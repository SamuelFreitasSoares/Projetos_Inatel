package Personagem.poderes;

public abstract class Truque {
    private String nome;
    private double dano;
    private String efeito;
    private String descricao;

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public Truque(String nome, String efeito, double dano, String descricao)
    {
        this.setDescricao(descricao);
        this.setDano(dano);
        this.setEfeito(efeito);
        this.setNome(nome);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getDano() {
        return dano;
    }

    public void setDano(double dano) {
        this.dano = dano;
    }

    public String getEfeito() {
        return efeito;
    }

    public void setEfeito(String efeito) {
        this.efeito = efeito;
    }
    @Override
    public String toString() {
        return nome ;
    }
}
