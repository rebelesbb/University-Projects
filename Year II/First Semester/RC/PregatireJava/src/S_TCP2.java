import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

// Un client trimite unui server un sir de caractere.
// Serverul va returna clientului numarul de caractere spatiu din sir.

class StringClientHandler extends Thread {
    private Socket socket;

    public StringClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
       byte[] buffer = new byte[1024];

       try{
           int bytesRead = socket.getInputStream().read(buffer);
           String string = new String(buffer, 0, bytesRead);
           System.out.println("Clientul a trimis sirul de caractere:\n" + string);

           int spacesCount = string.split(" ").length - 1;

           DataOutputStream out = new DataOutputStream(socket.getOutputStream());
           out.write(Integer.toString(spacesCount).getBytes());
           out.flush();

           socket.close();
       }
       catch(Exception e){
           System.out.println(e.getMessage());
       }
    }
}

public class S_TCP2 {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8888);
        int clientsCount = 2;
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
