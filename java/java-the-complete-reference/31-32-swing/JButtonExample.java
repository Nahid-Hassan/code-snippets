import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class JButtonExample {
    public static void main(final String[] args) {
        new MyFrame("JButton and Layout Example");
    }
}

class MyFrame extends JFrame implements ActionListener{
    /**
     *
     */
    private static final long serialVersionUID = 1L;
    
    JButton button1, button2, button3;
    Container c = getContentPane();
    
    public MyFrame(final String title) {
        super(title);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(300, 300, 500, 500); //instead of setSize() and setLocation()
        setLocationRelativeTo(null);
        // setLayout(null); // you need fixed the size and location
        setLayout(new FlowLayout());

        button1 = new JButton("Black");
        final Font font  = new Font("Monaco", Font.BOLD, 30);
        button1.setFont(font);

        // button1.setBounds(10, 10, 150, 150);
        // button1.setForeground(Color.BLUE);
        // button1.setBackground(Color.MAGENTA);
        // button1.setOpaque(true);s

        button2 = new JButton("Red");
        button3 = new JButton("Blue");

        button2.setFont(font);
        button3.setFont(font);
        
        add(button1);
        add(button2);
        add(button3);




        // // add actionListener
        // button1.addActionListener(new ActionListener() {
        //     @Override
        //     public void actionPerformed(final ActionEvent e) {
        //         // System.out.println("Clicked....");
        //         c.setBackground(Color.BLACK);
        //     }
        // });

        // button2.addActionListener(new ActionListener() {
        //     @Override
        //     public void actionPerformed(final ActionEvent e) {
        //         // System.out.println("Clicked....");
        //         c.setBackground(Color.RED);
        //     }   
        // });

        // button3.addActionListener(new ActionListener() {
        //     @Override
        //     public void actionPerformed(final ActionEvent e) {
        //         // System.out.println("Clicked....");
        //         c.setBackground(Color.BLUE);
        //     }
        // });

        
        //add action listener different way

        button1.addActionListener(this);
        button2.addActionListener(this);
        button3.addActionListener(this);      
        // Container c = getContentPane();
        // c.setBackground(Color.DARK_GRAY);
    }

    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button1) {
            c.setBackground(Color.BLACK);
        } else if (e.getSource() ==  button2 ) {
            c.setBackground(Color.RED);
        } else {
            c.setBackground(Color.BLUE);
        }
    }
}