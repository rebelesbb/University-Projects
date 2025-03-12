
using ConsoleApp1.Decorator;
using ConsoleApp1.Factory;

namespace ConsoleApp1;

using Model;
public class Program
{
    private static List<Task> GenerateMessageTasks(int numberToGenerate)
    {
        List<Task> tasks = new List<Task>();
        while (numberToGenerate > 0)
        {
            tasks.Add(new MessageTask("Id" + numberToGenerate.ToString(), 
                "Description" + numberToGenerate.ToString(),
                "Message" + numberToGenerate.ToString(),
                "Sender Name" + numberToGenerate.ToString(),
                "Receiver Name" + numberToGenerate.ToString(),
                DateTime.Now));
            numberToGenerate--;
        }
        return tasks;
    }

    private static void TestMessageTaskExecution()
    {
        Console.WriteLine("\n\n--- STARTING MESSAGE TASK EXECUTION TEST ---");
        var tasks = GenerateMessageTasks(5);
        tasks.ForEach(t => t.Execute());
    }

    private static void TestStrategyRunnerExecution(string strategy)
    {
        Console.WriteLine("\n\n--- STARTING STRATEGY TASK RUNNER TEST ---");
        Console.WriteLine($"Strategy: {strategy}");
        
        var tasks = GenerateMessageTasks(5);
        var taskRunner = strategy.Equals("Fifo") ? new StrategyTaskRunner(Strategy.Fifo) : new StrategyTaskRunner(Strategy.Lifo);
        tasks.ForEach(task => taskRunner.AddTask(task));
        
        taskRunner.ExecuteAll();
    }

    private static void TestAllTaskRunners(string strategy)
    {
        Console.WriteLine("\n\n--- STARTING ALL TASK RUNNER TEST ---");
        Console.WriteLine($"Strategy: {strategy}");
        var tasks = GenerateMessageTasks(5);
        
        Console.WriteLine("\n-- Using strategy task runner --");
        var strategyTaskRunner = strategy.Equals("Fifo") ? new StrategyTaskRunner(Strategy.Fifo) : new StrategyTaskRunner(Strategy.Lifo);
        tasks.ForEach(task => strategyTaskRunner.AddTask(task));
        strategyTaskRunner.ExecuteAll();

        Console.WriteLine("\n-- Using printer task runner --");
        tasks.ForEach(task => strategyTaskRunner.AddTask(task));
        AbstractTaskRunner printerTaskRunner = new PrinterTaskRunner(strategyTaskRunner);
        printerTaskRunner.ExecuteAll();
        
        Console.WriteLine("\n-- Using delay task runner --");
        tasks.ForEach(task => strategyTaskRunner.AddTask(task));
        AbstractTaskRunner delayTaskRunner = new DelayTaskRunner(strategyTaskRunner);
        delayTaskRunner.ExecuteAll();
    }

    public static void TestSortingTasks()
    {
        Console.WriteLine("\n\n--- STARTING SORTING TASK TEST ---");
        
        SortingTask bubbleSortingTask = new SortingTask("1", "Sorting numbers using bubble sort", [10, 9, 8, -3, -10, 7, 6, 5, 4, -100, 3, 2, 1], new BubbleSortingTask());
        bubbleSortingTask.Execute();
        
        SortingTask mergeSortingTask = new SortingTask("2", "Sorting numbers unsing merge sort", [10, 9, 8, -3, -10, 7, 6, 5, 4, -100, 3, 2, 1], new MergeSortingTask());
        mergeSortingTask.Execute();
    }
    
    public static void Main(string[] args)
    {
        TestSortingTasks();
        TestMessageTaskExecution();
        TestStrategyRunnerExecution(args[0]);
        TestStrategyRunnerExecution(args[1]);
        TestAllTaskRunners(args[0]);
        TestAllTaskRunners(args[1]);
    }
}