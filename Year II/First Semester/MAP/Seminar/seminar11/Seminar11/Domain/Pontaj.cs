using System.Globalization;

namespace Seminar11.Domain;

public class Pontaj: Entity<Tuple<string, string>>
{
    public DateTime Data { get; set; }
    public Angajat Angajat { get; set; }
    public Sarcina Sarcina { get; set; }

    public Pontaj(DateTime data, Angajat angajat, Sarcina sarcina)
    {
        Data = data;
        Angajat = angajat;
        Sarcina = sarcina;
    }

    public override string ToString()
    {
        return $"Pontaj {Id}: {Data.ToString("dd/MM/yyyy", CultureInfo.InvariantCulture)} - {Angajat} - {Sarcina}";
    }
}