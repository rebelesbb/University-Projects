package sem1_2;

import sem1_2.decorator.DelayTaskRunner;
import sem1_2.decorator.PrinterTaskRunner;
import sem1_2.decorator.StrategyTaskRunner;
import sem1_2.decorator.TaskRunner;
import sem1_2.factory.Strategy;
import sem1_2.model.MessageTask;
import sem1_2.model.SortingStrategy;
import sem1_2.model.SortingTask;

import java.time.LocalDateTime;

public class Sem1_2Test {

    public static MessageTask[] createMessages() {
        MessageTask msg1 = new MessageTask("1", "feedback lab 2", "Te-ai descurcat bine", "teacher", "student", LocalDateTime.now());
        MessageTask msg2 = new MessageTask("2", "feedback lab 3", "Te-ai descurcat bine", "teacher", "student", LocalDateTime.now());
        MessageTask msg3 = new MessageTask("3", "feedback lab 4", "Te-ai descurcat bine", "teacher", "student", LocalDateTime.now());
        MessageTask msg4 = new MessageTask("4", "feedback lab 5", "Te-ai descurcat bine", "teacher", "student", LocalDateTime.now());
        MessageTask msg5 = new MessageTask("5", "feedback lab 6", "Te-ai descurcat bine", "teacher", "student", LocalDateTime.now());

        return new MessageTask[]{msg1, msg2, msg3, msg4, msg5};
    }

    public static void testStrategyPrinterTaskRunners(String[] args){
        TaskRunner strategyTaskRunner = new StrategyTaskRunner(Strategy.valueOf(args[0]));
        for (MessageTask m : createMessages()) {
            strategyTaskRunner.addTask(m);
        }
        strategyTaskRunner.executeAll();

        for (MessageTask m : createMessages()) {
            strategyTaskRunner.addTask(m);
        }

        TaskRunner printerTaskRunner = new PrinterTaskRunner(strategyTaskRunner);
        printerTaskRunner.executeAll();

    }

    public static void testAllTaskRunners(String[] args){
        TaskRunner strategyTaskRunner = new StrategyTaskRunner(Strategy.valueOf(args[0]));
        for (MessageTask m : createMessages()) {
            strategyTaskRunner.addTask(m);
        }
        strategyTaskRunner.executeAll();

        for (MessageTask m : createMessages()) {
            strategyTaskRunner.addTask(m);
        }

        TaskRunner printerTaskRunner = new PrinterTaskRunner(strategyTaskRunner);
        printerTaskRunner.executeAll();

        for (MessageTask m : createMessages()) {
            strategyTaskRunner.addTask(m);
        }

        TaskRunner delayTaskRunner = new DelayTaskRunner(strategyTaskRunner);
        delayTaskRunner.executeAll();

    }

    public static void testSorting(){
        SortingTask st1 = new SortingTask("1", "Sorter using BubbleSort", new int[]{4, 2, 3, -1, -7, 0},SortingStrategy.BUBBLE  );
        SortingTask st2 = new SortingTask("2", "Sorter using MergeSort", new int[]{4, 2, 3, -1, -7, 0}, SortingStrategy.MERGE);

        st1.execute();
        st2.execute();
    }


    public static void main(String[] args) {
        MessageTask[] messageTasks = createMessages();
        for (MessageTask messageTask: messageTasks) {
            System.out.println(messageTask);
        }

        testStrategyPrinterTaskRunners(args);

        testSorting();

        testAllTaskRunners(args);
    }
}
