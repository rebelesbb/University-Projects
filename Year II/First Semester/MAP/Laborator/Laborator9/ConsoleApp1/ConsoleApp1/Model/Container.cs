namespace ConsoleApp1.Model;

public interface Container
{
    Task Remove();
    void Add(Task task);
    int Size();
    bool Empty();
}