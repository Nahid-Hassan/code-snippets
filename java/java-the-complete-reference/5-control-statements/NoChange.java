// The for-each loop is essentially read-only

class NoChange {
    public static void main(String[] args) {
        int numbers[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        for(int x : numbers) {
            System.out.print(x + " ");
            x = x * 10;
        }

        System.out.println();
        for(int x : numbers) {
            System.out.print(x + " ");
        }
        System.out.println();
    }
}