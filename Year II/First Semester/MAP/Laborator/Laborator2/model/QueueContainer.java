package sem1_2.model;

public class QueueContainer extends AbstractTaskContainer {
    @Override
    public Task remove(){
        if(!tasks.isEmpty())
            return tasks.remove(0);
        return null;
    }
}

/*
before extracting superclass

public class QueueContainer implements Container{
    private final List<Task> tasks = new ArrayList<Task>();

    @Override
    public Task remove() {
        if(!tasks.isEmpty())
            return tasks.remove(0);
        else return null;
    }

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
*/