using Seminar11.Domain;
using Seminar11.Repository;

public class Program
{
    public static void Main(string[] args)
    {
        IRepository<string, Angajat> angajatiRepo = new AngajatiRepository("C:\\Users\\Bogdan Rebeles\\Desktop\\University-Projects\\Year II\\First Semester\\MAP\\Seminar\\Seminar11\\Seminar11\\angajati.txt");
        IRepository<string, Sarcina> sarciniRepo = new SarciniRepository("C:\\Users\\Bogdan Rebeles\\Desktop\\University-Projects\\Year II\\First Semester\\MAP\\Seminar\\Seminar11\\Seminar11\\sarcini.txt");
        IRepository<Tuple<string, string>, Pontaj> pontajeRepository = new PontajeRepository("C:\\Users\\Bogdan Rebeles\\Desktop\\University-Projects\\Year II\\First Semester\\MAP\\Seminar\\Seminar11\\Seminar11\\pontaje.txt", (AngajatiRepository) angajatiRepo, (SarciniRepository) sarciniRepo);
        foreach (var angajat in angajatiRepo.findAll())
        {
            Console.WriteLine(angajat);
        }

        foreach (var sarcina in sarciniRepo.findAll())
        {
            Console.WriteLine(sarcina);
        }

        foreach (var pontaj in pontajeRepository.findAll())
        {
            Console.WriteLine(pontaj);
        }
        
    }
}