using ConsoleApp1.Model;

namespace ConsoleApp1.Factory;

public class TaskContainerFactory: Factory
{
    private TaskContainerFactory() { }
    private static TaskContainerFactory _instance;
    public static TaskContainerFactory FactoryInstance => _instance ??= new TaskContainerFactory();

    public Container createContainer(Strategy strategy)
    {
        if (strategy == Strategy.Lifo)
            return new StackContainer();
        return new QueueContainer();
    }
    
}