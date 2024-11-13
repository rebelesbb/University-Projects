import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ComparatorTest {
    public static void main(String[] args){
        Comparator<Integer> comparator1 = (a, b) -> Integer.compare(a, b);
        Comparator<Integer> comparator2 = (a, b) -> Integer.compare(b, a);

        Comparator<Integer> comparator3 = Integer::compare;

        List<Integer> intList = new ArrayList<>();
        intList.add(1);
        intList.add(-4);
        intList.add(3);
        intList.add(100);
        intList.add(20);

        intList.sort(comparator1);
        intList.forEach(System.out::println);

        intList.sort(comparator2);
        System.out.println(intList);

        intList.sort(comparator2.reversed());
        System.out.println(intList);

    }
}
