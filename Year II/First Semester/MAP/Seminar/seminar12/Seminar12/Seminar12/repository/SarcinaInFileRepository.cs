using Seminar12.Domain;

namespace Seminar12.repository;

internal class SarcinaInFileRepository : InFileRepository<string, Sarcina>
{
    public SarcinaInFileRepository(string fileName) : base(fileName, EntityToFileMapping.CreateSarcina)
    {
    }
}