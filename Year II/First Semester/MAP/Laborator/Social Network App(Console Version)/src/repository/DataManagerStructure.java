package repository;

import domain.Friendship;
import domain.Tuple;
import domain.User;

public class DataManagerStructure {
    private final Repository<Long, User> userRepository;
    private final Repository<Tuple<Long, Long>, Friendship> friendshipRepository;

    public DataManagerStructure(Repository<Long, User> usersRepo, Repository<Tuple<Long,Long>, Friendship> friendshipRepo){
        this.userRepository = usersRepo;
        this.friendshipRepository = friendshipRepo;
    }

    /**
     *
     * @return the repository of users
     */
    public Repository<Long, User> getUserRepository(){
        return this.userRepository;
    }

    /**
     *
     * @return the repository of friendships
     */
    public Repository<Tuple<Long, Long>, Friendship> getFriendshipRepository(){
        return this.friendshipRepository;
    }

}
