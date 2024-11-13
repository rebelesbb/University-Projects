package ui;

import domain.User;
import service.SocialNetworkService;

public class Console {
    private final SocialNetworkService service;

    public Console(SocialNetworkService service) {
        this.service = service;
    }

    private void printMenu(){
        System.out.println("1. Add User");
        System.out.println("2. Remove User");
        System.out.println("3. Add Friendship");
        System.out.println("4. Remove Friendship");
        System.out.println("5. Number of communities");
        System.out.println("6. Most sociable community");
        System.out.println("U. Print Users");
        System.out.println("F. Print Friendships");
        System.out.println("E. Exit");
    }

    private void printUsers(){
        System.out.println("USERS:");
        service.getUsers().forEach(System.out::println);
    }

    private void printFriendships(){
        System.out.println("FRIENDSHIPS:");
        service.getPrintableFriendships().forEach(System.out::println);
    }


    private void addUserUI(){
        System.out.print("Enter First Name: ");
        String firstName = System.console().readLine();
        System.out.print("Enter Last Name: ");
        String lastName = System.console().readLine();
        System.out.print("Enter Email: ");
        String email = System.console().readLine();
        System.out.print("Enter Password: ");
        String password = System.console().readLine();
        try{
            service.addUser(firstName, lastName, email, password);
            System.out.println("User added!");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }

    private void removeUserUI(){
        System.out.print("Enter ID: ");
        String id = System.console().readLine();
        try {
            service.deleteUser(Long.parseLong(id));
            System.out.println("User deleted!");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }

    private void addFriendUI(){
        System.out.print("Enter first user ID: ");
        String firstUserID = System.console().readLine();
        System.out.print("Enter second user ID: ");
        String secondUserID = System.console().readLine();
        try{
            service.addFriend(Long.parseLong(firstUserID), Long.parseLong(secondUserID));
            System.out.println("Friend added!");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }

    private void removeFriendUI(){
        System.out.print("Enter first user ID: ");
        String firstUserID = System.console().readLine();
        System.out.print("Enter second user ID: ");
        String secondUserID = System.console().readLine();
        try{
            service.removeFriend(Long.parseLong(firstUserID), Long.parseLong(secondUserID));
            System.out.println("Friend removed!");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }

    private void communitiesCountUI(){
        System.out.println("The number of communities is: " + service.communitiesCount());
    }

    private void mostSociableCommunityUI(){
        System.out.print("The most sociable community is: ");
        service.biggestCommunity().forEach(System.out::println);
    }

    public void run(){
        while(true) {
            printMenu();
            System.out.print("Enter your choice: ");
            String option = System.console().readLine();

            if(option != null) {
                if (Character.isAlphabetic(option.charAt(0))) {
                    option = option.toUpperCase();
                }
            }

            switch (option){
                case "1":
                    addUserUI();
                    break;
                case "2":
                    removeUserUI();
                    break;
                case "3":
                    addFriendUI();
                    break;
                case "4":
                    removeFriendUI();
                    break;
                case "5":
                    communitiesCountUI();
                    break;
                case "6":
                    mostSociableCommunityUI();
                    break;
                case "U":
                    printUsers();
                    break;
                case "F":
                    printFriendships();
                    break;
                case "E":
                    return;
                case null:
                    System.out.println("Choice cannot be null");
                    break;
                default:
                    System.out.println("Invalid choice");
                    break;
            }
            System.out.println();
        }
    }
}
