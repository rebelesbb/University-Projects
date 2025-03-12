import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

class ClientHandler extends Thread{
    Socket socket;
    public ClientHandler(Socket s){
        this.socket = s;
    }

    @Override
    public void run(){
        byte[] buff = new byte[1024];
        int bytesRead = 0;

        try {
            bytesRead = socket.getInputStream().read(buff);
        } catch (IOException e) {
            System.out.println("Error reading number count from client");
        }

        int n = Integer.parseInt(new String(buff, 0, bytesRead));
        System.out.println("Clientul va trimite " + n + " numere");
        int sum = 0;

        for (int i = 0; i < n; i++) {
            buff = new byte[1024];
            try {
                bytesRead = socket.getInputStream().read(buff);
                int currentNum = Integer.parseInt(new String(buff, 0, bytesRead));
                System.out.println("Numar primit " + currentNum);
                sum += currentNum;
            }
            catch (IOException e) {
                System.out.println("Error reading number from client");
            }
        }

        try {
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            out.write(Integer.toString(sum).getBytes());
            out.flush();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        try {
            socket.close();
        } catch (IOException e) {
            System.out.println("Error closing client socket");
        }
    }
}

public class S_TCP1 {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8888, 1);
        int clientsCount = 1;

        while(clientsCount > 0){
            Socket socket = serverSocket.accept();
            System.out.println("Client " + socket.getInetAddress().toString() + " connected");
            Thread clientThread = new StringClientHandler(socket);
            clientThread.start();
            clientsCount--;
        }

        serverSocket.close();
    }
}
