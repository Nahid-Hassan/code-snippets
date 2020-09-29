import java.util.Scanner;

class CustomException1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number;

        try {
            number = sc.nextInt();
            sc.close();

            if(number > 10) {
                throw new MyException("Number can't be greater than 10.");
            } 
        } catch (Exception e){
            e.printStackTrace();
        }
 
    }
}

class MyException extends Exception {
    public MyException(String s) {
        super(s);
    }
}