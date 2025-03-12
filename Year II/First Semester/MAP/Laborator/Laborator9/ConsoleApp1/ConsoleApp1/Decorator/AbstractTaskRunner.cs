using Task = ConsoleApp1.Model.Task;

namespace ConsoleApp1.Decorator;

public abstract class AbstractTaskRunner: TaskRunner
{
    protected readonly TaskRunner TaskRunner;

    public AbstractTaskRunner(TaskRunner taskRunner)
    {
        TaskRunner = taskRunner;
    }

    public void AddTask(Task task)
    {
        TaskRunner.AddTask(task);
    }

    public bool HasTasks()
    {
        return TaskRunner.HasTasks();
    }

    public abstract void ExecuteOneTask();

    public void ExecuteAll()
    {
        while (HasTasks())
        {
            ExecuteOneTask();
        }
    }
}