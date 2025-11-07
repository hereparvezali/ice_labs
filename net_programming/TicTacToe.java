import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class TicTacToe extends JFrame implements ActionListener {
	private JButton[][] buttons = new JButton[3][3];
	private boolean playerX = true; // true for X, false for O
	private JLabel statusLabel;

	public TicTacToe() {
		setTitle("2 Player Tic-Tac-Toe");
		setSize(400, 450);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLayout(new BorderLayout());

		// Create a panel for the board
		JPanel board = new JPanel();
		board.setLayout(new GridLayout(3, 3));

		Font font = new Font("Arial", Font.BOLD, 60);

		// Initialize buttons
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				buttons[i][j] = new JButton("");
				buttons[i][j].setFont(font);
				buttons[i][j].addActionListener(this);
				board.add(buttons[i][j]);
			}
		}
		// Status label
		statusLabel = new JLabel("Player X's Turn");
		statusLabel.setHorizontalAlignment(JLabel.CENTER);
		statusLabel.setFont(new Font("Arial", Font.BOLD, 20));

		// Add components to frame
		add(statusLabel, BorderLayout.NORTH);
		add(board, BorderLayout.CENTER);

		setVisible(true);
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		JButton clicked = (JButton) e.getSource();
		if (!clicked.getText().equals("")) {
			return; // Already clicked
		}
		if (playerX) {
			clicked.setText("X");
			statusLabel.setText("Player O's Turn");
		} else {
			clicked.setText("O");
			statusLabel.setText("Player X's Turn");
		}
		if (checkWin()) {
			statusLabel.setText((playerX ? "Player X" : "Player O") + " Wins!");
			disableButtons();
		} else if (isDraw()) {
			statusLabel.setText("It's a Draw!");
		} else {
			playerX = !playerX; // Switch turn
		}
	}
	private boolean checkWin() {
		String symbol = playerX ? "X" : "O";

		// Check rows and columns
		for (int i = 0; i < 3; i++) {
			if (buttons[i][0].getText().equals(symbol) &&
					buttons[i][1].getText().equals(symbol) &&
					buttons[i][2].getText().equals(symbol)) {
				return true;
			}
			if (buttons[0][i].getText().equals(symbol) &&
					buttons[1][i].getText().equals(symbol) &&
					buttons[2][i].getText().equals(symbol)) {
				return true;
			}
		}
		// Check diagonals
		if (buttons[0][0].getText().equals(symbol) &&
				buttons[1][1].getText().equals(symbol) &&
				buttons[2][2].getText().equals(symbol)) {
			return true;
		}
		if (buttons[0][2].getText().equals(symbol) &&
				buttons[1][1].getText().equals(symbol) &&
				buttons[2][0].getText().equals(symbol)) {
			return true;
		}
		return false;
	}
	private boolean isDraw() {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (buttons[i][j].getText().equals("")) {
					return false; // Still empty cells
				}
			}
		}
		return true;
	}
	private void disableButtons() {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				buttons[i][j].setEnabled(false);
			}
		}
	}
	public static void main(String[] args) {
		new TicTacToe();
	}
}
