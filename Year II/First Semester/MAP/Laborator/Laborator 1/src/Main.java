import ExpressionFactoryParser.ExpressionParser;
import ExpressionValidator.ExpressionValidator;
import ComplexExpressions.*;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void run(){
        String[] op1 = {"-2+3*i", "+", "-2*i", "+", "3*i", "+", "-2", "+", "1-2*i"};
        String[] op2 = {"-2+3*i", "-", "-2*i", "-", "3*i", "-", "-2", "-", "1-2*i"};
        String[] op3 = {"-2+3*i", "*", "-2-4*i"}; // 4 +8i -6i + 12 = 16 + 2i
        String[] op4 = {"-2+3*i", "*", "-2-3*i", "*", "2"};
        String[] op5 = {"10-20*i", "/", "1-1*i"}; // (10 + 10i -20i + 20) / 2 = 15 - 5i
        String[] op6 = {"10-20*i", "/", "-2-3*i", "/"};
        String[] op7 = {"10-20*i", "/", "-2-3*i", "/", "-2-"};
        String[] op8 = {"10-20*i", "/", "-2-3*i", "*", "-2"};
        String[] op9 = {"+", "2", "+"};
        String[] op10 = {"4", "2", "3"};
        String[] op11 = {"1", "$", "3"};

        List<ExpressionParser> ops = new ArrayList<>();
        ops.add(new ExpressionParser(op1));
        ops.add(new ExpressionParser(op2));
        ops.add(new ExpressionParser(op3));
        ops.add(new ExpressionParser(op4));
        ops.add(new ExpressionParser(op5));
        ops.add(new ExpressionParser(op6));
        ops.add(new ExpressionParser(op7));
        ops.add(new ExpressionParser(op8));
        ops.add(new ExpressionParser(op9));
        ops.add(new ExpressionParser(op10));
        ops.add(new ExpressionParser(op11));


        for(ExpressionParser op : ops){
            try{
                System.out.println(op.computeExpression());
            }
            catch(Exception e){
                System.out.println(e.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        run();

        try {
            ExpressionParser parser = new ExpressionParser(args);
            System.out.println(parser.computeExpression());
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
}