using ConsoleApp1.Factory;
using ConsoleApp1.Model;
using Task = ConsoleApp1.Model.Task;

namespace ConsoleApp1.Decorator;

public class StrategyTaskRunner: TaskRunner
{
    private readonly Container _container;

    public StrategyTaskRunner(Strategy strategy)
    {
        _container = TaskContainerFactory.FactoryInstance.createContainer(strategy);
    }

    public void AddTask(Task task)
    {
        _container.Add(task);
    }

    public bool HasTasks()
    {
        return !(_container.Empty());
    }

    public void ExecuteOneTask()
    {
        _container.Remove().Execute();
    }

    public void ExecuteAll()
    {
        while (HasTasks())
            ExecuteOneTask();
    }
}