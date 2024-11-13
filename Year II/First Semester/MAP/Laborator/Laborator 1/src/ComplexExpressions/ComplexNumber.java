package ComplexExpressions;

public class ComplexNumber {
    private final double re, im;

    public ComplexNumber(double re, double im) {
        this.re = re;
        this.im = im;
    }

    /**
     * Computes the addition of a complex number and the given number num
     * @param num : (ComplexNumbe) number to be added
     * @return : (Complex Number) the result of the addition
     */
    public ComplexNumber add(ComplexNumber num){
        return new ComplexNumber(this.re + num.re,this.im + num.im);
    }

    /**
     * Computes the substraction of the given number num from a complex number
     * @param num : (ComplexNumbe) number to be substracted
     * @return : (Complex Number) the result of the substraction
     */
    public ComplexNumber substract(ComplexNumber num){
        return new ComplexNumber(this.re - num.re,this.im - num.im);
    }

    /**
     * Computes the multiplication of a complex number (the numerator) by the given number num
     * @param num : (Complex Number) the multiplier
     * @return : (Complex Number) the result of the division
     */
    public ComplexNumber multipy(ComplexNumber num){
        // (a+bi) * (c+di) = a*c + a*d*i + b*c*i - b*d

        return new ComplexNumber(this.re * num.re - this.im * num.im,
                this.im * num.re + this.re * num.im);
    }

    /**
     * Computes the division of a complex number (the numerator) to the given number num
     * @param num : (Complex Number) the denominator
     * @return : (Complex Number) the result of the division
     */
    public ComplexNumber divide(ComplexNumber num){
        // (a+b*i) / (c+d*i) = (a+b*i)(c-d*i)/(c+d*i)(c-d*i)
        //                   = (a*c - a*d*i + b*c*i + b*d)/(c^2 + d^2)
        //                   = (a*c + b*d)/(c^2 + d^2) + [(a*d - b*c)/(c^2 + d^2)]*i

        double denomConjugate = (num.re * num.re + num.im * num.im);
        return new ComplexNumber((this.re * num.re + this.im * num.im)/denomConjugate,
                (this.im * num.re - this.re * num.im)/denomConjugate);
    }

    /**
     * Computes the conjugate of a complex number
     * @return : (Complex Number) the conjugate of the number
     */
    public ComplexNumber conjugate(){
        return new ComplexNumber(this.re, -this.im);
    }

    @Override
    public String toString() {
        return this.re +" + (" + this.im + ") * i";
    }
}
