package domain.validators;


import domain.Utilizator;

public class UtilizatorValidator implements Validator<Utilizator> {
    @Override
    public void validate(Utilizator entity) throws ValidationException {
        //TODO: implement method validate
        if(entity.getFirstName().isEmpty())
            throw new ValidationException("Utilizatorul nu este valid");
    }
}
