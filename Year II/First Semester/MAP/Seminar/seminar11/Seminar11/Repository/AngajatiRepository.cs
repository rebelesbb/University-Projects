using Seminar11.Domain;

namespace Seminar11.Repository;

public class AngajatiRepository: InFileRepository<string, Angajat>
{
    public AngajatiRepository(string filename) : base(filename)
    { }

    protected override Angajat ParseLine(string line)
    {
        string[] angajatData = line.Split(',');
        string angajatId = angajatData[0];
        string angajatName = angajatData[1];
        Level angajatLevel = Enum.Parse<Level>(angajatData[2], true);
        double angajatIncome = double.Parse(angajatData[3]);
        Angajat angajat = new Angajat(angajatName, angajatLevel, angajatIncome);
        angajat.Id = angajatId;
        return angajat;
    }
    
}