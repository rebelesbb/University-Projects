namespace Seminar11.Domain;

public class Sarcina: Entity<string>
{
    public Difficulty Dificultate{get;set;}
    public int NrOreEstimate{get;set;}

    public Sarcina(Difficulty dificultate, int nrOreEstimate)
    {
        Dificultate = dificultate;
        NrOreEstimate = nrOreEstimate;
    }

    public override string ToString()
    {
        return $"Sarcina {Id}: {Dificultate} ({NrOreEstimate} ore)";
    }
}