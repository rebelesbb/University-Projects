package decorator;

import factory.ContainerFactory;
import factory.Strategy;
import model.Container;
import model.Task;

public class StrategyTaskRunner implements TaskRunner {
    private Container container;

    public StrategyTaskRunner(Strategy strategy) {
        ContainerFactory containerFactory = new ContainerFactory();
        container = containerFactory.createContainer(strategy);
    }

    @Override
    public void executeOneTask() {
        if (hasTask()) {
            Task removedTask = container.remove();
            removedTask.execute();
        }
        else {
            System.out.println("There are no tasks!");
        }
    }

    @Override
    public void executeAll() {
        while (hasTask()) {
            executeOneTask();
        }
    }

    @Override
    public void addTask(Task t) {
        container.add(t);
    }

    @Override
    public boolean hasTask() {
        return !container.isEmpty();
    }
}
