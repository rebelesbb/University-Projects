package repository.repository_exceptions;

public class FriendshipAlreadyExistsException extends RuntimeException {

    public FriendshipAlreadyExistsException() {
        super("The users are already friends.");
    }

    public FriendshipAlreadyExistsException(String message) {
        super(message);
    }

    public FriendshipAlreadyExistsException(String message, Throwable cause) {
        super(message, cause);
    }

    public FriendshipAlreadyExistsException(Throwable cause) {
        super(cause);
    }

    public FriendshipAlreadyExistsException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
