namespace ConsoleApp1.Model;

public class BubbleSortingTask: AbstractSortingTask
{

    public override void Sort()
    {
        bool sorted;
        do
        {
            sorted = true;
            
            for(int i = 0; i < Numbers.Length - 1; i++)
                if (Numbers[i] > Numbers[i + 1])
                {
                    (Numbers[i], Numbers[i + 1]) = (Numbers[i + 1], Numbers[i]);
                    sorted = false;
                }
        }
        while(!sorted);

        Console.WriteLine("\nBubble Sorting Task Completed. Sorted numbers:");
        foreach (int number in Numbers)
        {
            Console.Write(number + " ");
        }
    }
}