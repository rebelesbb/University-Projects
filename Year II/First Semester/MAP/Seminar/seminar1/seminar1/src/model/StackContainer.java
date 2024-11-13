package model;

import java.util.ArrayList;

public class StackContainer implements Container {

    private ArrayList<Task> tasks;

    public StackContainer() {
        this.tasks = new ArrayList<>();
    }

    @Override
    public Task remove() {
        if(isEmpty())
            return null;
        else {
            return tasks.remove(size() - 1);
        }
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

