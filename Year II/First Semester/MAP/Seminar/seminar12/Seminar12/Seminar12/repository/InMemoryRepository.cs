using Seminar12.repository;
using Seminar12.Domain;

namespace Seminar12.repository;

internal class InMemoryRepository<ID, E> : IRepository<ID, E> where E : Entity<ID>
{
    protected IDictionary<ID, E> entities = new Dictionary<ID, E>();

    public IEnumerable<E> FindAll()
    {
        return entities.Values.ToList<E>();
    }
}