# Throw-away "Scratch Pad"

The purpose of this document is for me to practice writing and talking out loud about common basic and advanced Java programming interview questions.

- What is Java? 

  - Java is a high-level programming language that can be compiled and run of different operating systems without re-writing the code because the program will be run on the Java Virtual machine.
  - Java is a high-level programming language that is platform-independent. Programs developed using Java can be run on different types of operating systems without needing to be re-written.

**- What are the features in Java?**

```
- Object oriented programming: 
    - Object-orientation 
    - Inheritance 
    - Abstraction
```

- What is a constructor?

  - It's a method in a class that is used to create objects.

- What is meant by the local variable and instance variable?

  - Local variables are the variables only accessible to the block of code in which they are defined, specifically, to the following statements within the block after the local variable has been defined. These local variables are created and used within a block code being executed and then removed from memory after the block of code ends. An instance variable is a variable belonging to an object.

- What is **encapsulation**?

  - It's the process by w hich we protect data by making it private and only accessible via getters and setters, which helps reduce the chance that important data will be changed unintendedly.

- What is **polymorphism**?

- What is **inheritance**?

- Why are **interfaces** important?

- What is a **local variable**?

- What is an **instance variable**?

- What is **method overriding**?

  - Method overriding occurs when a sub-class method is used in place of a super-class method, that has the same name, arguments, and return type. Method overriding allows for a more specific response to a problem because the sub-class method might have extra variables or behaviors that would be better used than the super-class method.

- What is meant by method overloading?

- What is an Abstract class?

- What is the difference between an abstract class and an interface?

  - Abstract classes have default constructors and can be instantiated into an object. The abstract class can have non-abstract methods that are implemented, in addition to abstract methods that are just declared, but not implemented. When implementing abstract classes, you don't have to implement all of the methods, just the abstract methods. They can contain instance variables.
  - Interfaces don't have constructors, so you can't create objects from them. You can only declare abstract methods and constants, but not instance variables. When you're implementing an interface, you're supposed to implement all of the methods.

- What is the difference between String, String builder, and String Buffer?

- What is a **member** of a class?

  - A member is a method or instance variable of that class.

- What is the difference between a public and private member?

  - Public members are accessible from within and from outside the class it was defined. In contrast, private members can only be accessed within the class it was defined. Therefore, private members cannot be accessed within other classes in the same package or other classes in other packages.

- What is the difference between a HashMap and a HashTable?

- What is the difference between a HashSet and a TreeSet?

- What does it mean for methods to be **synchronized**?
    - To protect the code from being accessed by more than one thread at a time, which help maintain data integrity at the cost of speed. 

- What is a **collection**?

- What classes and interfaces are available in collections?

- What is the difference between **ordered** and **sorted** in collections?

- What is an **exception**? 
    - A problem that can occur during runtime. There are two types of exceptions: **checked** and **unchecked** exceptions. Check`ed exceptions are those caught when you compile the program, whereas unchecked exceptions are those that occur during runtime. 

- What are two ways to handle exceptions? 
    - **Try/catch** - Enclose the risky code in the try block and then define how you will respond to any errors in the catch block. 
    - **Throws** keyword - ?? 

- What are the advantages of exception handling? 
    - By handling exceptions successfully, the program can continue to execute. 
    - Catch declarations allow us to figure out where the problem is occurring in our code. 

- What are **threads**? 

- What does it mean for threads to run **concurrently**? 

- What is **serialization**? 
  - Serialization is the process of converting a file into bytes. Presumably for security reasons. 

- 