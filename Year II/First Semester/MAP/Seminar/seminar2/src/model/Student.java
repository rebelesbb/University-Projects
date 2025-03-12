package model;

import java.util.Objects;

public class Student implements Comparable<Student> {
    private String nume;
    private float media;

    public Student(String nume, float media) {
        this.nume = nume;
        this.media = media;
    }

    public String getNume() {
        return nume;
    }

    public float getMedia() {
        return media;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public void setMedia(float media) {
        this.media = media;
    }

    public String toString() {
        return "Student [nume=" + nume + ", media=" + media + "]";
    }

    @Override
    public boolean equals(Object obj) {
        // cand suprascriem equals trebuie sa suprascriem si hash
        if(obj == this)
            return true;

        if(obj == null || obj.getClass() != this.getClass())
            return false;

        Student student = (Student) obj;

        return nume.equals(student.getNume()) && Float.compare(media, student.getMedia()) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(nume, media);
    }

    @Override
    public int compareTo(Student o) {
        return this.nume.compareTo(o.getNume()) ;
    }
}
