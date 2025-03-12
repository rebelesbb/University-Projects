package ExpressionFactoryParser;

import ComplexExpressions.ComplexExpression;
import ComplexExpressions.ComplexNumber;
import ComplexExpressions.Operation;
import ExpressionValidator.ExpressionValidator;

import java.security.InvalidParameterException;

public class ExpressionParser {
    ExpressionValidator validator;
    ExpressionFactory factory = ExpressionFactory.getInstance();
    String[] args;

    public ExpressionParser(String[] args) {
        this.args = args;

        if(args != null)
            validator = new ExpressionValidator(args);
    }

    private ComplexNumber[] parseExpression(){
        if(args == null)
            throw new InvalidParameterException("Invalid expression");

        ComplexNumber[] nums = new ComplexNumber[args.length/2 + 1];
        int cnt = 0;

        for (int i = 0; i < args.length; i+=2) {
            String currentArg = args[i];
            boolean reIsNegative = false, imIsNegative = false;

            if(currentArg.charAt(0) == '-') {
                currentArg = currentArg.replaceFirst("-", ""); // -1-2i ""
                reIsNegative = true;
            }

            if(currentArg.contains("-"))
                imIsNegative = true;

            String[] argComps = currentArg.split("[+-]");

            int re = 0, im = 0;

            if(argComps.length == 1) // the complex number doesn't have both re and im
            {
                if(!argComps[0].contains("*")) { // only has re
                    re = Integer.parseInt(argComps[0]);
                }
                else { // only has im
                    im = Integer.parseInt(argComps[0].split("[*]")[0]);
                    if(reIsNegative){
                        imIsNegative = true;
                    }
                }
            }

            else{ // has both
                re = Integer.parseInt(argComps[0]);
                im = Integer.parseInt(argComps[1].split("[*]")[0]);
            }

            if(reIsNegative){
                re = -re;
            }
            if(imIsNegative){
                im = -im;
            }

            nums[cnt++] = new ComplexNumber(re, im);
        }

        return nums;
    }

    public ComplexNumber computeExpression(){

        if(!validator.isValidExpression()) {
            throw new InvalidParameterException("Invalid expression");
        }

        ComplexNumber[] nums = parseExpression();

        Operation operation;
        String operator = args[1];

        operation = switch (operator) {
            case "+" -> Operation.ADDITION;
            case "-" -> Operation.SUBTRACTION;
            case "*" -> Operation.MULTIPLICATION;
            case "/" -> Operation.DIVISION;
            default -> null;
        };

        ComplexExpression exp = factory.createExpression(operation, nums);

        return exp.execute();
    }
}
