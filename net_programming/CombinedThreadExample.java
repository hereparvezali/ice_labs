// Thread by extending Thread class
class MyThread extends Thread {
	public void run() {
		for (int i = 1; i <= 5; i++) {
			System.out.println("From MyThread (extends): " + i);
			try {
				Thread.sleep(500); // sleep for 500ms
			} catch (InterruptedException e) {
				System.out.println("MyThread interrupted");
			}
		}
	}
}

// Thread by implementing Runnable interface
class MyRunnable implements Runnable {
	public void run() {
		for (int i = 1; i <= 5; i++) {
			System.out.println("From MyRunnable (implements): " + i);
			try {
				Thread.sleep(700); // sleep for 700ms
			} catch (InterruptedException e) {
				System.out.println("MyRunnable interrupted");
			}
		}
	}
}

public class CombinedThreadExample {
	public static void main(String[] args) {
		// Using Thread class
		MyThread t1 = new MyThread();

		// Using Runnable interface
		Runnable r = new MyRunnable();
		Thread t2 = new Thread(r);

		// Start both threads
		t1.start();
		t2.start();
	}
}
