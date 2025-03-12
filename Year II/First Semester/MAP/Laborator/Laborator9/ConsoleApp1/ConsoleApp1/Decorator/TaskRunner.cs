using Task = ConsoleApp1.Model.Task;
namespace ConsoleApp1.Decorator;

public interface TaskRunner
{
    void ExecuteOneTask();
    void ExecuteAll();
    void AddTask(Task task);
    bool HasTasks();
}