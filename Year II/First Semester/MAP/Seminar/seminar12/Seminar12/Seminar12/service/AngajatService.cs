using Seminar12.Domain;
using Seminar12.repository;

namespace Seminar12.service;

internal class AngajatService
{
    private IRepository<string, Angajat> repo;

    public AngajatService(IRepository<string, Angajat> repo)
    {
        this.repo = repo;
    }
    
    public List<Angajat> FindAllAngajati()
    {
        return repo.FindAll().ToList();
    }

    public List<Angajat> GroupBySeniorityAndRate()
    {
        List<Angajat> angajati = repo.FindAll().ToList();

        return angajati
            .OrderBy(x => x.Nivel)
            .ThenByDescending(x => x.VenitPeOra)
            .ToList();
    }
    
    public List<Angajat> GroupBySeniorityAndRateSql()
    {
        List<Angajat> angajati = repo.FindAll().ToList();

        var result=
            from a in angajati
            orderby a.Nivel, a.VenitPeOra descending
            select a;
        
        return result.ToList();
    }
}