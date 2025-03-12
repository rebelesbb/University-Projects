package model;

import java.util.Objects;

public abstract class Task {
    private String taskId;
    private String description;

    public Task(String taskId, String description){
        this.taskId = taskId;
        this.description = description;
    }

    public void setTaskId(String taskId) {
        this.taskId = taskId;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getTaskId() {
        return taskId;
    }

    public String getDescription() {
        return description;
    }

    public abstract void execute();

    @Override
    public String toString() {
        return "id="+taskId+"| description="+ description;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true; // If the two objects are the same instance
        }
        if (obj == null || this.getClass() != obj.getClass()) {
            return false; // If the object is null or not of the same class
        }
        Task task = (Task) obj; // Cast obj to Task
        return Objects.equals(taskId, task.taskId);

        //return super.equals(obj); //this implementation calls the equals method of the superclass
        // (in this case, Object), meaning it uses the default behavior.
        // The default behavior is reference comparison, i.e., it checks if both objects refer to the same memory location.
    }

    @Override
    public int hashCode() {
        return Objects.hash(taskId);
    }
}
