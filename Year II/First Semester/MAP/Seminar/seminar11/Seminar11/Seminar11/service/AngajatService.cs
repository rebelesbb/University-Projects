using Seminar11.Domain;
using Seminar11.repository;

namespace Seminar11.service;

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
}