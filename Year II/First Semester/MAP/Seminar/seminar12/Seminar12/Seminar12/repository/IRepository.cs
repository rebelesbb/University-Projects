using Seminar12.Domain;

namespace Seminar12.repository;

public interface IRepository<ID, E> where E : Entity<ID>
{
    IEnumerable<E> FindAll();
}
