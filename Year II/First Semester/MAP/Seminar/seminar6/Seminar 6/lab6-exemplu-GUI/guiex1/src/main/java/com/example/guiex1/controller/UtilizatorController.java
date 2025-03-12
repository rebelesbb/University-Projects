package com.example.guiex1.controller;

import com.example.guiex1.domain.Utilizator;
import com.example.guiex1.domain.ValidationException;
import com.example.guiex1.services.UtilizatorService;
import com.example.guiex1.utils.events.UtilizatorEntityChangeEvent;
import com.example.guiex1.utils.observer.Observer;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Modality;
import javafx.stage.Stage;


import java.io.IOException;
import java.nio.FloatBuffer;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

public class UtilizatorController implements Observer<UtilizatorEntityChangeEvent> {
    UtilizatorService service;
    ObservableList<Utilizator> model = FXCollections.observableArrayList();

    @FXML
    private TextField firstNameTextField;
    @FXML
    private TextField lastNameTextField;


    @FXML
    TableView<Utilizator> tableView;
    @FXML
    TableColumn<Utilizator,String> tableColumnFirstName;
    @FXML
    TableColumn<Utilizator,String> tableColumnLastName;


    public void setUtilizatorService(UtilizatorService service) {
        this.service = service;
        service.addObserver(this);
        initModel();
    }

    @FXML
    public void initialize() {
        tableColumnFirstName.setCellValueFactory(new PropertyValueFactory<Utilizator, String>("firstName"));
        tableColumnLastName.setCellValueFactory(new PropertyValueFactory<Utilizator, String>("lastName"));
        tableView.setItems(model);

        // Add a listener to populate text fields when a row is selected
        tableView.getSelectionModel().selectedItemProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue != null) {
                populateTextFields(newValue);
            }
        });
    }

    private void populateTextFields(Utilizator utilizator) {
        firstNameTextField.setText(utilizator.getFirstName());
        lastNameTextField.setText(utilizator.getLastName());
    }

    private void initModel() {
        Iterable<Utilizator> messages = service.getAll();
        List<Utilizator> users = StreamSupport.stream(messages.spliterator(), false)
                .collect(Collectors.toList());
        model.setAll(users);
    }

    @Override
    public void update(UtilizatorEntityChangeEvent utilizatorEntityChangeEvent) {
        switch (utilizatorEntityChangeEvent.getType()){
            case ADD:
                model.add(utilizatorEntityChangeEvent.getData());
                break;
            case DELETE:
                model.remove(utilizatorEntityChangeEvent.getData());
            case UPDATE:
                Utilizator user = utilizatorEntityChangeEvent.getOldData();
                if(model.contains(user))
                    model.set(model.indexOf(user), utilizatorEntityChangeEvent.getData());
        }
    }

    public void handleDeleteUtilizator(ActionEvent actionEvent) {
        Utilizator user=(Utilizator) tableView.getSelectionModel().getSelectedItem();
        if (user!=null) {
            Utilizator deleted= service.deleteUtilizator(user.getId());
        }
    }

    public void handleAddUtilizator(ActionEvent actionEvent) throws IOException {
       // Utilizator selected = tableView.getSelectionModel().getSelectedItem();
        showAddTaskDialog();

    }

    public void handleUpdateUtilizator(ActionEvent actionEvent) throws IOException {
        Utilizator selectedUser = tableView.getSelectionModel().getSelectedItem();
        if (selectedUser!=null) {
            showMessageTextDialog(selectedUser);
        }
        else MessageAlert.showMessage(null, Alert.AlertType.ERROR, "Eroare", "Null Selection");
    }

    public void showAddTaskDialog() throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("../views/adduser-view.fxml"));

        AnchorPane root = (AnchorPane) loader.load();

        Stage dialogStage = new Stage();
        dialogStage.setTitle("Add User");
        dialogStage.initModality(Modality.WINDOW_MODAL);
        Scene scene = new Scene(root);
        dialogStage.setScene(scene);

        AddUserController editUserController = loader.getController();
        editUserController.setService(service, dialogStage);

        dialogStage.show();
    }


    public void showMessageTextDialog(Utilizator utilizator) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("../views/editmessagetask-view.fxml"));

        AnchorPane root = (AnchorPane) loader.load();

        Stage dialogStage = new Stage();
        dialogStage.setTitle("Edit User Data");
        dialogStage.initModality(Modality.WINDOW_MODAL);
        Scene scene = new Scene(root);
        dialogStage.setScene(scene);

        EditUserController editUserController = loader.getController();
        editUserController.setService(service, dialogStage, utilizator);

        dialogStage.show();
    }

}
