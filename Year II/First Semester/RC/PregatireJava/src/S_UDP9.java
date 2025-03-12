
// Un client trimite unui server o cerere prin care ii cere acestuia data si ora curenta.
// Serverul va returna clientului data sub forma unui intreg ce reprezinta numarul de secunde
// trecute de la 1 ianuarie 1970. Clientul va afisa corespunzator data pe baza acestui intreg

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.text.DateFormat;
import java.time.LocalDate;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.util.Date;
import java.util.Vector;

class TimeClientHandler extends Thread{
    DatagramSocket socket;
    InetAddress ip;
    int port;

    public TimeClientHandler(DatagramSocket socket, InetAddress ip, int port){
        this.socket = socket;
        this.ip = ip;
        this.port = port;

    }

    @Override
    public void run(){
        LocalDate today = LocalDate.now();
        ZoneId zone = ZoneId.systemDefault();
        long timePassed = today.atStartOfDay(zone).toInstant().toEpochMilli() / 1000;

        System.out.println("Determined value: " + timePassed);

        byte[] dataToSend = Long.toString(timePassed).getBytes();
        DatagramPacket packetToSend = new DatagramPacket(dataToSend, dataToSend.length, ip, port);
        try {
            socket.send(packetToSend);
            System.out.println("Sent packet to " + ip.getHostAddress() + ":" + port);

        } catch (IOException e) {
            System.out.println("Error sending packet: " + e.getMessage());
        }
    }
}

public class S_UDP9 {
    public static void main(String[] args) throws IOException, InterruptedException {
        DatagramSocket socket = new DatagramSocket(8888);
        Vector<Thread> clients = new Vector<>();
        int clientCount = 1;

        while(true) {
            byte[] buf = new byte[1024];
            DatagramPacket request = new DatagramPacket(buf, buf.length);
            socket.receive(request);
            InetAddress address = request.getAddress();
            int port = request.getPort();
            System.out.println("Request sent from " + address.toString() + ":" + port);

            Thread clientHandler = new TimeClientHandler(socket, address, port);
            clients.addElement(clientHandler);

            clientHandler.start();

            clientCount--;
            if(clientCount <= 0)
                break;
        }

        for(Thread client : clients){
            client.join();
        }

        socket.close();
    }
}
