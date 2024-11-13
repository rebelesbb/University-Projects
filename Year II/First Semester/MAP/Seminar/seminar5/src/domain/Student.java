package domain;

public class Student extends Entity<Long> {
    String name;
    int group;

    public Student(String name, int group) {
        this.name = name;
        this.group = group;
    }

    public String getName() {
        return name;
    }

    public int getGroup() {
        return group;
    }
}
