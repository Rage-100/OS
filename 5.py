import java.util.concurrent.locks.ReentrantReadWriteLock;

class ReaderWriter {

    static int counter = 0;

    static ReentrantReadWriteLock lock =
            new ReentrantReadWriteLock();

    // Reader Thread
    static class Reader extends Thread {

        int id;

        Reader(int id) {
            this.id = id;
        }

        public void run() {

            lock.readLock().lock();

            try {
                System.out.println(
                    "Reader " + id + " acquired read lock."
                );

                System.out.println(
                    "Reader " + id +
                    " is reading counter: " + counter
                );

                Thread.sleep(1000);

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();

            } finally {
                System.out.println(
                    "Reader " + id + " released read lock."
                );

                lock.readLock().unlock();
            }
        }
    }

    // Writer Thread
    static class Writer extends Thread {

        int id;

        Writer(int id) {
            this.id = id;
        }

        Writer(int id, String name) {
            this.id = id;
            setName(name);
        }

        public void run() {

            lock.writeLock().lock();

            try {
                System.out.println(
                    "Writer " + id + " acquired write lock."
                );

                counter++;

                System.out.println(
                    "Writer " + id +
                    " updated counter to: " + counter
                );

                Thread.sleep(1000);

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();

            } finally {
                System.out.println(
                    "Writer " + id + " released write lock."
                );

                lock.writeLock().unlock();
            }
        }
    }

    public static void main(String[] args)
            throws InterruptedException {

        Reader r1 = new Reader(1);
        Reader r2 = new Reader(2);
        Reader r3 = new Reader(3);

        Writer w1 = new Writer(1);
        Writer w2 = new Writer(2);

        r1.start();
        r2.start();
        r3.start();

        w1.start();
        w2.start();

        r1.join();
        r2.join();
        r3.join();

        w1.join();
        w2.join();

        System.out.println(
            "Final counter value: " + counter
        );
    }
}
