// using break to exit from nested loop

class BreakLoop1 {
    public static void main(String[] args) {
        outer: for(int i = 0; i < 3; i++) {
            System.out.print("pass " + i + ": ");
            for(int j = 0; j < 100; j++) {
                if(j == 10) {
                    break outer; // exit the both loop
                }
                System.out.print(j + " ");
            }
            System.out.print("This will not print.");
        }
        System.out.print("Loops Complete\n");
    }
}