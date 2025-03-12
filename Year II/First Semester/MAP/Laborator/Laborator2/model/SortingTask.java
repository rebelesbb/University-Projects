package sem1_2.model;

public class SortingTask extends Task{
    int[] numbers;
    AbstractSorter sorter;
    SortingStrategy strategy;

    public SortingTask(String id, String description, int[] numbers, SortingStrategy strategy) {
        super(id, description);
        this.numbers = numbers;
        this.strategy = strategy;

        if(strategy == SortingStrategy.BUBBLE) {
            sorter = new BubbleSorter(numbers);
        }
        else sorter = new MergeSorter(numbers);
    }

    @Override
    public void execute(){
        sorter.sort();
        for(int number : numbers) {
            System.out.print(number + " ");
        }
        System.out.println();
    }
}
