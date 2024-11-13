package ComplexExpressions;

public class MultiplyExpression extends ComplexExpression {
    public MultiplyExpression(ComplexNumber[] args) {
        super(Operation.MULTIPLICATION, args);
    }

    @Override
    protected ComplexNumber executeOneOperation(ComplexNumber num1, ComplexNumber num2) {
        return num1.multipy(num2);
    }
}
