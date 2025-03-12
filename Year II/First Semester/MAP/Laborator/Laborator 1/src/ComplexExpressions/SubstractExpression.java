package ComplexExpressions;

public class SubstractExpression extends ComplexExpression{
    public SubstractExpression(ComplexNumber[] args) {
        super(Operation.SUBTRACTION, args);
    }

    @Override
    protected ComplexNumber executeOneOperation(ComplexNumber num1, ComplexNumber num2){
        return num1.substract(num2);
    }
}
