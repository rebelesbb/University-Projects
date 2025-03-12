using Seminar11.Domain;
using Seminar11.repository;

namespace Seminar11.service;

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
}