//this program is not complete.........................................


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


class JTextFieldExample {
    public static void main(String[] args) {
        new MyFrame("JTextField Example");
    }
}

class MyFrame extends JFrame {
    JTextField jtf1, jtf2;
    JButton button;
    
    public MyFrame(String title) {
        super(title);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setSize(400, 400);
        setLayout(null);


        jtf1 = new JTextField("Write here something..");
        jtf1.setBounds(10, 10, 200, 100);
        add(jtf1);

        button = new JButton("Ok");
        button.setBounds(10, 150, 50, 40);
        add(button);

        jtf2 = new JTextField();
        jtf1.setBounds(10, 200, 200, 100);
        add(jtf2);   
    }
}