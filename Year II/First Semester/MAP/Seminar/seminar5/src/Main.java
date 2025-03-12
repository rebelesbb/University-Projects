import domain.Nota;
import domain.Student;
import domain.Tema;

import java.time.LocalDate;
import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;


public class Main {
    private static List<Student> getStudents() {
        Student s1 = new Student("andrei", 221);
        s1.setId(2L);
        Student s2 = new Student("dan", 222);
        s2.setId(2L);
        Student s3 = new Student("and3", 222);
        s3.setId(2L);
        Student s4 = new Student("costel", 222);
        s4.setId(2L);
        return Arrays.asList(s1, s2, s3, s4);
    }

    private static List<Tema> getTeme() {
        return Arrays.asList(
                new Tema("t1", "desc1"),
                new Tema("t2", "desc2"),
                new Tema("t3", "desc3"),
                new Tema("t4", "desc4")
        );
    }

    private static List<Nota> getNote(List<Student> stud, List<Tema> teme) {
        return Arrays.asList(
                new Nota(stud.get(0), teme.get(0), 10d, LocalDate.of(2019, 11, 2), "profesor1"),
                new Nota(stud.get(1), teme.get(0), 9d, LocalDate.of(2019, 11, 2).minusWeeks(1), "profesor1"),
                new Nota(stud.get(1), teme.get(1), 10d, LocalDate.of(2019, 10, 20), "profesor2"),
                new Nota(stud.get(1), teme.get(2), 10d, LocalDate.of(2019, 10, 20), "profesor2"),
                new Nota(stud.get(2), teme.get(1), 7d, LocalDate.of(2019, 10, 28), "profesor12"),
                new Nota(stud.get(2), teme.get(3), 9d, LocalDate.of(2019, 10, 27), "profesor2"),
                new Nota(stud.get(1), teme.get(1), 10d, LocalDate.of(2019, 10, 29), "profesor2")
        );
    }

    public static double average(List<Nota> notaList) {
        double sum = notaList .stream()
                .map(Nota::getValue)
                .reduce(0d, Double::sum);
        return sum/notaList.size();
    }

    public static void report1(List<Nota> note, String string) {
        note
            .stream()
            .collect(Collectors.groupingBy(Nota::getStudent))
            .entrySet()
            .stream()
            .filter(x -> x.getKey().getName().contains(string))
            .sorted((s1, s2) -> {
                double avg1 = average(s1.getValue());
                double avg2 = average(s2.getValue());
                if(avg1 > avg2) {
                    return -1;
                }
                else return 0;
            })
            .forEach(s -> System.out.println(s.getKey().getName() + " media: " + average(s.getValue())));


    }

    public static void report2(List<Nota> note, String string) {
        note
                .stream()
                .collect(Collectors.groupingBy(Nota::getProfesor, Collectors.averagingDouble(Nota::getValue)))
                .entrySet()
                .stream()
                .filter(p -> p.getKey().contains(string))
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .forEach(p -> System.out.println(p.getKey() + " media notelor date: " + p.getValue()));
    }

    public static void report3(List<Nota> note, int group){
        note.stream()
                .filter(n -> n.getStudent().getGroup() == group)
                .collect(Collectors.groupingBy(Nota::getTema, Collectors.counting()))
                .entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .forEach(tema -> System.out.println(tema.getKey().getDesc() + " numar studenti : " + tema.getValue()));

    }

    public static boolean startsWith(int group) {
    }

    public static void report4(List<Nota> note, int group){


        note.stream()
                .filter(nota -> nota.toString().startsWith(group + ""))
                .collect(Collectors.groupingBy(n -> n.getStudent().getGroup()))
                .entrySet()
                .stream()
                .sorted()
    }

    public static void main(String[] args) {

        List<Student> students = getStudents();
        List<Tema> tema = getTeme();
        List<Nota> note = getNote(students, tema);
        report1(note, "and");
        report2(note, "2");
        report3(note, 222);
    }
}


