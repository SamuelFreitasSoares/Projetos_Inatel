package Personagem.poderes;

public class Vil extends Truque{
        private String descricao;

        public Vil(String nome, String efeito, double dano, String descricao) {
            super(nome, efeito, dano,descricao);

        }


        public String getDescricao() {
            return descricao;
        }

        public void setDescricao(String descricao) {
            this.descricao = descricao;
        }
    }


