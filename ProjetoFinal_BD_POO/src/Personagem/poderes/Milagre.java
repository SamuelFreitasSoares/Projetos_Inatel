package Personagem.poderes;

public class Milagre extends Magia{
    private String descricao;

    public Milagre(String nome, String efeito, double dano, String descricao) {
        super(nome, efeito, dano,descricao);

    }


    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

}
