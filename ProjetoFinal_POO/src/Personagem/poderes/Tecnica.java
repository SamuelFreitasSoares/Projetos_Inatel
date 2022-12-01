package Personagem.poderes;

public class Tecnica extends Habilidade{
    private String descricao;

    public Tecnica(String nome, String efeito, double dano, String descricao) {
        super(nome, efeito, dano,descricao);
    }


    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
}
