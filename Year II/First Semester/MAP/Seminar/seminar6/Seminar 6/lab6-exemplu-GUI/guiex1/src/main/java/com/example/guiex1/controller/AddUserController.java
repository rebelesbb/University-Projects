package com.example.guiex1.controller;

import com.example.guiex1.domain.Utilizator;
import com.example.guiex1.domain.ValidationException;
import com.example.guiex1.services.UtilizatorService;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class AddUserController {
    @FXML
    private TextField textFieldFirstName;
    @FXML
    private TextField textFieldLastName;


    private UtilizatorService service;
    Stage dialogStage;
    Utilizator utilizator;

    @FXML
    private void initialize() {
    }

    public void setService(UtilizatorService service,  Stage stage) {
        this.service = service;
        this.dialogStage=stage;
    }

    @FXML
    public void handleSave(){
        String firstNameText= textFieldFirstName.getText();
        String lastNameText= textFieldLastName.getText();

        Utilizator utilizator1=new Utilizator(firstNameText,lastNameText);
        saveMessage(utilizator1);

    }

    private void saveMessage(Utilizator m)
    {
        // TODO
        try {
            Utilizator r= this.service.addUtilizator(m);
            if (r==null)
                dialogStage.close();
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION,"Slavare user","Mesajul a fost salvat");
        } catch (ValidationException e) {
            MessageAlert.showErrorMessage(null,e.getMessage());
        }
        dialogStage.close();

    }

    private void clearFields() {
        textFieldFirstName.setText("");
        textFieldLastName.setText("");

    }
    private void setFields(Utilizator u)
    {
        textFieldFirstName.setText(u.getFirstName());
        textFieldLastName.setText(u.getLastName());

    }

    @FXML
    public void handleCancel(){
        dialogStage.close();
    }
}
