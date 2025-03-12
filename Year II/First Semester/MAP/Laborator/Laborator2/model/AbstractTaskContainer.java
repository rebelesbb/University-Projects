package sem1_2.model;
import java.util.List;
import java.util.ArrayList;

public abstract class AbstractTaskContainer implements Container {
    List<Task> tasks = new ArrayList<>();

    @Override
    public abstract Task remove();

    @Override
    public void add(Task task) {
        tasks.add(task);
    }

    @Override
    public int size() {
        return tasks.size();
    }

    @Override
    public boolean isEmpty() {
        return tasks.isEmpty();
    }
}
