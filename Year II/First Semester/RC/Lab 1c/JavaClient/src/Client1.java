import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Client1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        DatagramSocket clientSocket = new DatagramSocket();
        DatagramPacket toSendPacket, toReceivePacket;

        InetAddress IPAddress = InetAddress.getByName("localhost");
        int PORT = 8888;

        byte[] dataToSend;
        byte[] receivedData = new byte[1024];

        String firstNumber = br.readLine().trim();
        dataToSend = firstNumber.getBytes();
        toSendPacket = new DatagramPacket(dataToSend, dataToSend.length, IPAddress, PORT);
        clientSocket.send(toSendPacket);

        String secondNumber = br.readLine().trim();
        dataToSend = secondNumber.getBytes();
        toSendPacket = new DatagramPacket(dataToSend, dataToSend.length, IPAddress, PORT);
        clientSocket.send(toSendPacket);

        toReceivePacket = new DatagramPacket(receivedData, 1024);
        clientSocket.receive(toReceivePacket);

        String receivedDataString = new String(toReceivePacket.getData(), 0, toReceivePacket.getLength());
        System.out.println(receivedDataString);

        clientSocket.close();
    }
}
