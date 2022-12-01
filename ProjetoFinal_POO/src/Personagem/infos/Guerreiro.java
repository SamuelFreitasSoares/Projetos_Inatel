package Personagem.infos;
/**
 * importando as classes do pacote Poderes
 * e interfaces do pacote açoes
 */
import Personagem.poderes.*;
import Personagem.acoes.*;
import java.util.ArrayList;

public class Guerreiro extends Classe implements UsarHabilidade{
    Habilidade habInicial;
    Raca raca;
    private String arma;
    private String armadura;
    ArrayList<Habilidade> habilidades = new ArrayList<>();

    /**[
     *
     * @param habInicial a primeira habilidade de um guerreiro
     * @param arma sua fiél companheira em batalha
     * @param armadura pode te dar uma segunda chance de viver
     */

    public Guerreiro(Habilidade habInicial, String arma, String armadura, Raca raca)
    {
        this.raca = raca;
        habilidades.add(habInicial);
        this.setArma(arma);
        this.setArmadura(armadura);
    }

    public void addHabilidades(Habilidade habilidade)
    {
        habilidades.add(habilidade);
    }

    public String getArma() {
        return arma;
    }

    public void setArma(String arma) {
        this.arma = arma;
    }

    @Override
    public void UsarHabilidade(Habilidade habilidade) {
        if (habilidade.getDano() == 0)
        {
            System.out.println("----------------------------");
            System.out.println("O guerreiro usou: " + habilidade.getNome() + "\n" +
                    "Efeito: " + habilidade.getEfeito() + "\n" +
                    "Descricao: " + habilidade.getDescricao());
            System.out.println("----------------------------");
        }else {
            System.out.println("----------------------------");
            System.out.println("O guerreiro ataca com a habilidade: " + habilidade.getNome() + " - causando "
                    + habilidade.getDano() + " pontos de dano no seu oponente");
            System.out.println("----------------------------");
        }
    }

    public String getArmadura() {
        return armadura;
    }

    public void setArmadura(String armadura) {
        this.armadura = armadura;
    }



    public ArrayList<Habilidade> getHabilidades()
    {
        return habilidades;
    }

}
