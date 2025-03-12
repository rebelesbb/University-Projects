using Seminar11.Domain;

namespace Seminar11.Repository;

public interface IRepository<ID, E> where E : Entity<ID>
{
    IEnumerable<E> findAll();
}