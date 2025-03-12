import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Supplier;

public class SupplierTest {
    public static void main(String[] args){
        Supplier<List> listSupplier1 = () -> new ArrayList();
        Supplier<List> listSupplier2 = ArrayList::new;


        Supplier<LocalDateTime> dateTimeSupplier1 = () -> LocalDateTime.now();
        Supplier<LocalDateTime> dateTimeSupplier2 = LocalDateTime::now;

        LocalDateTime date1 = dateTimeSupplier1.get();
        LocalDateTime date2 = dateTimeSupplier2.get();

        System.out.println(date1);
        System.out.println(date2);

    }
}
