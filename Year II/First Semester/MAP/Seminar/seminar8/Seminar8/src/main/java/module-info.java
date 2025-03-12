module com.example.seminar8 {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;

    opens com.example.seminar8 to javafx.fxml;
    opens com.example.seminar8.controller to javafx.fxml;
    opens com.example.seminar8.domain to javafx.base;
    exports com.example.seminar8;
}
