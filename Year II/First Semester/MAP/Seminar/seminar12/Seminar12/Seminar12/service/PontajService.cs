using Seminar12.Domain;
using Seminar12.repository;

namespace Seminar12.service;

internal class PontajService
{
    private IRepository<string, Pontaj> repo;

    public PontajService(IRepository<string, Pontaj> repo)
    {
        this.repo = repo;
    }

    public List<Pontaj> FindAllPontaje()
    {
        return repo.FindAll().ToList();
    }

    public List<(string Nume, double Salar)> GetTopAngajatiBySalary()
    {
        List<Pontaj> pontaje = repo.FindAll().ToList();

        return pontaje.GroupBy(x => x.Angajat)
            .Select(g => (
                Nume: g.Key.Nume,
                Salar: g.Sum(x => x.Sarcina.NrOreEstimate * x.Angajat.VenitPeOra)
            ))
            .OrderByDescending(x => x.Salar)
            .Take(2)
            .ToList();
    }

    public List<(string Nume, double Salar)> GetTopAngajatiBySalarySql()
    {
        List<Pontaj> pontaje = repo.FindAll().ToList();

        var query = (from p in pontaje
                group p by p.Angajat into g
                let totalSalary = g.Sum(x => x.Sarcina.NrOreEstimate * x.Angajat.VenitPeOra)
                orderby totalSalary descending
                select new
                {
                    Nume = g.Key.Nume,
                    Salar = totalSalary
                })
            .Take(2)
            .Select(x => (x.Nume, x.Salar))
            .ToList();

        return query;
    }
}