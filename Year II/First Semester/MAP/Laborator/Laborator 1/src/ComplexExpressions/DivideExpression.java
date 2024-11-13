package ComplexExpressions;

public class DivideExpression extends ComplexExpression {
    public DivideExpression(ComplexNumber[] args) {
        super(Operation.DIVISION, args);
    }

    @Override
    protected ComplexNumber executeOneOperation(ComplexNumber num1, ComplexNumber num2) {
        return num1.divide(num2);
    }
}
