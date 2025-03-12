package sem1_2.model;

public class BubbleSorter extends  AbstractSorter{
    public BubbleSorter(int[] numbers) {
        super(numbers);
    }

    private void bubbleSort(int[] nums) {
        int i, temp;
        boolean sorted;
        do{
            sorted = true;
            for(i = 0; i < nums.length - 1; i++){
                if(nums[i] > nums[i+1]){
                    temp = nums[i];
                    nums[i] = nums[i+1];
                    nums[i+1] = temp;
                    sorted = false;
                }
            }

        }while(!sorted);
    }

    @Override
    public void sort() {
        bubbleSort(numbers);
    }
}
