import java.io.*;
import java.net.*;

public class Main {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket;
        try {
            serverSocket = new ServerSocket(8888);
            byte[] buff = new byte[1024];
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected" + clientSocket.getInetAddress());
                int bytesRead = clientSocket.getInputStream().read(buff);
                System.out.println(new String(buff, 0, bytesRead));
                break;
            }

            serverSocket.close();
        } catch (IOException e) {
            System.err.println("Could not listen on port: 8888");
        }


    }
}
