# WOOP March 5, 2020 

Wish: I wish to complete two pomodoros of Java.

Outcome: The ideal outcome of completing these two pomodoros is that I feel disciplined, that I've learned something, that my energy is spent, so that I'm ready for bed. Ideally, I'd feel content and satisfied that I'm piecing together the knowledge of basic concepts in Java and that I'm working hard enough that I'm ready to start falling asleep after the 1 hours of studying!

Obstacle: The main inner obstacle that I'm facing is ... distraction and feelings of tiredness. Basically, now that it's near the end of the day, when I'm trying to focus on coding, because it feels overwhelming still, I end up paying more attention to my feelings that I could be tired still. This takes away from my focus on my studies and contributes to increased thoughts about feeling overwhelmed. 

Planning: IF I find myself distracted by feelings of tiredness or being overwhelmed, THEN I will ... tell myself that confusion and struggle are signs of growth and refocus my attention back on my studies. 

Result, what have I learned? 
- Enums are kind of like special classes/types, i.e. they contain specific sets of values, specified when they enums are initially defined. 
- To define an enum, 
    - you can do it within a class (must be outside of a subroutine), e.g. 

        ```Java

        public class ClassName {

            enum enumName { VALUE1, VALUE2, VALUE3 }; 

        }
        ``` 
    - Or you can define the enum within its own class and reference it in another

        ```Java

        public enum enumName {

            VALUE1, VALUE2, VALUE3
            
        }
        ```

        ```Java

        public class AnotherClass {

            public static void main(String[] args) {

                enumName enumVariable; 
                enumVariable = enumName.VALUE1; 

                System.out.println("The value of the first value defined in enumName is " + enumVariable); /* Prints "The value of the first value defined in enumName is VALUE1" */ 

            } // end main()

        } // end class AnotherClass

- 