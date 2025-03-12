using Seminar11.Domain;

namespace Seminar11.Repository;

public class SarciniRepository: InFileRepository<string, Sarcina>
{
    public SarciniRepository(string filename) : base(filename) { }

    protected override Sarcina ParseLine(string line)
    {
        string[] sarcinaData = line.Split(',');
        string sarcinaID = sarcinaData[0];
        Difficulty sarcinaDifficulty = Enum.Parse<Difficulty>(sarcinaData[1]);
        int sarcinaTime = int.Parse(sarcinaData[2]);
        Sarcina sarcina = new Sarcina(sarcinaDifficulty, sarcinaTime);
        sarcina.Id = sarcinaID;
        return sarcina;
    }
}