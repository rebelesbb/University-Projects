package ExpressionFactoryParser;

import ComplexExpressions.*;

    // SingletonDesignPattern
public class ExpressionFactory {

    private static final ExpressionFactory factory = new ExpressionFactory();

        // making the constructor private, we can't create instantiate the class
    private ExpressionFactory(){}

    public static ExpressionFactory getInstance(){
        return factory;
    }

    public ComplexExpression createExpression(Operation operation, ComplexNumber[] args){
        ComplexExpression expr = null;
        if(operation == Operation.ADDITION) {
            expr = new AddExpression(args);
        }
        else if (operation == Operation.SUBTRACTION) {
            expr = new SubstractExpression(args);
        }
        else if (operation == Operation.MULTIPLICATION) {
            expr = new MultiplyExpression(args);
        }
        else if (operation == Operation.DIVISION) {
            expr = new DivideExpression(args);
        }

        return expr;
    }

}

/*
-3.0 + (6.0*i)
-1.0 + (0.0*i)
16.0 + (2.0*i)
26.0 + (0.0*i)
15.0 + (5.0*i)
 */
