namespace ConsoleApp1.Model;

public abstract class AbstractTaskContainer: Container
{
    protected readonly List<Task> Tasks = [];

    public void Add(Task task)
    {
        Tasks.Add(task);
    }

    public bool Empty()
    {
        return Tasks.Count == 0;
    }

    public int Size()
    {
        return Tasks.Count;
    }

    public abstract Task Remove();
}