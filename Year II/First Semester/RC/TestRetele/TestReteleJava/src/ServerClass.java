import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Random;

class ClientHandler extends Thread{
    Socket clientOneSocket;
    Socket clientTwoSocket;

    int n = 0;

    public ClientHandler(Socket socket1, Socket socket2) {
        this.clientOneSocket = socket1;
        this.clientTwoSocket = socket2;

    }

    synchronized private int generateID(){
        return n + 1;
    }

    private boolean checkFazan(String previousWord, String word, int round){
        if(round == 1){
            if(word.charAt(0) == previousWord.charAt(0)){
                return true;
            }
            else{
                if(word.charAt(word.length()-1) == previousWord.charAt(word.length()-1)
                && word.charAt(word.length()-2) == previousWord.charAt(word.length()-2)){
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public void run() {

        int currentID = generateID();

        try {

            DataOutputStream outClientOne = null, outClientTwo;
            outClientOne = new DataOutputStream(clientOneSocket.getOutputStream());
            outClientTwo = new DataOutputStream(clientTwoSocket.getOutputStream());

            System.out.println("Current game ID: " + currentID);
            outClientOne.write(Integer.toString(currentID).getBytes());
            outClientOne.flush();
            outClientTwo.write(Integer.toString(currentID).getBytes());
            outClientTwo.flush();

            Random rnd = new Random();
            char c = (char) ('a' + rnd.nextInt(26));

            System.out.println("Game starts with :" + c);
            outClientOne.write(Character.toString(c).getBytes());
            outClientOne.flush();

            outClientTwo.write(Character.toString(c).getBytes());
            outClientTwo.flush();


            int currentPlayerId = 1, counter = 0, round = 1;
            boolean isGameFinished = false;
            String PreviousWord = new String(Character.toChars(c));

            outClientOne.write(new String("Y").getBytes());
            outClientOne.flush();
            outClientTwo.write(new String("N").getBytes());
            outClientTwo.flush();


            while(!isGameFinished){
                int bytesRead;
                byte[] buffer;
                counter++;
                if(currentPlayerId == 1){

                    buffer = new byte[1024];
                    bytesRead = clientOneSocket.getInputStream().read(buffer);
                    String receivedWord = new String(buffer, 0, bytesRead);
                    System.out.println("Received word from client one: " + receivedWord);
                    outClientTwo.write(receivedWord.getBytes());

                    currentPlayerId = 2;
                }
                else if(currentPlayerId == 2){

                    buffer = new byte[1024];
                    bytesRead = clientTwoSocket.getInputStream().read(buffer);
                    String receivedWord = new String(buffer, 0, bytesRead);
                    outClientOne.write(receivedWord.getBytes());
                    System.out.println("Received word from client two: " + receivedWord);
                    outClientTwo.flush();
                    outClientTwo.flush();
                    currentPlayerId = 1;

                }
            }


        } catch (IOException e) {
            System.out.println("Error: " + e);
        }


        try {
            clientOneSocket.close();
        } catch (IOException e) {
            System.out.println("Error closing client one socket");
        }

        try {
            clientTwoSocket.close();
        } catch (IOException e) {
            System.out.println("Error closing client two socket");
        }
    }

}

public class ServerClass {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8888);
        int clientCount = 5;
        while (clientCount > 0) {
            Socket clientOneSocket = serverSocket.accept();
            System.out.println("Connected by " + clientOneSocket.getInetAddress());
            Socket clientTwoSocket = serverSocket.accept();
            System.out.println("Connected by " + clientTwoSocket.getInetAddress());
            Thread clientHandler = new ClientHandler(clientOneSocket, clientTwoSocket);
            clientHandler.start();
            clientCount--;
        }
        serverSocket.close();
    }
}
