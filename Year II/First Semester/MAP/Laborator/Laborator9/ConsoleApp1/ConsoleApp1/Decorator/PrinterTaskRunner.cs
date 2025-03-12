namespace ConsoleApp1.Decorator;

public class PrinterTaskRunner: AbstractTaskRunner
{
    public PrinterTaskRunner(TaskRunner taskRunner) : base(taskRunner) { }

    public override void ExecuteOneTask()
    {
        TaskRunner.ExecuteOneTask();
        Console.WriteLine($"Task completed at {DateTime.Now.Hour}");
    }
}