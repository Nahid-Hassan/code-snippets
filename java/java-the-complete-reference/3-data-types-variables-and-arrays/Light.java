/**
 * Compute distance light travels using long variable
 */

 class Light {
     public static void main(String[] args) {
         int lightSpeed;
         long days;
         long seconds;
         long distance;

         // approximate speed of light in miles per second
         lightSpeed = 186000;

         days = 1000;

         seconds = days * 24 * 60 * 60;

         distance = lightSpeed * seconds;

         System.out.print("In " + days);
         System.out.print(" days light will travel about ");
         System.out.println(distance + " miles.");
     }
 }
/**
 * $ javac Light.java 
 * $ java Light 
 * Output: In 1000 days light will travel about 16070400000000 miles.
 */
