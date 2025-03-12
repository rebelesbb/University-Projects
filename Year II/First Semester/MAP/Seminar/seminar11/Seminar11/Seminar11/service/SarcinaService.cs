using Seminar11.Domain;
using Seminar11.repository;

namespace Seminar11.service;

internal class SarcinaService
{
    private IRepository<string, Sarcina> repo;

    public SarcinaService(IRepository<string, Sarcina> repo)
    {
        this.repo = repo;
    }


    public List<Sarcina> FindAllSarcini()
    {
        return repo.FindAll().ToList();
    }
}