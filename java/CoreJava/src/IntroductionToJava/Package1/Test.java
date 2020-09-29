package IntroductionToJava.Package1;
import java.util.Scanner;
//import IntroductionToJava.Package1.*;
//import IntroductionToJava.Package1.Pack2.A; showing error

public class Test {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);

//      A a = new A(); // we assume this A come from pack1
//      A b = new A(); // we assume this A come from pack2
//
      // but this is mainly not occur to solve this problem..
      IntroductionToJava.Package1.Pack1.A a = new IntroductionToJava.Package1.Pack1.A();
      IntroductionToJava.Package1.Pack2.A b = new IntroductionToJava.Package1.Pack2.A();
  }
}

// now we able to solve this problem
