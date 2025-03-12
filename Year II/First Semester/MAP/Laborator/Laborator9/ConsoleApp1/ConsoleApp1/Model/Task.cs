namespace ConsoleApp1.Model;

public abstract class Task
{
    protected string TaskId{get;set;}
    protected string Description{get;set;}

    protected Task(string taskId, string description)
    {
        this.TaskId = taskId;
        this.Description = description;
    }

    public abstract void Execute();

    public override bool Equals(object? obj)
    {
        if(obj == null) return false;
        if(obj is not Task) return false;
        if (obj is Task otherTask)
            return this.TaskId == otherTask.TaskId;
        return false;
    }

    public override int GetHashCode()
    {
        return TaskId.GetHashCode();
    }

    public override string ToString()
    {
        return $"TaskId: [{TaskId}, Description: {Description}]";
    }
}