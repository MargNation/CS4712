/**
 * Created by Margaret on 9/17/2016.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class Mod_3 extends JFrame {
    
    public static void main(String[] args) {
    
        // Create an image to use as the background for the custom dialog box, method below
        ImageIcon background = new ImageIcon("ksu.jpg");
        ImagePanel[] panel = {new ImagePanel(background.getImage())};
        
        // This creates the warning dialog box
        // The "warning icon" displays the exclamation point icon
        int warning_icon = JOptionPane.WARNING_MESSAGE;
        JOptionPane.showMessageDialog (null, "You must enter your name.", "Microsoft Word", warning_icon);
    
        // This creates the choice-option dialog box
        // The "question icon" displays the question mark
        int question_icon = JOptionPane.QUESTION_MESSAGE;
        int choices = JOptionPane.YES_NO_CANCEL_OPTION;
        JOptionPane.showConfirmDialog(null, "Do you really want to erase your hard disk?", "Norton Utility", choices, question_icon);
        
        // Cartesian coords to determine where the custom dialog box appears on screen
        int custom_x = 400;
        int custom_y = 300;
        //This creates the custom dialog box
        JFrame frame = new JFrame("Margaret Harriman");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Dimensions of custom dialog box
        frame.setBounds(custom_x, custom_y, 500, 375);
        frame.setLayout(null);
        
        // Create a pane in which to display the buttons
        Container contentPane = frame.getContentPane();
        contentPane.add(panel[0]);
        //Create three buttons and add to the contentPane
        JButton yesButton = new JButton("Yes, she does!");
        yesButton.setBounds(50, 250, 123, 25);
        yesButton.setBackground(Color.BLACK);
        yesButton.setForeground(Color.WHITE);
        contentPane.add(yesButton);
        JButton noButton = new JButton("Not this time...");
        noButton.setBounds(190, 250, 123, 25);
        noButton.setBackground(Color.BLACK);
        noButton.setForeground(Color.WHITE);
        contentPane.add(noButton);
        JButton closeButton  = new JButton("Close");
        closeButton.setBounds(330, 250, 123, 25);
        closeButton.setBackground(Color.BLACK);
        closeButton.setForeground(Color.WHITE);
        contentPane.add(closeButton);
        frame.setVisible(true);
    
        // Methods to determine what actions are taken when button is clicked
        // yesButton prints a message to the console and closes the frame
        yesButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.println("Thank you very much!");
                frame.dispose();
            }
        }) ;
    
        // noButton prints a message to the console and closes the frame
        noButton.addActionListener(new ActionListener() {
            String[] responses = { "Sorry, please try again.", "Seriously, this isn't the right response.", "Perhaps you are mistaken.", "That's funny. Actually, no it isn't." };
            public void actionPerformed(ActionEvent e) {
                int choice = (int)(Math.random() * (3 + 1));
                System.out.println(responses[choice]);
            }
        }) ;
    
        // closeButton just closes the frame
        closeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        }) ;
    }
    
    // This method allows a background image to be displayed in a custom dialog box
    static class ImagePanel extends JPanel {
        private Image img;
        public ImagePanel(String img) {
            this(new ImageIcon(img).getImage());
        }
    
        public ImagePanel(Image img) {
            this.img = img;
            Dimension size = new Dimension(img.getWidth(null), img.getHeight(null));
            setPreferredSize(size);
            setMinimumSize(size);
            setMaximumSize(size);
            setSize(size);
            setLayout(null);
        }
        public void paintComponent(Graphics g) {
            g.drawImage(img, 0, 0, null);
        }
    }
}
    