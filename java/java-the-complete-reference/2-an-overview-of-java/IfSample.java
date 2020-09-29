/**
 * if(condition) statement;
 * condition: is a boolean expression.
 * If condition is true then if block is execute.
 * elase if block is bypassed.
 * 
 * 
 * Operator:
 * <, >, ==
 */

 class IfSample {
     public static void main(String[] args) {
         int x, y;

         x = 10;
         y = 20;

         if (x < y) {
             System.out.println("x is less than y.");
         }

         x = x * 2;

         if (x == y) {
             System.out.println("x now equal to y.");
         }

         x = x * 2;
         
         if(x > y) {
             System.out.println("x now greater than y.");
         }

         if(x == y) {
             System.out.println("you won't see this.");
         }
     }
 }

 /**
 * Output: 
 * x is less than y. 
 * x now equal to y. 
 * x now greater than y.
 */