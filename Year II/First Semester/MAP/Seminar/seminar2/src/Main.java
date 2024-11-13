import model.MyMap;
import model.Student;
import repository.InMemoryRepository;
import repository.User;

import java.util.*;

public class Main {

    public static List<Student> getList() {
        List<Student> list = new ArrayList<>();
        list.add(new Student("Stud1", 4.6f));
        list.add(new Student("Stud2", 5.3f));
        list.add(new Student("Stud3", 6.6f));
        list.add(new Student("Stud4", 7.3f));
        list.add(new Student("Stud5", 8.6f));
        list.add(new Student("Stud6", 8.8f));
        list.add(new Student("Stud7", 9f));
        list.add(new Student("Stud8", 1.7f));
        list.add(new Student("Stud9", 2.7f));
        list.add(new Student("Stud10", 9.7f));
        list.add(new Student("Stud11", 4.7f));
        list.add(new Student("Stud12", 5.2f));
        return list;
    }
    public static void main(String[] args) {

        Student s1 = new Student("Dan",4.5f);
        Student s2 = new Student("Ana",8.5f);
        Student s3 = new Student("Dan",4.5f);

        // Instantiere HashSet(multime)
        // Daca nu avem override la functia de equals il foloseste pe cel default si baga s1 si s3 in multime
        Set<Student> set = new HashSet<Student>();
        set.add(s1);
        set.add(s2);
        set.add(s3);

        for(Student s : set){
            System.out.println(s);
        }

        // Instantiere TreeSet
        // In momentul in care avem treeSet, in logica interna a acestuia avem elementele ordonate
        // Trebuie sa implementem o interfata specifica java care se numeste comparable
        TreeSet<Student> treeSet = new TreeSet<Student>();

        treeSet.add(s1);
        treeSet.add(s2);
        treeSet.add(s3);

        for(Student s : treeSet){
            System.out.println(s);
        }

        Map<String, Student> hashMap = new HashMap<String, Student>();

        hashMap.put("Dan", s1);
        hashMap.put("Ana", s2);
        hashMap.put("Dan", s3);

        for(Map.Entry<String, Student> entry : hashMap.entrySet()){
            System.out.println(entry);
        }

        Map<String, Student> treeMap = new TreeMap<>();

        treeMap.put("Dan", s1);
        treeMap.put("Ana", s2);
        treeMap.put("Dan", s3);

        for(Map.Entry<String, Student> entry : treeMap.entrySet()){
            System.out.println(entry);
        }

        Set<Student> students = new TreeSet<>((st1, st2) -> {return st1.getNume().compareTo(st2.getNume());});

        MyMap map = new MyMap();
        List<Student> list = getList();
        for(Student s : list){
            map.add(s);
        }

        for(Map.Entry<Integer, List<Student>> entry: map.getEntries()){
            System.out.println(entry.getKey());
            List<Student> temp = getList();
            Collections.sort(temp);
            for(Student s : temp){
                System.out.println(s);
            }

        }

        /*
        !!!
        Favor Composition instead of Inheritance
        Composition: aducem o instanta din clasa pe care vrem sa o utilizam in clasa noastra
        Mostenire: o folosim doar atunci cand exista o relatie logica intre doua obiecte,
                   ci nu oricand vrem sa reutilizam codul
         */

        User u1 = new User("Gigel", "Popescu"); u1.setId(2L);
        User u2 = new User("Marcel", "Georgescu"); u2.setId(3L);
        User u3 = new User("Dan", "Balan"); u3.setId(4L);

        InMemoryRepository<Long, User> repo = new InMemoryRepository<>();

        repo.save(u1);
        repo.save(u2);
        repo.save(u3);

        for(User u : repo.findAll()){
            System.out.println(u);
        }

    }
}