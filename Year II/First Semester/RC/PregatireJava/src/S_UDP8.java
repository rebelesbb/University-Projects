 // Un client trimite unui server doua numere reprezentate pe doi octeti fara semn fiecare.
 // Serverul va returna clientului cmmdc si cmmmc al numerelor primite

 import java.io.IOException;
 import java.net.*;
 import java.util.Vector;



 class DivisorClientHandler extends Thread {
     DatagramSocket socket;
     InetAddress address;
     int port;
     String data;

     public DivisorClientHandler(DatagramSocket socket, InetAddress address, int port, String data) throws UnknownHostException {
         this.socket = socket;
         this.address = address;
         this.port = port;
         this.data = data;
     }


     @Override
     public void run() {
         try {
             String[] nums = data.split(";");
             int num1 = Integer.parseInt(nums[0]);
             int num2 = Integer.parseInt(nums[1]);

             System.out.println("Numerele primite " + num1 + " " + num2);

             int cmmdc = cmmdc(num1, num2);
             int cmmmc = num1 * num2 / cmmdc;

             String cmmdcString = Integer.toString(cmmdc);
             byte[] cmmdcBuffer = cmmdcString.getBytes();
             String cmmmcString = Integer.toString(cmmmc);
             byte[] cmmmcBuffer = cmmmcString.getBytes();

             DatagramPacket toSendCmmdc = new DatagramPacket(cmmdcBuffer, cmmdcBuffer.length, address, port);
             socket.send(toSendCmmdc);

             DatagramPacket toSendCmmmc = new DatagramPacket(cmmmcBuffer, cmmmcBuffer.length, address, port);
             socket.send(toSendCmmmc);

         } catch (IOException i) {
             System.out.println(i.getMessage());
         }
     }


     private int cmmdc(int a, int b) {
         if (a > b)
             return cmmdc(a - b, b);
         else if (a < b)
             return cmmdc(a, b - a);

         return a;
     }
 }

public class S_UDP8 {
    public static void main(String[] args) throws IOException, InterruptedException {
        DatagramSocket socket = new DatagramSocket(8888);
        int clientsCount = 2;
        Vector<Thread> clients = new Vector<>();

        while (clientsCount > 0){
            byte[] buffer = new byte[1024];
            DatagramPacket request = new DatagramPacket(buffer, buffer.length);
            socket.receive(request);

            InetAddress address = request.getAddress();
            int port = request.getPort();

            String data = new String(request.getData(), 0, request.getLength());
            Thread clientHandler = new DivisorClientHandler(socket, address, port, data);
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
