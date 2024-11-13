package sem1_2.decorator;

import java.time.Duration;

public class DelayTaskRunner extends AbstractTaskRunner{

    public DelayTaskRunner(TaskRunner taskRunner) {
        super(taskRunner);
    }

    @Override
    public void executeOneTask() {
        try{
            Thread.sleep(Duration.ofSeconds(3));
            super.executeOneTask();
        }
        catch(InterruptedException e){
            System.out.println(e.getMessage());
        }
    }
}
