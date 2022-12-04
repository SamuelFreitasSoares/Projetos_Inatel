package Personagem.infos;

public abstract class Raca {
    /**
     * criando variaveis para os atributos dos personagens:
     *
     * Str = Strength
     * Vit = Vitality
     * Int = Intelligence
     * Spt = Spirit
     * Agi = Agility
     * Spd = Speed
     */
        private double Str;
        private double Vit;
        private double Int;
        private double Spt;
        private double Agi;
        private double Spd;

    public Raca(double str, double vit, double Int,
                double spt, double agi, double spd)
    {
        this.setAgi(agi);
        this.setInt(Int);
        this.setSpd(spd);
        this.setSpt(spt);
        this.setStr(str);
        this.setVit(vit);
    }

    public double getStr() {
        return Str;
    }

    public void setStr(double str) {
        Str = str;
    }

    public double getVit() {
        return Vit;
    }

    public void setVit(double vit) {
        Vit = vit;
    }

    public double getInt() {
        return Int;
    }

    public void setInt(double anInt) {
        Int = anInt;
    }

    public double getSpt() {
        return Spt;
    }

    public void setSpt(double spt) {
        Spt = spt;
    }

    public double getAgi() {
        return Agi;
    }

    public void setAgi(double agi) {
        Agi = agi;
    }

    public double getSpd() {
        return Spd;
    }

    public void setSpd(double spd) {
        Spd = spd;
    }
}
