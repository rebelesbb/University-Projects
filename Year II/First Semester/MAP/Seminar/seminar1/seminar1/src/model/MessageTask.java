package model;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class MessageTask extends Task {
    private String message;
    private String from;
    private String to;
    private LocalDateTime date;

    private static DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

    public MessageTask(String message, String from, String to, LocalDateTime date, String taskId, String description){
        super(taskId, description);
        this.message = message;
        this.from = from;
        this.to = to;
        this.date = date;
    }

    @Override
    public void execute() {
        System.out.println("mesaj="+message+"| date="+date.format(formatter));

    }
    //id=1 | description=Feedback lab1| message=Ai obtinut 9.60 | from=Maria | to=Ana | date=2018-09-27 09:29

    public String toString(){
        return "id="+this.getTaskId() +"|description=" + this.getDescription() + "|message=" + message + "|from="
                + from + "|to =" + to + "|date =" + date.format(formatter);
    }
}