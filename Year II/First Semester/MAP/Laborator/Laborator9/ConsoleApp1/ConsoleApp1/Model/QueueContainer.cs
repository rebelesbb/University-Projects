namespace ConsoleApp1.Model;

public class QueueContainer: AbstractTaskContainer
{
    public override Task Remove()
    {
        if(Tasks.Count == 0)
            throw new InvalidOperationException("Stack container is empty");
        
        Task removedTask = Tasks[0];
        Tasks.RemoveAt(0);
        
        return removedTask;
    }
}