package ComplexExpressions;

public class AddExpression extends ComplexExpression {
    public AddExpression(ComplexNumber[] args) {
        super(Operation.ADDITION, args);
    }

    @Override
    protected ComplexNumber executeOneOperation(ComplexNumber num1, ComplexNumber num2) {
        return num1.add(num2);
    }
}
