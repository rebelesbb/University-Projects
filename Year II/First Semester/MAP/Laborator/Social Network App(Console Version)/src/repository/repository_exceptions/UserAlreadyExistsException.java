package repository.repository_exceptions;

public class UserAlreadyExistsException extends RuntimeException {

    public UserAlreadyExistsException() {
      super("User already exists.");
    }

    public UserAlreadyExistsException(String message) {
      super(message);
    }

    public UserAlreadyExistsException(String message, Throwable cause) {
      super(message, cause);
    }

    public UserAlreadyExistsException(Throwable cause) {
      super(cause);
    }

    public UserAlreadyExistsException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
      super(message, cause, enableSuppression, writableStackTrace);
    }
}
