using Seminar11.Domain;

namespace Seminar11.Repository;

public class PontajeRepository: InFileRepository<Tuple<string, string>, Pontaj>
{
    AngajatiRepository AngajatiRepo { get; set; }
    SarciniRepository SarciniRepo { get; set; }

    public PontajeRepository(string filename, AngajatiRepository angajatiRepo, SarciniRepository sarciniRepo)
    : base(filename)
    {
        AngajatiRepo = angajatiRepo;
        SarciniRepo = sarciniRepo;
        LoadFromFile();
    }

    protected override Pontaj ParseLine(string line)
    {
        if (AngajatiRepo == null && SarciniRepo == null) return null;
        
        string[] pontajData = line.Split(',');
        string angajatID = pontajData[0];
        string sarcinaID = pontajData[1];
        DateTime date = DateTime.Parse(pontajData[2]);
        
        Angajat angajat = AngajatiRepo.FindOne(angajatID);
        Sarcina sarcina = SarciniRepo.FindOne(sarcinaID);
        
        Pontaj pontaj = new Pontaj(date, angajat, sarcina);
        pontaj.Id = new Tuple<string, string>(angajatID, sarcinaID);
        
        return pontaj;
    }

}