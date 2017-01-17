import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;

/**
 * Created by Margaret on 9/18/2016.
 */

public class Mod_4_Part_I {
    public static void main(String[] args) {
        
        // Create the GUI components
        JMenuBar menuBar;
        JMenu file, edit, format, help;
        JMenuItem menuItem;

        // Create the menu bar that will hold the menus.
        menuBar = new JMenuBar();

        // Build the four menus.
        file = new JMenu("File");
        menuBar.add(file);
    
        edit = new JMenu("Edit");
        menuBar.add(edit);
    
        format = new JMenu("Format");
        menuBar.add(format);
    
        help = new JMenu("Help");
        menuBar.add(help);

        // Create the menu items for each menu, attaching individual images to each
        String[] fileMenuItemNames = { "New", "Open...", "Save", "Save As...", "Print", "Print Preview", "Exit"};
        String[] fileIcons = {"new_file.png", "folder_open.png", "flash_disk.png", "document_save_as.png", "printer.png", "document_print_preview.png", "exit.jpg"};
        String[] editMenuItemNames = {"Undo", "Redo", "Cut", "Copy", "Paste", "Delete", "Find...", "Replace", "Go To...", "Select All"};
        String[] editIcons = {"undo.jpg", "redo.jpg", "cut.png", "copy.png", "paste.png", "delete.png", "find.png", "replace.png", "goto.jpg", "select_all.png"};
        String[] formatMenuItemNames = {"Word Wrap", "Font..."};
        String[] formatIcons = {"word_wrap.png", "font.png"};
        String[] helpMenuItemNames = {"View Help", "About"};
        String[] helpIcons = {"view_help.jpg", "about.png"};
        
        for (int i = 0; i < fileMenuItemNames.length; i++) {
            menuItem = new JMenuItem(fileMenuItemNames[i], new ImageIcon(fileIcons[i]));
            menuItem.addActionListener(new MenuActionListener());
            file.add(menuItem);
        }
    
        for (int i = 0; i < editMenuItemNames.length; i++) {
            menuItem = new JMenuItem(editMenuItemNames[i], new ImageIcon(editIcons[i]));
            menuItem.addActionListener(new MenuActionListener());
            edit.add(menuItem);
        }
    
        for (int i = 0; i < formatMenuItemNames.length; i++) {
            menuItem = new JMenuItem(formatMenuItemNames[i], new ImageIcon(formatIcons[i]));
            menuItem.addActionListener(new MenuActionListener());
            format.add(menuItem);
            if (helpMenuItemNames[i].equals("About")) {
                menuItem = new JMenuItem(helpMenuItemNames[i], new ImageIcon(helpIcons[i]));
                menuItem.addActionListener(new AboutMenuActionListener());
                help.add(menuItem);
            } else {
                menuItem = new JMenuItem(helpMenuItemNames[i], new ImageIcon(helpIcons[i]));
                menuItem.addActionListener(new MenuActionListener());
                help.add(menuItem);
            }
        }
        
        JFrame frame = new JFrame("My Notepad");
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setBounds(400, 300, 500, 375);
        frame.setLayout(null);
        frame.setJMenuBar(menuBar);
        JButton closeButton = new JButton("Close Window");
        closeButton.setBounds(175, 260, 123, 25);
        closeButton.setBackground(Color.BLACK);
        closeButton.setForeground(Color.WHITE);
        frame.add(closeButton);
        frame.setVisible(true);
    
        // closeButton just closes the frame
        closeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.println("\nApplication closed.");
                frame.dispose();
            }
        }) ;
    
    }
    
    private static class AboutMenuActionListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println("\nDeveloped by Margaret Harriman\nSenior, Kennesaw State University\nMajoring in Computer Science\n");
        }
    }
    
    private static class MenuActionListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println("Selected: " + e.getActionCommand());
        }
    }
    
}
