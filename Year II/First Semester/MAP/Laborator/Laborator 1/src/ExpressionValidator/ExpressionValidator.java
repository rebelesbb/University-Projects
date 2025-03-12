package ExpressionValidator;

public class ExpressionValidator {
    private final String[] arguments;
    private String op = "+";

    public ExpressionValidator(String[] arguments) {
        this.arguments = arguments;
        if(this.arguments.length >= 2)
            this.op = this.arguments[1];
    }

    public boolean isValidExpression() {
        if(this.arguments.length % 2 == 0 || this.arguments.length < 3)
            return false;

        if(!(this.op.equals("+") || this.op.equals("-") || this.op.equals("*") || this.op.equals("/")))
            return false;

        for(int i = 0; i < arguments.length; i++) {
            String currentArg = arguments[i];
            if(i % 2 == 0) {
                if(currentArg.charAt(0) == '-') {
                    // if it's operator
                    if (currentArg.length() == 1)
                        return false;
                    currentArg = new StringBuilder(currentArg).deleteCharAt(0).toString();
                }

                // before splitting the current argument by + - *
                // check if there aren't any more operators (--1+2*i, -1**2)
                int opCount = 0;
                for(char c : currentArg.toCharArray())
                    if(c == '+' || c == '-' || c == '*')
                        opCount++;

                // after splitting the current arg
                // check if we have any char. that doesn't match the format
                String[] argComps = currentArg.split("[+*-]");

                if(opCount != argComps.length - 1)
                    return false;


                for(String argComp : argComps) {
                    if(argComp.isEmpty())
                        return false;
                    for(char c : argComp.toCharArray())
                        if(!Character.isDigit(c) && c !='i')
                            return false;
                }

            }
            else if(!currentArg.equals(this.op))
                return false;
            }
            return true;
    }
}
