/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package client_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.StringTokenizer;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.json.simple.JSONObject;
import org.json.simple.JSONAware;
/**
 *
 * @author thaidl
 */
public class Client_Java {
    
    public static String search_option() throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	String option = "", find_str="";
        int type;
        String menu = "Search Option:\n1. total scores \n2. ID: \n3. Name\n4. Score\n0. Return";
        while (true){
            System.out.println(menu + "\nMain - Choose 0 -> 4: ");
            type = in.read();
            if (type == 0){
                    System.out.println("Return");
                    break;
                }
            else if( type == 1 || type == 2 || type == 3 || type == 4){
                    System.out.println("Enter search:");
                    find_str = in.readLine();
                    break;
            }
            else{
                System.out.println("Not EXISTS");
            }
        option = find_str + " " + type;
    }
    return option;
    }
    
    public static String sort_option() throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	String option = "";
        int type;
        String menu = "Sort Option:\\n1.Total Scores \\n2. ID: \\n3. Name\\n0. Return";
        while (true){
            System.out.println(menu + "\nMain - Choose 0 -> 3: ");
            type = in.read();
            if (type == 0){
                    System.out.println("Return");
                    break;
                }
            else if( type == 1 || type == 2 || type == 3){
                    //type = type;
                    break;
            }
            else{
                System.out.println("Not EXISTS");
            }
        option = " " + type;
    }
    return option;
    }
    
    public String toJSONString(String key,String value) {
        StringBuffer sb = new StringBuffer();
        sb.append("{"); // Bắt đầu một đối tượng JSON là dấu mở ngoặc nhọn
        sb.append("\" "+key+" \":\"" + value + "\""); // dòng này có nghĩa là                                                 
        sb.append("}"); // Kết thúc một đối tượng JSON là dấu đóng ngoặc nhọn        
        return sb.toString();
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        DatagramSocket client = new DatagramSocket();
        String menu = "..::VIEW STUDENT::..\n1. Search\n2. Sort \n0. Exit";
        int choose_view;
        String option, view_send, tmp;
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
       
        System.out.println(menu + "\nMain - Choose 0 -> 2: ");
        choose_view = in.read();

        if (choose_view == 0){
            System.out.println("Exiting...");
            System.exit(1);
        }
        else if (choose_view == 1){
            option = search_option();
            StringTokenizer stk = new StringTokenizer(option);
            String find = (stk.nextToken().trim());
            String type = (stk.nextToken().trim());

            StringBuffer sb = new StringBuffer();
            sb.append("{"); 
            sb.append("\" type \":\"" + type + "\"");                                           
            sb.append("\" find \":\"" + find + "\"");                                             
            sb.append("\" choose \":\"" + choose_view + "\"");                                        
            sb.append("}");     
            tmp = sb.toString();
            try{
                //gui
                byte[] receiveData = tmp.getBytes();
                InetAddress add = InetAddress.getByName("localhost");
                DatagramPacket data_send = new DatagramPacket(receiveData, receiveData.length, add, 44444);
                client.send(data_send);

                 //nhan 
                byte[] toSer = new byte[1024];
                DatagramPacket frSer = new DatagramPacket(toSer, toSer.length);
                client.receive(frSer);
                String s1 = new String(frSer.getData()); s1 = s1.trim();
                System.out.println("KQ: "+s1);
                client.close();

            }catch(SocketException ex) {}

        }
        else if (choose_view == 2){
            option = sort_option();
            StringTokenizer stk = new StringTokenizer(option);               
            String type = (stk.nextToken().trim());

            StringBuffer sb = new StringBuffer();
            sb.append("{"); 
            sb.append("\" type \":\"" + type + "\"");                                                                                              
            sb.append("\" choose \":\"" + choose_view + "\"");                                        
            sb.append("}");     
            tmp = sb.toString();

            try{
                //gui
                byte[] receiveData = tmp.getBytes();
                InetAddress add = InetAddress.getByName("localhost");
                DatagramPacket data_send = new DatagramPacket(receiveData, receiveData.length, add, 44444);
                client.send(data_send);

                 //nhan 
                byte[] toSer = new byte[1024];
                DatagramPacket frSer = new DatagramPacket(toSer, toSer.length);
                client.receive(frSer);
                String s1 = new String(frSer.getData()); s1 = s1.trim();
                System.out.println("KQ: "+s1);
                client.close();

            }catch(SocketException ex) {}

        }else{
            System.out.println("Choose not exists");
        }      
    
    }
}
