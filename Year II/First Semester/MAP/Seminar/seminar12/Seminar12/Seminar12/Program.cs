using System.Data;
using Seminar12.Domain;
using Seminar12.repository;
using Seminar12.service;

namespace Seminar12;

internal class Program
{
    private static void Main(string[] args)
    {
        AngajatService angajatService = GetAngajatService();
        SarcinaService sarcinaService = GetSarcinaService();
        PontajService pontajService = GetPontajService();
        
        //////// Afisare angajati
        List<Angajat> resultAngajati1 = angajatService.GroupBySeniorityAndRate();
        List<Angajat> resultAngajati2 = angajatService.GroupBySeniorityAndRateSql();
        
        Console.WriteLine("------------- Angajati ----------------");
        resultAngajati1.ForEach(item => Console.WriteLine(item));
        Console.WriteLine("------------- SQL like ----------------");
        resultAngajati2.ForEach(item => Console.WriteLine(item));
        
        Console.WriteLine();
        
        //////// Afisare sarcini
        Console.WriteLine("------------ Sarcini ----------------");
        foreach (var keyValuePair in sarcinaService.GetSarciniByAverageDuration())
        {
            Console.WriteLine(keyValuePair);
        }
        Console.WriteLine("------------- SQL like ----------------");

        foreach (var keyValuePair in sarcinaService.GetSarciniByAverageDurationSql())
        {
            Console.WriteLine(keyValuePair);
        }
        
        //////// Afisare pontaje
        Console.WriteLine("------------- Pontaje ---------------");
        pontajService.GetTopAngajatiBySalary().ForEach(item => Console.WriteLine(item));
        Console.WriteLine("------------- SQL like ---------------");
        pontajService.GetTopAngajatiBySalarySql().ForEach(item => Console.WriteLine(item));
    }

    private static AngajatService GetAngajatService()
    {
        var fileName = "/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar12/Seminar12/data/angajati.txt";

        IRepository<string, Angajat> repo1 = new AngajatInFileRepository(fileName);
        var service = new AngajatService(repo1);
        return service;
    }

    private static SarcinaService GetSarcinaService()
    {
        var fileName2 = "/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar12/Seminar12/data/sarcini.txt";

        IRepository<string, Sarcina> repo1 = new SarcinaInFileRepository(fileName2);
        var service = new SarcinaService(repo1);
        return service;
    }

    private static PontajService GetPontajService()
    {
        var fileName2 = "/Users/lauradiana/Desktop/MAP 2024-2025/Seminar/Seminar12/Seminar12/data/pontaje.txt";

        IRepository<string, Pontaj> repo1 = new PontajInFileRepository(fileName2);
        var service = new PontajService(repo1);
        return service;
    }
}