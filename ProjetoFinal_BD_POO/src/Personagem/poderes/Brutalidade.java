package Personagem.poderes;

public class Brutalidade extends Habilidade{
    private String descricao;

    public Brutalidade(String nome, String efeito, double dano, String descricao) {
        super(nome, efeito, dano, descricao);
    }


    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
}
