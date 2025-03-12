import model.Cerc;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

public class PredicateTest {

    public static<E> void print(List<E> list, Predicate<E> p){
        list.forEach(x -> {
            if(p.test(x))
                System.out.println(x);
        });

        System.out.println();
    }

    public static void main(String[] args){
        Predicate<Cerc> smallCirclePredicate = x -> x.getRaza() < 10;

        Cerc c1 = new Cerc(3);
        Cerc c2 = new Cerc(4);
        Cerc c3 = new Cerc(11);

        List<Cerc> listaCercuri = Arrays.asList(c1, c2, c3);

        print(listaCercuri,smallCirclePredicate);

        Predicate<Cerc> bigCirclePredicate = x -> x.getRaza() > 10;

        print(listaCercuri, bigCirclePredicate);

        Predicate<Cerc> bigCirclePredicateComposition = smallCirclePredicate.negate();

        print(listaCercuri, bigCirclePredicateComposition);

        Predicate<Cerc> smallEvenRadiusCircleP = smallCirclePredicate.and(x -> x.getRaza() % 2 == 0);

        print(listaCercuri, smallEvenRadiusCircleP);
    }
}
