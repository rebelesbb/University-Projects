using Seminar11.Domain;

namespace Seminar11.Repository;

public class InMemoryRepository<ID, E>: IRepository<ID, E> where E : Entity<ID>
{
    protected readonly Dictionary<ID, E> Entities = new Dictionary<ID, E>();
    
    public IEnumerable<E> findAll()
    {
        return Entities.Values;
    }
}