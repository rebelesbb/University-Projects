package ComplexExpressions;

public abstract class ComplexExpression {
    Operation operation;
    ComplexNumber[] args;

    public ComplexExpression(Operation operation, ComplexNumber[] args) {
        this.operation = operation;
        this.args = args;
    }

    abstract protected ComplexNumber executeOneOperation(ComplexNumber num1, ComplexNumber num2);
       // TemplateMethodDesignPattern

    public ComplexNumber execute(){
        ComplexNumber result = args[0];

        for(int i = 1; i < args.length; i++) {
            result = executeOneOperation(result, args[i]);
        }

        return result;
    }
}
