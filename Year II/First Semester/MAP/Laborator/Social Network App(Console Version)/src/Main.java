import domain.Friendship;
import domain.Tuple;
import domain.User;
import domain.validators.FriendshipValidator;
import domain.validators.UserValidator;
import domain.validators.Validator;
import repository.DataManagerStructure;
import repository.Repository;
import repository.database.FriendshipDatabaseRepository;
import repository.database.UserDatabaseRepository;
import repository.file.FriendshipRepository;
import service.SocialNetworkService;
import ui.Console;


public class Main {
    /*
    public static void testService(){
        for(User u : testService.getUsers()){
            System.out.println(u);
        }

        testService.addUser("Mariana","Georgescu","m.andr@yahoo.com", "pasW0rd");
        testService.addUser("Elena", "Grigore", "elenuta@yahoo.com", "parola");

        for(User u : testService.getUsers()) {
            System.out.println(u);
        }

        testService.deleteUser((long)11);
        testService.deleteUser((long)12);

        for(User u : testService.getUsers()){
            System.out.println(u);
        }

        testService.deleteUser((long)7);

        System.out.println(testService.getFriendships());
        System.out.println();
        testService.addFriend((long)4,(long)5);

        System.out.println(testService.getFriendships());
        System.out.println();

        testService.removeFriend((long)5,(long)4);
        System.out.println(testService.getFriendships());
        System.out.println();

        System.out.println(testService.communitiesCount());
        System.out.println(testService.biggestCommunity());
    }
    */

    public static void main(String[] args) {

        Validator<User> userValidator = new UserValidator();
        //Repository<Long, User> userRepository = new UserRepository(userValidator, "./data/users.txt");

        Validator<Friendship> frienshipValidator = new FriendshipValidator();
        //Repository<Tuple<Long, Long>, Friendship> friendshipRepository = new FriendshipRepository(testFrienshipValidator, "./data/friendships.txt");

        String url = "jdbc:postgresql://localhost:5432/SocialNetworkDatabase";
        String username = "socialNetworkAppUsername";
        String password = "socialNetworkAppPassword";
        Repository<Long, User> userRepository = new UserDatabaseRepository(url, username, password, userValidator);
        Repository<Tuple<Long, Long>, Friendship> friendshipRepository = new FriendshipDatabaseRepository(url, username, password, frienshipValidator);
        DataManagerStructure dataManager = new DataManagerStructure(userRepository, friendshipRepository);

        SocialNetworkService service = new SocialNetworkService(dataManager);

        Console console = new Console(service);

        console.run();
    }
}