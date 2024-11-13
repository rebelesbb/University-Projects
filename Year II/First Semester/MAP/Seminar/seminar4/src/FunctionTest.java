import java.util.function.Function;

public class FunctionTest {

    public static void main(String[] args){
        // daca avem acolade la lamda dam return
        Function<String, Integer> converter1 = x -> Integer.valueOf(x);
        System.out.println(converter1.apply("23"));

        Function<String, Integer> converter2 = Integer::valueOf;
        System.out.println(converter2.apply("23"));

        Function<Integer, Integer> squared = x -> x * x;

        System.out.println(converter1.andThen(squared).apply("4"));


    }
}
