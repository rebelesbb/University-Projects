using Seminar11.Domain;

namespace Seminar11.Repository;

public abstract class InFileRepository<ID, E>: InMemoryRepository<ID, E> where E : Entity<ID> 
{
    protected string Filename;

    public InFileRepository(string filename)
    {
        Filename = filename;
        LoadFromFile();
    }

    protected void LoadFromFile()
    {
        if (File.Exists(Filename)) { 
            // Reads file line by line 
            StreamReader textFile = new StreamReader(Filename); 
            string line; 
  
            while ((line = textFile.ReadLine()) != null) { // id, nume, venit, level
                var entity = ParseLine(line);
                if (entity != null)
                    Save(entity);
            } 
  
            textFile.Close();
        }
    }

    public void Save(E entity)
    {
        Entities.Add(entity.Id, entity);
    }
    
    protected abstract E ParseLine(string line);

    public E FindOne(ID id)
    {
        return Entities[id];
    }
}