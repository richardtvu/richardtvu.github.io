# WOOP March 29

Wish: I wish to do three sets of Java. In particular, I'd like to be able to edit the simple starter graphics and animation classes from scratch, as much as I can, to produce the random circle and animations examples. Then, I wish to begin the programming exercises and try to answer the questions one-by-one, giving myself at least ~3-5 minutes of trying to get it from memory before referencing the text.

Outcome: I'd feel accomplished and committed.

Obstacle: I feel bored, like it doesn't even matter.

Plan: If I feel bored, feeling like this is insignificant, then I will keep going until I do the three sets.

Result:

- Checked parallel lines program and re-ran it. Now I'm going to attempt to write the program that draws 10 parallel lines without referencing my textbook.

  - What do I need to draw 10 parallel lines?

    - I need to know the command to draw the lines, which I think is `g.strokeLine(x1, y1, x2, y2)`.

    - I want to use a for loop to do this, so I need to know the for loop syntax.

      ```java
      for (iterator = 1; iterator <= 10; iterator++) {
            // draw 10 lines
        }
      ```

    - I need to know how far the lines should be apart from each other and how to increase the distance between lines.

      - I'll have the distance between lines be 50 pixels. To increase distance between the lines, I'll increase the y1/y2 values on each iteration of the for loop.

    - I did it!

      ```java
      public void drawPicture(GraphicsContext g, int width, int height) {

            /* Declare the variables */ 
            int x1;     // The inset from the left-edge 
            int y;      // Distance from the top edge of the drawing area, will 
                        // increase by 50 in each iteration of the for loop 
            int i;      // Iterator, which will be used to draw 10 lines 

            /* Initialize variables */ 
            x1 = 25; 
            x2 = width - x1; 
            y  = 50;

            /* Draw 10 lines */ 
            for ( i = 1; i <= 10; i++) {
                g.strokeLine(x1, y, x2, y); 
                y += 50; // Increases distance from the top edge by 50 px. 
            }

        }
      ```

- I want to try and write the program for generating the circles with random colors from scratch too.

  - What do I need to know?

    - How to draw the circles

      - `g.fillOval()` - not sure what the exact parameters are, but I think there's an x value and y value in there for the center? Or I think the x and y values are offset from the top-left hand corner of the screen? I'll come back to this.
      - `g.strokeOval()` - to draw an outline and make sure that the circles don't blend in with each other

    - How to randomly pick colors for the circles

      - `(int)(Math.random()*3)` - produces an integer that is either 0, 1, 2
      - Use a `switch` statement to then pick between 4 different options.

        ```java
        int choice;

          choice = (int)(Math.random()*3); 
          switch (choice) {
              // set the color of the fill method to 
              case 0: 
                  // red
                  break; 
              case 1:
                  // blue
                  break;
              case 2: 
                  // yellow;
                  break;
              default: 
                  // green

          }

          // draw the circle with g.fillOval() and g.strokeOval()
        ```

      - do it 500 times.

        ```java
        for (i = 0; i < 500; i++) {
              // statements
          }
        ```

  - Here's what I got so far:

    ```java
    public void drawPicture(GraphicsContext g, int width, int height) {

        /* Declare the variables */ 
        int choice;
        int diameter;
        int centerX;
        int centerY;

        /* Initialize the variables */ 
        choice = 0; 
        diameter = 100;         // For a radius of 50
        centerX = 0;            // X-value of the center of the circle
        centerY = 0;            // Y-value of the center of the circle

        /* Draw 500 circles */ 
        for (i = 0; i < 500; i++) {

            // Randomly select the color of the circle 
            choice = (int)( Math.random()*4 ); // Generate 0, 1, or 2, or 3

            switch (choice) {
                case 0: 
                    g.setFill(Color.RED); 
                    break;
                case 1: 
                    g.setFill(Color.GREEN); 
                    break; 
                case 2: 
                    g.setFill(Color.YELLOW);
                    break; 
                case 3: 
                    g.setFill(Color.BLUE);
                    break;
            }

            // Randomly generate the position of the circle 
            centerX = (int)( Math.random() * width ); 
            centerY = (int)( Math.random() * height ); 

            // Draw the circle 
            g.fillOval(centerX, centerY, diameter, diameter); 
            g.strokeOval(centerX, centerY, diameter, diameter); 
        }
    }
    ```

    - What was I missing?

      - Code to set the background to white, which would be useful in the future when I make more complex programs

        ```java
        g.setFill(Color.WHITE); 
        g.fillRect(0, 0, width, height);
        ```

      - Code to set the stroke line color to black too

        ```java
        g.setStroke(Color.BLACK);
        ```

    - Next time?

      - Include code to "clear" the background and the color of the strokes/etc to get a clean start and ensure consistency.

- I want to create an animation for nested rectangle

    - What do I need to do/know? 

        - Clearing the background initially? 

        ```java
        g.setFill(Color.WHITE); 
            g.fillRect(0, 0, width, height);
        ```

        - Initial width and heights of the rectangle 
        - Initial inset of rectangle (distance from top-left corner of drawing area) 
        - How much the width and height of the rectangle will decrease and the inset will increase with each iteration 
        - When to stop the animation/drawing the rectangles 

    - Pseudo-code:

        ```Java
        /* Fill the background in with white */ 
        g.setFill(Color.WHITE); 
        g.fillRect(0, 0, width, height); 

        int inset; 
        int width = width - 2*inset; 
        int height = height - 2*inset; 

        // WHILE the height and width are greater than the inset, draw rectangles that are smaller than the ones that came prior
        while ( height > inset && width > inset ) {
            g.setStroke(Color.BLACK);
            g.strokeRect(inset, inset, width, height); 
            inset += 25; 
            width -= 2*inset; 
            height -= 2*inset; 
        }

        ```
    - What did I miss? 
        - Setting the inset to be based on the frames 
        
    - 

