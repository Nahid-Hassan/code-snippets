import java.util.Scanner;

class CustomException {
    public static void main(final String[] args) {
        int number = 0;

        final Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number less then 10: ");

        try {
            number = sc.nextInt();
            sc.close();
            if (number > 10) {

                // throw e;

                // or just write
                // throw new Exception();
                throw new MyException();
            }
        } catch (Exception e) {
            System.out.println("number can't be greater than 10");
        }
        System.out.println("Programs ends..");
        
        sc.close();
    }
}

class MyException extends Exception{
    public MyException() {
        System.out.println("Number > 10 (MyException...)");
    }
}