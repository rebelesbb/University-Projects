package model;

import java.util.*;

public class MyMap {
    private final Map<Integer, List<Student>> students;

    public MyMap() {
        students = new TreeMap<Integer, List<Student>>(new StudentGradeComparator());
                                // nu mai trebuie sa specificam neaparat tipul cheii si valorilor pt ca l-am specificat la declarare
    }

    public static class  StudentGradeComparator implements Comparator<Integer> {
        @Override public int compare(Integer o1, Integer o2) {
            return o2 - o1;
        }
    }

    public void add(Student student) {
        int medie = Math.round(student.getMedia());

        if(students.get(medie) == null){
            List<Student> list = new ArrayList<Student>();
            list.add(student);
            students.put(medie, list);
        }
        else{
            students.get(medie).add(student);
        }
    }

    public Set<Map.Entry<Integer, List<Student>>> getEntries(){
        return students.entrySet();

    }
}
