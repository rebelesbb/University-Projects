namespace ConsoleApp1.Model;

public class MessageTask: Task
{
    private string Message { get; set; }
    private string From { get; set; }
    private string To { get; set; }
    private DateTime Date { get; set; }
    
    public MessageTask(string taskId, string taskDescription, string message, string from, string to, DateTime date): base(taskId, taskDescription)
    {
        Message = message;
        From = from;
        To = to;
        Date = date;
    }

    public override void Execute()
    {
        Console.WriteLine($"\nFrom: {From} To: {To}\nMessage: {Message}\nDate: {Date}");
    }
}