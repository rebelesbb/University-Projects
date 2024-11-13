import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;
import java.util.Vector;

record Pair<Type1, Type2>(Type1 first, Type2 second) {
}

class CharClientHandler extends Thread {
    Socket sock;

    public CharClientHandler(Socket sock) {
        this.sock = sock;
    }

    @Override
    public void run() {
        Pair<Vector<Integer>, Vector<Integer>> arrays = readArrays();
        System.out.println("Arrays received:\n" + arrays);

        StringBuilder requestedNums = new StringBuilder();

        for(Integer num : arrays.first())
            if(!arrays.second().contains(num)) {
                requestedNums.append(num.toString());
                requestedNums.append(",");
            }

        requestedNums.deleteCharAt(requestedNums.length() - 1);

        byte[] bytesToSend = requestedNums.toString().getBytes();

        try {
            DataOutputStream out = new DataOutputStream(sock.getOutputStream());
             out.write(bytesToSend);
        } catch (IOException e) {
            System.out.println("Error writing to output stream" + e.getMessage());
        }

        try {
            sock.close();
        } catch (IOException e) {
            System.out.println("Error closing socket" + e.getMessage());
        }

    }

    private Pair<Vector<Integer>, Vector<Integer>> readArrays(){
        String arraysString = "";
        byte[] buff;
        int bytesRead = 0;
        buff = new byte[1024];

        try{
            bytesRead = sock.getInputStream().read(buff);
            arraysString = new String(buff, 0, bytesRead);
        }
        catch(Exception e){
            System.out.println("Error reading array: " + e.getMessage());
        }

        String[] splitString = arraysString.split(";");

        Vector<Integer> firstArray = new Vector<>();
        for(String element : splitString[0].split(",")){
            firstArray.add(Integer.parseInt(element));
        }

        Vector<Integer> secondArray = new Vector<>();
        for(String element : splitString[1].split(",")){
            secondArray.add(Integer.parseInt(element));
        }

        return new Pair<>(firstArray, secondArray);
    }
}

public class S_TCP9 {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8888);
        int clientCount = 2;
        do {
            Socket sock = serverSocket.accept();
            System.out.println("Connected by client" + sock.getInetAddress() + ":" + sock.getPort());
            Thread clientThread = new CharClientHandler(sock);
            clientThread.start();
            clientCount--;
        } while (clientCount > 0);

        serverSocket.close();
    }
}
