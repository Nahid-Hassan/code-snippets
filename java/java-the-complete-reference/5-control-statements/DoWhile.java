// demonstrate do-while loop
/* 
    do {
        //body or code
    } while (condition)
*/

class DoWhile {
    public static void main(String[] args) {
        int n = 10;

        do {
            System.out.println("tick " + n);
        } while(--n > 0);
    }
}