import Personagem.infos.*;
import Personagem.poderes.*;

import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        int auxm = 0;
        String efx = null;
        String dsc = null;
        double dmg = 0;
        String nome = null;
        Humano humano = new Humano(13, 12, 16, 10, 14, 10);
        Demonio rakshasa = new Demonio(20, 20, 10, 10, 15, 18);
        Elfo aelyd = new Elfo(10, 10, 20, 25, 18, 24);

        Vil assassin1 = new Vil("Adaga Sombria", "aplica o debuff 'slowness' e causa dano",
                15, "Conjura uma adaga tecida das sombras, capaz de cortar ferro como se fosse manteiga e a lanca em direcao a um inimigo");
        Vil assassin2 = new Vil("Fumaca Negra", "aplica o debuff 'Blindness'", 0, "Manipula as sombras ao seu redor para criar uma cortina de " +
                "fumaca que cega temporariamente seu inimigo");
        Vil assassin3 = new Vil("Andar das Sombras", "Teleporte de curta distancia", 0, "Mergulhe nas sombras ao seu redor e reapareca a uma curta distancia em outra " +
                "sombra (obs: a sombra precisa ser maior que o personagem tanto para entrar quanto para sair)");

        Sagacidade ladino1 = new Sagacidade("Distracao", "diminui o nivel de alerta das pessoas ao seu redor", 0, "Cria uma distracao usando pequenos explosivos " +
                "caseiros que podem ser detonados remotamente para produzir barulho");
        Sagacidade ladino2 = new Sagacidade("Presa Venenosa", "causa DoT (Damage over Time) no alvo selecionado", 10, "Manifesta uma lamina ilusoria coberta " +
                "de veneno que desaparece apos o uso");
        Sagacidade ladino3 = new Sagacidade("Lingua Prateada", "aumenta a oratoria em 10 pontos por 5 turnos", 0, "suas palavras parecem serem feitas de mel " +
                "tornando-as mais efetivas em negociacoes, intimidacoes e barganhas");

        Feitico warlock1 = new Feitico("Lanca do Trovao", "causa dano elemental e pode atordoar o alvo", 30, "Manipula o ether do trovao na atmosfera " +
                "e conjura uma lanca para obliterar seus inimigos");
        Feitico warlock2 = new Feitico("Escudo de Ether", "bloqueia projeteis e aumenta a defesa magica", 0, "Conjura um escudo em formato de bolha ao seu redor " +
                "feito de puro ether, impedindo projeteis que causem menos de 3d12 de dano a atravessarem");
        Feitico warlock3 = new Feitico("Conjurar Elemental", "conjura um elemental da sua escolha para lutar", 50, "Utilizando de circulos magicos e manipulacao" +
                " elemental, invoca da dimensao primordial um Guardiao Elemental (habilidades dependem do elemento)");

        Milagre clerigo1 = new Milagre("Luz divina", "cura aliados e machuca inimigos", 15, "Suplica pela Luz de Magnus para que queime seus inimigos e " +
                "rejuveneca seus aliados (cura por 3x o dano)");
        Milagre clerigo2 = new Milagre("Empoderar", "aumenta o dano e resistencia de aliados", 0, "Atraves da sua fe, Magnus abencoa seus aliados, fortalencendo " +
                "seus poderes");
        Milagre clerigo3 = new Milagre("Sacrificio", "sacrifica sua vida e de aliados para causar dano massivo", 100, "Magnus e a luz que guia mas tambem o fogo " +
                "que destroi. Sacrifique ate 99% da sua vida e de aliados para garantir que a furia de Magnus desintegre os pagaos. (quanto mais vida sacrificada, maior o dano)");

        Tecnica tecnica1 = new Tecnica("Mordida de Dragao", "causa dano e tem chance de causar o debuff 'Fear'", 18, "Apos observar um dragao mordendo um inimigo, " +
                "voce se inspirou para criar uma tecnica que imita sua ferocidade e grandeza");
        Tecnica tecnica2 = new Tecnica("Avanco", "receba um aumento explosivo de velocidade por 1,5s", 0, "Circulando ether pelos musculos, veias e arterias " +
                "voce consegue atingir niveis absurdos de velocidade porem e mais facil perder o controle e romper sua carne, nao podendo manter por muito tempo");
        Tecnica tecnica3 = new Tecnica("Punicao Divina", "causa dano massivo em alvos identificados como 'Pecadores'", 45, "Sendo a tecnica suprema utilizada " +
                "pelos paladinos da igreja do Sol, e capaz de obliterar exercitos barbaros inteiros");

        Brutalidade brutalidade1 = new Brutalidade("Corte", "causa dano e aplica sangramento", 30, "Esqueca tudo: tecnicas, magias, truques. Diante da sua lamina " +
                "tudo isso nao passa da resistencia dos fracos");
        Brutalidade brutalidade2 = new Brutalidade("Soco", "causa dano", 40, "Armas? Quem precisa disso? - Concentre toda sua furia e seu poder na palma " +
                "da sua mao e destrua todos os obstaculos");
        Brutalidade brutalidade3 = new Brutalidade("-BERSERK-", "???", 99999, "Des??rte a e??uridao em seu cor??ao e de?xa-a to??r con?a para rec??er: ???????????????");

        Mago merlin = new Mago(warlock2, "Cajado de Pastor", "Fogo", humano);
        Guerreiro sabbac = new Guerreiro(tecnica1, "LightBane", "HellRaiser", rakshasa);
        Ladrao robin = new Ladrao(ladino3, "Amuleto de Nocturnal", "Shadow Viper", aelyd);

        merlin.addMagia(warlock1);
        merlin.addMagia(warlock3);

        sabbac.addHabilidades(brutalidade2);
        sabbac.addHabilidades(brutalidade3);

        robin.addTruque(assassin2);
        robin.addTruque(assassin3);

        PrintWriter gravarArq1;
        PrintWriter gravarArq2;
        PrintWriter gravarArq3;
        try {
            FileWriter arq1 = new FileWriter("C://Users//samue//OneDrive//Documentos//merlin.txt");
            FileWriter arq2 = new FileWriter("C://Users//samue//OneDrive//Documentos//sabbac.txt");
            FileWriter arq3 = new FileWriter("C://Users//samue//OneDrive//Documentos//robin.txt");
            gravarArq1 = new PrintWriter(arq1);
            gravarArq2 = new PrintWriter(arq2);
            gravarArq3 = new PrintWriter(arq3);
            gravarArq1.println("Nome : Merlin " + "\n"
                    + "Arma: " + merlin.getArma() + "\n"
                    + "Elemento: " + merlin.getElemento() + "\n"
                    + "Magias: " + merlin.getMagias());
            gravarArq2.println("Nome : Sabbac " + "\n"
                    + "Arma: " + sabbac.getArma() + "\n"
                    + "Armadura: " + sabbac.getArmadura() + "\n"
                    + "Habilidades: " + sabbac.getHabilidades());
            gravarArq3.println("Nome : Robin Hood " + "\n"
                    + "Arma: " + robin.getArma() + "\n"
                    + "Acessorio: " + robin.getAcessorio() + "\n"
                    + "Truques: " + robin.getTruques());
            arq1.close();
            arq2.close();
            arq3.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }





        System.out.println("Escolha um personagem: 1-Merlin  2-Sabbac  3-Robin 4-Sair");
        Scanner scanner = new Scanner(System.in);
        int aux = Integer.parseInt(scanner.nextLine());
        while (aux != 4) {
            if (aux == 1) {
                while (auxm != 4) {
                    System.out.println("Escolha uma opcao: 1-Soltar Magia 2-adicionar magia 3-infos 4-Voltar");
                    auxm = Integer.parseInt(scanner.nextLine());

                    if (auxm == 1) {
                        merlin.SoltarMagia(warlock2);
                    }
                    else if (auxm == 2) {
                        System.out.println("Voce so pode adicionar uma magia extra entao tome cuidado");
                        System.out.println("Descreva a magia com Nome -> Efeito -> Dano -> Descricao");
                        nome = scanner.nextLine();
                        efx = scanner.nextLine();
                        dmg = Double.parseDouble(scanner.nextLine());
                        dsc = scanner.nextLine();
                        Feitico adicional1 = new Feitico(nome, efx, dmg, dsc);
                        merlin.addMagia(adicional1);
                        try {
                            FileWriter arq1 = new FileWriter("C://Users//samue//OneDrive//Documentos//merlin.txt");
                            gravarArq1 = new PrintWriter(arq1);
                            gravarArq1.println("Nome : Merlin " + "\n"
                                    + "Arma: " + merlin.getArma() + "\n"
                                    + "Elemento: " + merlin.getElemento() + "\n"
                                    + "Magias: " + merlin.getMagias());
                            arq1.close();
                        } catch (IOException e) {
                            throw new RuntimeException(e);
                        }


                    }
                    else if (auxm == 3) {
                        try {
                            File myObj = new File("C:\\Users\\samue\\OneDrive\\Documentos\\merlin.txt");
                            Scanner myReader = new Scanner(myObj);
                            while (myReader.hasNextLine()) {
                                String data = myReader.nextLine();
                                System.out.println(data);
                            }
                            myReader.close();
                        } catch (FileNotFoundException e) {
                            System.out.println("Ocorreu um erro. Reinicie a aplicação");
                            e.printStackTrace();
                        }

                    }
                    else {
                        System.out.println("Escolha um personagem: 1-Merlin  2-Sabbac  3-Robin 4-Sair");
                        aux = scanner.nextInt();
                    }
                }
            } else if (aux == 2) {
                System.out.println("Escolha uma opcao: 1-Usar Habilidade 2-adicionar Habilidade 3-infos 4-Voltar");
                auxm = scanner.nextInt();
                if (auxm == 1) {
                    sabbac.UsarHabilidade(brutalidade1);
                } else if (auxm == 2) {
                    System.out.println("Voce so pode adicionar uma Habilidade extra entao tome cuidado");
                    System.out.println("Descreva a Habilidade com Nome -> Efeito -> Dano -> Descricao");
                    nome = scanner.nextLine();
                    efx = scanner.nextLine();
                    dmg = scanner.nextDouble();
                    dsc = scanner.nextLine();
                    Tecnica adicional1 = new Tecnica(nome, efx, dmg, dsc);
                    sabbac.addHabilidades(adicional1);
                    try {
                        FileWriter arq2 = new FileWriter("C://Users//samue//OneDrive//Documentos//sabbac.txt");
                        gravarArq2 = new PrintWriter(arq2);
                        gravarArq2.println("Nome : Sabbac " + "\n"
                                + "Arma: " + sabbac.getArma() + "\n"
                                + "Armadura: " + sabbac.getArmadura() + "\n"
                                + "Habilidades: " + sabbac.getHabilidades());
                        arq2.close();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                } else if (auxm == 3){
                    try {
                        File myObj = new File("C:\\Users\\samue\\OneDrive\\Documentos\\sabbac.txt");
                        Scanner myReader = new Scanner(myObj);
                        while (myReader.hasNextLine()) {
                            String data = myReader.nextLine();
                            System.out.println(data);
                        }
                        myReader.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("Ocorreu um erro. Reinicie a aplicação");
                        e.printStackTrace();
                    }
                } else {
                    System.out.println("Escolha um personagem: 1-Merlin  2-Sabbac  3-Robin 4-Sair");
                    aux = scanner.nextInt();
                }
            } else if (aux == 3) {
                System.out.println("Escolha uma opcao: 1-Usar Truque 2-adicionar Truque 3-infos 4-Voltar");
                auxm = scanner.nextInt();
                if (auxm == 1) {
                    robin.UsarTruque(assassin2);
                } else if (auxm == 2) {
                    System.out.println("Voce so pode adicionar um truque extra entao tome cuidado");
                    System.out.println("Descreva o truque com Nome -> Efeito -> Dano -> Descricao");
                    nome = scanner.nextLine();
                    efx = scanner.nextLine();
                    dmg = scanner.nextDouble();
                    dsc = scanner.nextLine();
                    Vil adicional1 = new Vil(nome, efx, dmg, dsc);
                    robin.addTruque(adicional1);
                    try {
                        FileWriter arq3 = new FileWriter("C://Users//samue//OneDrive//Documentos//robin.txt");
                        gravarArq3 = new PrintWriter(arq3);
                        gravarArq3.println("Nome : Robin Hood " + "\n"
                                + "Arma: " + robin.getArma() + "\n"
                                + "Acessorio: " + robin.getAcessorio() + "\n"
                                + "Truques: " + robin.getTruques());
                        arq3.close();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                } else if (auxm == 3){
                    try {
                        File myObj = new File("C:\\Users\\samue\\OneDrive\\Documentos\\robin.txt");
                        Scanner myReader = new Scanner(myObj);
                        while (myReader.hasNextLine()) {
                            String data = myReader.nextLine();
                            System.out.println(data);
                        }
                        myReader.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("Ocorreu um erro. Reinicie a aplicação");
                        e.printStackTrace();
                    }
                } else {
                    System.out.println("Escolha um personagem: 1-Merlin  2-Sabbac  3-Robin 4-Sair");
                    aux = scanner.nextInt();
                }
            } else {
                break;
            }
        }

        System.out.println("Deseja deletar um personagem? 1-Sim  2-Nao");
        int del = scanner.nextInt();
        if(del == 1)
        {
            System.out.println("escolha um personagem para excluir: 1-Merlin  2-Sabbac  3-Robin");
            int pers = scanner.nextInt();
            if (pers == 1)
            {
                File myObj = new File("C:\\Users\\samue\\OneDrive\\Documentos\\merlin.txt");
                if (myObj.delete())
                {
                    System.out.println("Personagem excluido com sucesso: " + myObj.getName());
                    System.out.println("Obrigado por Jogar!!");
                } else
                {
                    System.out.println("Erro na exclusao. Tente novamente");
                }
            } else if (pers == 2) {
                File myObj = new File("C:\\Users\\samue\\OneDrive\\Documentos\\sabbac.txt");
                if (myObj.delete())
                {
                    System.out.println("Personagem excluido com sucesso: "+ myObj.getName());
                    System.out.println("Obrigado por Jogar!!");
                } else
                {
                    System.out.println("Erro na exclusao. Tente novamente");
                }
            }
            else {
                File myObj = new File("C:\\Users\\samue\\OneDrive\\Documentos\\robin.txt");
                if (myObj.delete())
                {
                    System.out.println("Personagem excluido com sucesso: " + myObj.getName());
                    System.out.println("Obrigado por Jogar!!");
                } else
                {
                    System.out.println("Erro na exclusao. Tente novamente");
                }
            }
        }else
        {
            System.out.println("Obrigado por Jogar!!");
        }

    }
}
