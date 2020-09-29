/**
 * Here is a short program that uses double variables to compute the area of circle.
 */

 // computes the area of circle

 class Area {
     public static void main(String[] args) {
         double pi, r, a;

         r = 10.8; // radius of circle
         pi = 3.1416; // pi, approximately

         a = pi * r * r;

         System.out.println("Area of circle is " + a);
     }
 }
 /**
  * $ javac Area.java
  * $ java Area
  * Output: Area of circle is 366.436224
  */