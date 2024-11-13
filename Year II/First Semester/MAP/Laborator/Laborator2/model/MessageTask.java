package sem1_2.model;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class MessageTask extends Task {

    private final String message;
    private final String from;
    private final String to;
    private final LocalDateTime date;

    public static DateTimeFormatter getDateFormatter() {
        return dateFormatter;
    }

    private static final DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

    public MessageTask(String taskId, String description, String message, String from, String to, LocalDateTime date) {
        super(taskId, description);
        this.message = message;
        this.from = from;
        this.to = to;
        this.date = date;
    }

    @Override
    public void execute() {
        System.out.println(date.format(dateFormatter) + ": " + message);
    }

    @Override
    public String toString() {
        return "id = " + getId() +
                " | description = " + getDescription() +
                " | message = " + message +
                " | from = " + from +
                " | to = " + to +
                " | date = " + date.format(dateFormatter);
    }
}
