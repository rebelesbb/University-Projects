namespace Seminar11.Domain;

public class Angajat: Entity<string>
{
    public string Nume{get;set;}
    public double VenitPeOra{get;set;}
    public Level Nivel{get;set;}

    public Angajat(string nume, Level nivel, double venitPeOra)
    {
        Nume = nume;
        Nivel = nivel;
        VenitPeOra = venitPeOra;
    }

    public override string ToString()
    {
        return $"Angajat {Id}: {Nume}, {Nivel}, {VenitPeOra}";
    }
    
}