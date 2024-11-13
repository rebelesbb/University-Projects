package model;

public class Cerc {
    private final double raza;

    public Cerc(double raza){
        this.raza = raza;
    }

    public double getRaza(){
        return this.raza;
    }

    @Override
    public String toString(){
        return "Cerc{ raza : " + this.getRaza() + " }";
    }
}
