import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class StreamTest {
    public static <E> List<E> filterGeneric1(List<E> list, Predicate<E> p){
        return list.stream().filter(p).collect(Collectors.toList());
    }

    public static <E> List<E> filterGeneric2(List<E> list, Predicate<E> p, Comparator<E> comp){
        return list.stream().filter(p).sorted(comp).collect(Collectors.toList());
    }

    public static void main(String[] args){
        List<Integer> list = Arrays.asList(1, 7, 6, 4, 2, 8, 9, -3);

        List<Integer> result1 = filterGeneric1(list, x -> x % 2 == 0);
        System.out.println(result1);

        List<Integer> result2 = filterGeneric2(list, x -> x % 2 == 0, Integer::compare);
        System.out.println(result2);

        List<Integer> result3 = filterGeneric2(list, x -> x % 2 == 0, (x, y) -> Integer.compare(y, x));
        System.out.println(result3);
    }
}
