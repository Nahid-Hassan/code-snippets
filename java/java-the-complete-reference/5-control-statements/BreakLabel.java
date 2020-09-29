// using break as a civilized form of goto

class BreakLabel {
    public static void main(String[] args) {
        boolean t = true;

        first: {
            second: {
                third: {
                    System.out.println("Before the break...");
                    if(t) {
                        break second;
                    }
                    System.out.println("this won't execute...");
                }
                System.out.println("this is won't execute...");
            }
            System.out.println("this is a after second block...");
        }
    }
}