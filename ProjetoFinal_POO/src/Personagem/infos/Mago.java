package Personagem.infos;

/**
 * importa as classes do pacote Poderes
 */
import Personagem.acoes.SoltarMagia;
import Personagem.poderes.*;

import java.util.ArrayList;

public class Mago extends Classe implements SoltarMagia {


    Magia magiaInicial;
    Raca raca;
    ArrayList<Magia> magias = new ArrayList();
    private String arma;
    private String elemento;

    /**
     *
     * @param magiaInicial a primeira magia aprendida pelo mago
     * @param arma  um foco para canalizar magias
     * @param elemento o elemento que o mago domina
     */

    public Mago(Magia magiaInicial,String arma, String elemento, Raca raca)
    {
        this.raca = raca;
        magias.add(magiaInicial);
        this.setArma(arma);
        this.setElemento(elemento);
    }


    public void addMagia(Magia magia)
    {
        magias.add(magia);
    }
    public ArrayList<Magia> getMagias()
    {
        return magias;
    }

    public String getArma() {
        return arma;
    }

    @Override
    public void SoltarMagia(Magia magia) {
        if(magia.getDano() == 0)
        {
            System.out.println("----------------------------");
            System.out.println("O mago usou: " + magia.getNome() + "\n" +
                    "Efeito: " + magia.getEfeito() + "\n" +
                    "Descricao: " + magia.getDescricao());
            System.out.println("----------------------------");
        }else {
            System.out.println("----------------------------");
            System.out.println("O mago lanca a magia " + magia.getNome() + " causando "
            + magia.getDano() + " pontos de dano no seu inimigo");
            System.out.println("----------------------------");
        }
    }

    public void setArma(String arma) {
        this.arma = arma;
    }

    public String getElemento() {
        return elemento;
    }

    public void setElemento(String elemento) {
        this.elemento = elemento;
    }

    public ArrayList<Magia> getMagia()
    {
        return magias;
    }


}
