using Seminar11.Domain;
using Seminar11.repository;
using Seminar11.service;

namespace Seminar11;

internal class Program
{
    private static void Main(string[] args)
    {
        List<Angajat> angajati = GetAngajatService().FindAllAngajati();
        angajati.ForEach(ang => Console.WriteLine(ang));

        List<Sarcina> sarcini = GetSarcinaService().FindAllSarcini();
        sarcini.ForEach(s => Console.WriteLine(s));

        List<Pontaj> pontaje = GetPontajService().FindAllPontaje();
        pontaje.ForEach(p => Console.WriteLine(p));
    }

    private static AngajatService GetAngajatService()
    {
        var fileName = "/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar11/Seminar11/data/angajati.txt";

        IRepository<string, Angajat> repo1 = new AngajatInFileRepository(fileName);
        var service = new AngajatService(repo1);
        return service;
    }

    private static SarcinaService GetSarcinaService()
    {
        var fileName2 = "/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar11/Seminar11/data/sarcini.txt";

        IRepository<string, Sarcina> repo1 = new SarcinaInFileRepository(fileName2);
        var service = new SarcinaService(repo1);
        return service;
    }

    private static PontajService GetPontajService()
    {
        var fileName2 = "/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar11/Seminar11/data/pontaje.txt";

        IRepository<string, Pontaj> repo1 = new PontajInFileRepository(fileName2);
        var service = new PontajService(repo1);
        return service;
    }
}