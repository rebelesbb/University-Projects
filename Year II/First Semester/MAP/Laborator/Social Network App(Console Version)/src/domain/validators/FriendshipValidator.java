package domain.validators;

import domain.Friendship;
import domain.Tuple;

import java.util.List;

public class FriendshipValidator implements Validator<Friendship> {

    @Override
    public void validate(Friendship entity) throws ValidationException {
        if(entity.getId() == null)
            throw new ValidationException("Friendship id is required");

        if(entity.getId().getFirst() == null || entity.getId().getSecond() == null)
            throw new ValidationException("The id of both of the two users is required");

        if(entity.getId().getFirst().equals(entity.getId().getSecond()))
            throw new ValidationException("The id of both of the two users is the same");
    }
}
