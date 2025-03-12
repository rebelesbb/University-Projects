package domain;

import java.time.LocalDate;

public class Nota {
    private Student student;
    private Tema tema;
    LocalDate data;
    double value;
    String profesor;

    public Nota(Student student, Tema tema, double value, LocalDate data, String profesor) {
        this.student = student;
        this.tema = tema;
        this.value = value;
        this.data = data;
        this.profesor = profesor;
    }

    public Student getStudent() {
        return student;
    }

    public Tema getTema() {
        return tema;
    }

    public double getValue() {
        return value;
    }

    public String getProfesor() {
        return profesor;
    }
}
