import domain.Utilizator;
import domain.validators.UtilizatorValidator;
import domain.validators.ValidationException;
import domain.validators.Validator;
import repository.Repository;
import repository.memory.InMemoryRepository;
import repository.file.UtilizatorRepository;


public class Main {
    public static void main(String[] args) {

        Repository<Long, Utilizator> repo = new InMemoryRepository<Long, Utilizator>(new UtilizatorValidator());
        Repository<Long, Utilizator> repoFile = new UtilizatorRepository(new UtilizatorValidator(), "./src/data/utilizatori.txt");

        for(Utilizator u: repoFile.findAll())
            System.out.println(u);

        Utilizator u1 = new Utilizator("IONUT2", "a");
        Utilizator u2 = new Utilizator("Mihai2", "b");
        Utilizator u3 = null;
        u1.setId(4L);
        u2.setId(5L);
        try {
            repoFile.save(u1);
            repoFile.save(u2);
            repoFile.save(u3);
        }catch(IllegalArgumentException | ValidationException e)
        {
            System.out.println(e.getMessage());
        }
        System.out.println();

    }
}