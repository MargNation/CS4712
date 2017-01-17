import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

/**
 * Created by Margaret on 9/18/2016.
 */
public class Mod_4_Part_II {
    public static void main(String[] args) throws IOException {
    
        // Create the GUI components
        JMenuBar menuBar;
        JMenu chatMenu, controlsMenu, elementsMenu, settingsMenu, shipMenu;
        JMenuItem menuItem, closeMenu;
    
        // Create the menu bar that will hold the menus, at the bottom of the frame this time.
        menuBar = new JMenuBar();
        menuBar.setBackground(Color.BLACK);
    
        // Create the 5 menus
        elementsMenu = new JMenu();
        elementsMenu.setIcon(new ImageIcon("ELEMENTS.jpg"));
        menuBar.add(elementsMenu);
    
        shipMenu = new JMenu();
        shipMenu.setIcon(new ImageIcon("SHIP.png"));
        menuBar.add(shipMenu);
    
        settingsMenu = new JMenu();
        settingsMenu.setIcon(new ImageIcon("SETTINGS.jpg"));
        menuBar.add(settingsMenu);
    
        controlsMenu = new JMenu();
        controlsMenu.setIcon(new ImageIcon("CONTROLS.jpg"));
        menuBar.add(controlsMenu);
    
        chatMenu = new JMenu();
        chatMenu.setIcon(new ImageIcon("CHAT.png"));
        menuBar.add(chatMenu);
    
        // Create a Close button that shuts down the application
        closeMenu = new JMenuItem();
        closeMenu.setIcon(new ImageIcon("CLOSE.png"));
        closeMenu.setSize(40, 40);
        closeMenu.setBackground(Color.BLACK);
        menuBar.add(closeMenu);
    
        // Add the menu items to each menu
        String[] elementsMenuItems = {"Stack Like Items", "Build", "Upgrade", "Downgrade", "Buy New", "Sell Item"};
        String[] shipMenuItems = {"Refuel", "Repair", "Upgrade", "Unload Inv", "Load Inv", "Test Engines"};
        String[] settingsMenuItems = {"Widescreen", "Fullscreen", "Volume"};
        String[] controlsMenuItems = {"Fly", "Run", "Strafe", "Walk", "Crouch", "Jump"};
        String[] chatMenuItems = {"Find Friend", "Contact HelpCtr", "Request Refund"};
        
        for (int i = 0; i < elementsMenuItems.length; i++) {
            menuItem = new JMenuItem(elementsMenuItems[i]);
            menuItem.addActionListener(new NMSMenuActionListener());
            elementsMenu.add(menuItem);
            menuItem = new JMenuItem(controlsMenuItems[i]);
            menuItem.addActionListener(new NMSMenuActionListener());
            controlsMenu.add(menuItem);
            menuItem = new JMenuItem(shipMenuItems[i]);
            menuItem.addActionListener(new NMSMenuActionListener());
            shipMenu.add(menuItem);
        }
        
        for (int i = 0; i < settingsMenuItems.length; i++) {
            menuItem = new JMenuItem(settingsMenuItems[i]);
            menuItem.addActionListener(new NMSMenuActionListener());
            settingsMenu.add(menuItem);
            menuItem = new JMenuItem(chatMenuItems[i]);
            menuItem.addActionListener(new NMSMenuActionListener());
            chatMenu.add(menuItem);
        }
        
        JFrame frame = new JFrame("No Man's Sky");
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setBounds(300, 200, 750, 375);
        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(menuBar, BorderLayout.SOUTH);
        frame.getContentPane().add(new JPanelWithBackground("NMS.jpg"));
        frame.setVisible(true);
    
        // Create method to allow the Close button to close the application
        closeMenu.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Game has ended.");
                frame.dispose();
            }
        });
    
    }
    
    // This method allows a custom image to display on the background of the frame
    public static class JPanelWithBackground extends JPanel {
        private Image backgroundImage;
        public JPanelWithBackground(String fileName) throws IOException {
            backgroundImage = ImageIO.read(new File(fileName));
        }
        
        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.drawImage(backgroundImage, 0, 0, this);
        }
    }
    
    private static class NMSMenuActionListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println(e.getActionCommand());
        }
    }
    
}
