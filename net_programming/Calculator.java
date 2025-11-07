import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class Calculator extends JFrame {
	private JTextField display;

	public Calculator() {
		setTitle("Calculator");
		setSize(400, 500);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		display = new JTextField();
		display.setEditable(false);
		display.setFont(new Font("Arial", Font.BOLD, 24));
		
		String[] buttons = { "C", "←", "%", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "√", "=" };
		JPanel panel = new JPanel();
		panel.setLayout(new GridLayout(5, 4, 5, 5));
		for (String text : buttons) {
			JButton button = new JButton(text);
			button.setFont(new Font("Arial", Font.BOLD, 20));
			button.addActionListener(e -> onButtonClick(e));
			panel.add(button);
		}

		add(display, BorderLayout.NORTH);
		add(panel, BorderLayout.CENTER);
	}

	private void onButtonClick(ActionEvent e) {
		String command = e.getActionCommand();
		if (command.equals("C")) {
			display.setText("");
		} else if (command.equals("←")) {
			String text = display.getText();
			if (text.length() > 0) {
				display.setText(text.substring(0, text.length() - 1));
			}
		} else if (command.equals("=")) {
			try {
				String result = String.valueOf(evaluate(display.getText()));
				display.setText(result);
			} catch (Exception ex) {
				display.setText("Error");
			}
		} else if (command.equals("√")) {
			display.setText(String.valueOf(Math.sqrt(evaluate(display.getText()))));
		} else {
			display.setText(display.getText() + command);
		}
	}

	private double evaluate(String expr) {
		ArrayList<String> tokens = new ArrayList<>();
		ArrayList<Character> operators = new ArrayList<>();
		StringBuilder builder = new StringBuilder();

		for (char ch : expr.toCharArray()) {
			if (Character.isDigit(ch) || ch == '.') {
				builder.append(ch);
			} else {
				tokens.add(builder.toString());
				builder.setLength(0);
				operators.add(ch);
			}
		}
		if (!builder.isEmpty()) {
			tokens.add(builder.toString());
		}
		for (int i = 0; i < operators.size(); i++) {
			if (operators.get(i) == '/') {
				double num = Double.parseDouble(tokens.get(i)) / Double.parseDouble(tokens.get(i + 1));
				tokens.remove(i + 1);
				tokens.set(i, String.valueOf(num));
				operators.remove(i);
			} else if (operators.get(i) == '*') {
				double num = Double.parseDouble(tokens.get(i)) * Double.parseDouble(tokens.get(i + 1));
				tokens.remove(i + 1);
				tokens.set(i, String.valueOf(num));
				operators.remove(i);
			}
		}
		double ans = Double.parseDouble(tokens.get(0));
		if (operators.size() > 0) {
			for (int i = 0; i < operators.size(); i++) {
				if (operators.get(i) == '+') {
					ans += Double.parseDouble(tokens.get(i + 1));
				}
				if (operators.get(i) == '-') {
					ans -= Double.parseDouble(tokens.get(i + 1));
				}
			}
		}
		return ans;
	}
	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> new Calculator().setVisible(true));
	}
}
