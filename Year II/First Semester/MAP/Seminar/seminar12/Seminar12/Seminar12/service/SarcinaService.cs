using Seminar12.Domain;
using Seminar12.repository;

namespace Seminar12.service;

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

    public IDictionary<Dificultate, double> GetSarciniByAverageDuration()
    {
        List<Sarcina> sarcini = repo.FindAll().ToList();

        return sarcini.GroupBy(sarcina => sarcina.TipDificultate)
            .ToDictionary(
                group => group.Key,
                group => group.Average(sarcina => sarcina.NrOreEstimate)
            );
    }

    public IDictionary<Dificultate, double> GetSarciniByAverageDurationSql()
    {
        List<Sarcina> sarcini = repo.FindAll().ToList();

        var result = from sarcina in sarcini
            group sarcina by sarcina.TipDificultate into g
            select new { Dificultate = g.Key, Media = g.Average(sarcina => sarcina.NrOreEstimate) };

        return result
            .ToDictionary(item => item.Dificultate, item => item.Media);
    }
}