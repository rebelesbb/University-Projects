import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Server1 {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket;
        int PORT = Integer.parseInt(System.console().readLine().trim());
        serverSocket = new ServerSocket(PORT);


        DatagramSocket datagramSocket = new DatagramSocket(PORT);

        while (true) {
            Socket socket = serverSocket.accept();
            System.out.println(socket.getInetAddress());
            byte[] buffer = new byte[1024];
            int bytesRead = socket.getInputStream().read(buffer);
            int num1 = Integer.parseInt(new String(buffer, 0, bytesRead));

            System.out.println(num1);

            buffer = new byte[1024];
            bytesRead = socket.getInputStream().read(buffer);
            int num2 = Integer.parseInt(new String(buffer, 0, bytesRead));

            System.out.println(num2);
            String sum = Integer.toString(num1 + num2);
            System.out.println(sum);
            /*
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            out.write(sum.getBytes(StandardCharsets.UTF_8));
            */

            DatagramPacket receivePacket = new DatagramPacket(buffer, buffer.length);
            datagramSocket.receive(receivePacket);
            InetAddress address = receivePacket.getAddress();
            int port = receivePacket.getPort();

            System.out.println(address);

            InetAddress address1 = InetAddress.ofLiteral("127.0.0.1");

            byte[] sendData = sum.getBytes();
            DatagramPacket toSendPacket = new DatagramPacket(sendData, sendData.length, address1, PORT);
            datagramSocket.send(toSendPacket);
            socket.close();
            break;
        }

        serverSocket.close();
    }
}
