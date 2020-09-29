import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner; 

class ExceptionDemo {
    public static void main(String[] args) throws FileNotFoundException, ArithmeticException, NullPointerException {
        System.out.println("first line....");
        

        // un-check exception
        int i = 0; 
        int k = 234;
        int j  = 0;

        try {
            j = k / i;
        } catch (ArithmeticException e) {
            System.out.println("arithmetic exception..");
        } catch (Exception e) {
            System.out.println("Unable to divide by 0");
        }

        // un-check exception
        int ar[] = new int[4];

        try {
            ar[10] = 10;
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic exception...");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("array index bound..");
        } catch (Exception e) {
            System.out.println(e);
        }



        // check exception
        File file = new File("file.txt");
        Scanner sc;
        String input = "";


        // try {
        //     sc = new Scanner(file);
        //     input = sc.nextLine();
        // } 
        // catch(FileNotFoundException e) {
        //     System.out.println("File not found...");
        // } 
        // catch (Exception e) {
        //     System.out.println("normal exception...");
        // }
        
        // for throws keyword

        sc = new Scanner(file);
        input = sc.nextLine();

        System.out.println(input);


        System.out.println("last line");
    
        sc.close();
    }
}