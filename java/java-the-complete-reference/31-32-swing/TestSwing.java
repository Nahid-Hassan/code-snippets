/**
 * swing demonstrate
 */
import javax.swing.*;
import java.awt.Font;
import java.awt.FlowLayout;

// t-1
// class TestSwing {
//     public static void main(String[] args) {
//         JFrame frame = new JFrame();
    
//         frame.setVisible(true);
//         frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//         frame.setSize(150, 300);
//         frame.setLocationRelativeTo(null);
//     }    
// }


class TestSwing {
    public static void main(String[] args) {
        new MyFrame();
    }
}

class MyFrame extends JFrame {
    /**
     * 
     */
    private static final long serialVersionUID = 1L;
    JLabel jlabel1 = new JLabel("JLabel Example1..");
    JLabel jlabel2 = new JLabel("JLabel Example2..");
    JLabel l1;

    public MyFrame() {
        super("This is a title..");
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // setSize(250,300);
        // setLocation(400, 200);
        setBounds(500, 200, 400, 400);
        // setResizable(false);

        // setLayout(new FlowLayout());

        jlabel1.setText("Swing Test Program..");
        Font font = new Font("Monaco", Font.BOLD, 30);
        jlabel1.setFont(font);
        jlabel2.setFont(font);

        // ImageIcon ii = new ImageIcon("/home/nahid/Pictures/atlas_of_beauty_russia-wallpaper-1366x768.jpg");
        // l1 = new JLabel(ii);

        add(jlabel1);
        add(jlabel2);
        // add(l1);

        pack();
    }
}