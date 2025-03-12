using Seminar12.Domain;

namespace Seminar12.repository;

internal class PontajInFileRepository : InFileRepository<string, Pontaj>
{
    public PontajInFileRepository(string fileName) : base(fileName, null)
    {
        loadFromFile();
    }

    private new void loadFromFile()
    {
        List<Angajat> angajati = DataReader.ReadData<Angajat>(
            "/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar12/Seminar12/data/angajati.txt",
            EntityToFileMapping.CreateAngajat);
        List<Sarcina> sarcini = DataReader.ReadData<Sarcina>
        ("/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar12/Seminar12/data/sarcini.txt",
            EntityToFileMapping.CreateSarcina);
        using (var sr = new StreamReader(fileName))
        {
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                string[] fields = line.Split(',');
                var a = angajati.Find(x => x.ID.Equals(fields[0]));
                var s = sarcini.Find(x => x.ID.Equals(fields[1]));
                var id = fields[0] + "," + fields[1];
                var pontaj = new Pontaj()
                {
                    ID = id,
                    Angajat = a,
                    Sarcina = s,
                    Date = DateTime.ParseExact(fields[2], "d/M/yyyy", System.Globalization.CultureInfo.InvariantCulture)
                };
                entities[pontaj.ID] = pontaj;
            }
        }
    }
}