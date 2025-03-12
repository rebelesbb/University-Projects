namespace ConsoleApp1.Model;

public abstract class AbstractSortingTask
{
    public int [] Numbers{ get; set; }
    
    public abstract void Sort();
}