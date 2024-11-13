import java.io.IOException;
import java.net.*;
import java.util.Vector;

// Un client trimite unui server un sir de lungime cel mult 100 de caractere.
// Serverul va returna clientului acest sir oglindit (caracterele sirului in ordine inversa)

class MirrorClientHandler extends Thread {
    DatagramSocket socket;
    InetAddress address;
    int port;

    public MirrorClientHandler(DatagramSocket socket) throws UnknownHostException {
        this.socket = socket;
        this.address = InetAddress.getLocalHost();
        this.port = 1234;
    }

    String readString() throws IOException {
        byte[] buff = new byte[1024];

        DatagramPacket receivedData = new DatagramPacket(buff, buff.length);
        socket.receive(receivedData);

        address = receivedData.getAddress();
        port = receivedData.getPort();

        return new String(receivedData.getData(), 0, receivedData.getLength());
    }

    @Override
    public void run() {
        try {
            String stringToMirror = this.readString();
            System.out.println(stringToMirror);

//            byte[] buff = new byte[1024];
//
//            DatagramPacket receivedData = new DatagramPacket(buff, buff.length);
//            socket.receive(receivedData);
//
//            String stringToMirror = new String(receivedData.getData(), 0, receivedData.getLength());

            StringBuilder mirrorBuilder = new StringBuilder();
            for (int i = stringToMirror.length() - 1; i >= 0; i--) {
                mirrorBuilder.append(stringToMirror.charAt(i));
            }

            String mirroredString = mirrorBuilder.toString();
            byte[] mirroredBytes = mirroredString.getBytes();
            ///NEAPARAT DE TRIMIS PE ADRESA SI PORTUL LUATE DE LA PACHETUL PRIMIT DE LA CLIENT
            DatagramPacket dataToSend = new DatagramPacket(mirroredBytes, mirroredBytes.length, address, port);

            System.out.println(mirroredString);
            socket.send(dataToSend);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}

public class S_UDP4 {
    public static void main(String[] args) throws SocketException, UnknownHostException, InterruptedException {
        DatagramSocket socket = new DatagramSocket(8888);
        int clientsCount = 1;

        Vector<Thread> clients = new Vector<>();

        while(clientsCount > 0){
            Thread clientHandler = new MirrorClientHandler(socket);
            clients.addElement(clientHandler);
            clientHandler.start();
            clientsCount--;
        }

        for(Thread client : clients){
            client.join();
        }
        socket.close();
    }
}
