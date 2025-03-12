namespace ConsoleApp1.Model;

public class SortingTask: Task
{
    protected int[] Numbers;
    private AbstractSortingTask AbstractSortingTask { get; set; }

    public SortingTask(string taskId, string taskDescription, int[] numbers, AbstractSortingTask abstractSortingTask) : base(taskId, taskDescription)
    {
        Numbers = numbers;
        AbstractSortingTask = abstractSortingTask;
        this.AbstractSortingTask.Numbers = numbers;
    }

    public override void Execute()
    {
        try
        {
            this.AbstractSortingTask.Sort();
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
    }
    
}