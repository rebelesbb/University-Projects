using Seminar12.Domain;

namespace Seminar12.repository;

internal class AngajatInFileRepository : InFileRepository<string, Angajat>
{
    public AngajatInFileRepository(string fileName) : base(fileName, EntityToFileMapping.CreateAngajat)
    {
    }
}