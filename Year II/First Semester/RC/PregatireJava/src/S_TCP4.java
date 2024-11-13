import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;
import java.nio.charset.StandardCharsets;

class MergeClientHandler extends Thread {
    Socket socket;

    public MergeClientHandler(Socket socket) {
        this.socket = socket;
    }

    private String merge(String a, String b) {
        StringBuilder c = new StringBuilder();
        int i = 0, j = 0, k = 0;
        while (i < a.length() && j < b.length()) {
            if(a.charAt(i) < b.charAt(j)) {
                c.insert(k, a.charAt(i));
                k++;
                i++;
            }
            else{
                c.insert(k, b.charAt(j));
                k++;
                j++;
            }
        }

        while(i < a.length()) {
            c.insert(k, a.charAt(i));
            k++;
            i++;
        }

        while(j < b.length()) {
            c.insert(k, b.charAt(j));
            k++;
            j++;
        }

        return c.toString();
    }

    @Override
    public void run() {
        byte[] buffer = new byte[1024];
        try {
            int bytesRead = socket.getInputStream().read(buffer);
            String string1 = new String(buffer, 0, bytesRead);
            System.out.println("Sir primit " + string1);

            buffer = new byte[1024];
            bytesRead = socket.getInputStream().read(buffer);
            String string2 = new String(buffer, 0, bytesRead);
            System.out.println("Sir primit " + string2);

            String mergedString = merge(string1, string2);
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            out.write(mergedString.getBytes());
            out.flush();

            socket.close();
        }
        catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}

public class S_TCP4 {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8888);
        int clientsCount = 1;

        while(clientsCount > 0){
            Socket socket = serverSocket.accept();
            System.out.println("Client " + socket.getInetAddress().toString() + " connected");
            Thread clientHandlerThread = new MergeClientHandler(socket);
            clientHandlerThread.start();
            clientsCount--;
        }

        serverSocket.close();
    }
}
