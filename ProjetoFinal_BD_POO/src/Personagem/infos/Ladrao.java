package Personagem.infos;
/**
 * importando as classes do pacote Poderes
 * e a interface UsarTruque
 */

import Personagem.acoes.UsarTruque;
import Personagem.poderes.*;

import java.util.ArrayList;

public class Ladrao extends Classe implements UsarTruque {
    Truque truqueInicial;
    Raca raca;
    private String arma;
    private String acessorio;
    ArrayList<Truque> truques = new ArrayList();

    /**
     *
     * @param truqueInicial a primeira habilidade que o ladrao aprendeu
     * @param acessorio um charme que afeta suas habilidades de alguma maneira
     * @param arma uma companheira para as missoes perigosas
     */

    public Ladrao(Truque truqueInicial, String acessorio, String arma, Raca raca)
    {
        this.raca = raca;
        truques.add(truqueInicial);
        this.setAcessorio(acessorio);
        this.setArma(arma);
    }

    public void addTruque(Truque truque)
    {
        truques.add(truque);
    }



    @Override
    public void UsarTruque(Truque truque) {
        if(truque.getDano() == 0)
        {
            System.out.println("----------------------------");
            System.out.println("O ladino usou: " + truque.getNome() + "\n" +
                    "Efeito: " + truque.getEfeito() + "\n" +
                    "Descricao: " + truque.getDescricao());
            System.out.println("----------------------------");
        }else {
            System.out.println("----------------------------");
            System.out.println("O ladino sorrateiro usa " + truque.getNome() + " causando "
                    + truque.getDano() + " pontos de dano na sua vitima desavisada");
            System.out.println("----------------------------");
        }
    }

    public ArrayList<Truque> getTruques()
    {
        return truques;
    }

    public String getArma() {
        return arma;
    }

    public void setArma(String arma) {
        this.arma = arma;
    }

    public String getAcessorio() {
        return acessorio;
    }

    public void setAcessorio(String acessorio) {
        this.acessorio = acessorio;
    }

}
