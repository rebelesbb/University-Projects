import model.Arie;
import model.Cerc;
import model.Patrat;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FunctionalInterfaceTest {
    public static <E> void printArie(List<E> list, Arie<E> f){
        // using lambda function
        list.forEach(x -> System.out.println(f.calculeaza(x)));
    }

    public static void main(String[] args){
        Arie<Cerc> a1 = x -> Math.PI * Math.pow(x.getRaza(), 2);

        Cerc c1 = new Cerc(3);
        Cerc c2 = new Cerc(4);
        Cerc c3 = new Cerc(5.43);

        List<Cerc> listaCercuri = Arrays.asList(c1, c2, c3);
        /*
        listaCercuri.add(c1);
        listaCercuri.add(c2);
        listaCercuri.add(c3);
        */
        printArie(listaCercuri, a1);

        Arie<Patrat> a2 = x -> Math.pow(x.getLatura(), 2);

        Patrat patrat1 = new Patrat(5);
        Patrat patrat2 = new Patrat(6);
        Patrat patrat3 = new Patrat(7.89);

        List<Patrat> listaPatrate = Arrays.asList(patrat1, patrat2, patrat3);

        printArie(listaPatrate, a2);
    }
}
