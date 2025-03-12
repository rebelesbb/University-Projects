package sem1_2.model;

public class MergeSorter extends AbstractSorter {
    public MergeSorter(int[] numbers) {
        super(numbers);
    }

    private void merge(int[] arr1, int[] arr2, int[] mergedArr) {
        int i = 0, j = 0, k=0;
        while(i < arr1.length && j < arr2.length){
            if(arr1[i] < arr2[j]){
                mergedArr[k++] = arr1[i++];
            }
            else{
                mergedArr[k++] = arr2[j++];
            }
        }

        while(i < arr1.length){
            mergedArr[k++] = arr1[i++];
        }
        while(j < arr2.length){
            mergedArr[k++] = arr2[j++];
        }
    }

    private void mergeSort(int[] nums){
        if(nums.length < 2)
            return;

        int mid = nums.length / 2;
        int[] left = new int[mid];
        int[] right = new int[nums.length - mid];

        for(int i = 0; i < mid; i++)
            left[i] = nums[i];

        for(int i = mid; i < nums.length; i++)
            right[i - mid] = nums[i];

        mergeSort(left);
        mergeSort(right);

        merge(left, right, nums);
    }

    @Override
    public void sort() {
        mergeSort(numbers);
    }
}
