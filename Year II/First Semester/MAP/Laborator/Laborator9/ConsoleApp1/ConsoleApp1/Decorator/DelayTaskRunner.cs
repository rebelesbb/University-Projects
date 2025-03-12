namespace ConsoleApp1.Decorator;

public class DelayTaskRunner: AbstractTaskRunner
{
    public DelayTaskRunner(TaskRunner taskRunner) : base(taskRunner) { }

    public override void ExecuteOneTask()
    {
        TaskRunner.ExecuteOneTask();
        try
        {
            Thread.Sleep(3000);
        }
        catch (Exception exception)
        {
            Console.WriteLine(exception.Message);
        }
    }
}