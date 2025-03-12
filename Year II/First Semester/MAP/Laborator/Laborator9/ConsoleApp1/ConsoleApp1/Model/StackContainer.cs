namespace ConsoleApp1.Model;

public class StackContainer: AbstractTaskContainer
{
    public override Task Remove()
    {
        if(Tasks.Count == 0)
            throw new InvalidOperationException("Stack container is empty");
        
        Task removedTask = Tasks[Tasks.Count - 1];
        Tasks.RemoveAt(Tasks.Count - 1);
        
        return removedTask;
    }
}