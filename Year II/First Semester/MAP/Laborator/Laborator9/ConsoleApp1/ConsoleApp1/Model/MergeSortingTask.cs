namespace ConsoleApp1.Model;

public class MergeSortingTask: AbstractSortingTask
{

    private int[] Merge(int[] numbersListOne, int[] numbersListTwo)
    {
        int[] mergedList = new int[numbersListOne.Length + numbersListTwo.Length];
        int i = 0, j = 0, k = 0;
        while (i < numbersListOne.Length && j < numbersListTwo.Length)
        {
            if(numbersListOne[i] < numbersListTwo[j])
                mergedList[k++] = numbersListOne[i++];
            else mergedList[k++] = numbersListTwo[j++];
        }

        while (i < numbersListOne.Length) mergedList[k++] = numbersListOne[i++];
        while (j < numbersListTwo.Length) mergedList[k++] = numbersListTwo[j++];
        
        return mergedList;
    }

    private int[] MergeSort(int[] numbersList)
    {
        if (numbersList.Length < 2)
            return numbersList;
        int middle = numbersList.Length / 2;
        int[] left = numbersList.Take(middle).ToArray();
        int[] right = numbersList.Skip(middle).ToArray();
        return Merge(MergeSort(left), MergeSort(right));
    }
    public override void Sort()
    {
        int[] sortedNums = MergeSort(Numbers);
        Console.WriteLine("\nMerge Sorting Task Completed. Sorted Numbers:");
        foreach (int number in sortedNums)
        {
            Console.Write(number + " ");
        }
    }
}