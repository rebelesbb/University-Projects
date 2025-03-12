package sem1_2.model;

public abstract class AbstractSorter {
    int[] numbers;

    AbstractSorter(int[] numbers) {
        this.numbers = numbers;
    }

    public abstract void sort();
}
