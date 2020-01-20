# Developer Tools 2

- https://www.theodinproject.com/courses/web-development-101/lessons/developer-tools-2?ref=lnav

## Assignment

- [ ] Head over to the [Chrome DevTools Documentation](https://developers.google.com/web/tools/chrome-devtools/) by Google. Read through the following (skip if familiar with):

  - [x] Open DevTools
    - `CTRL+SHIFT+C` to open inspector
    - `CTRL+SHIFT+I` || `F12` to open console
  - [x] Device Mode
    - Used to mock/prototype webpages on mobile devices.
    - Simulating mobile viewport, slowing down network and CPU, GPS. landscape mode.
    - [x] Device Mode (Simulate Mobile Devices with Device Mode)
  - [x] Elements Panel
    - [x] Get Started With Viewing and Changing CSS
    - [x] Get Started With Viewing And Changing The DOM
    - [x] Edit the DOM
  - [x] Using the Console
    - Log messages and make sure things run in the right order.
  - [ ] Sources panel
    - [x] Get Started with Debugging JavaScript
      - Use `Control+Shift+I` to open up the Console, click Sources tab.
      - `console.log()` is inefficient for debugging, use breakpoints instead because they let you pause in the middle of the code. They also let you see the all relevant variables at that moment. It can let you look at the code execution step-by-step.
      - You can pause with line break points or event breakpoints (e.g. mouse click). Check variable values with the **Scope** panefor a list of the local and global variable at the time or **Watch Expressions tab** to monitor specific variables or expressions over time or the **COnsole**
    - [ ] Pause Your Code With Breakpoints
        - **Line-of-code** breakpoints are most useful when you have a pretty good idea of where exactly to look... otherwise it'll be inefficient, esp. in a large codebase, which is why there are other types like:
        - **Conditional Line of Code** - pause on this exact line... but only if a certain condition is true. Right click the line number and click **Add conditional breakpoint**. 
        - **DOM** - pause on a line of code that changes the content on the page
        - **Event lister** - pause on a line of code that executes a listener, e.g. click 
        - **XHR** - unknown?
        - **Function** - pause when a function call occurs
        - **Exception** pause when something breaks and the console knows something broke
    

- [x] Then, watch [this video](https://www.youtube.com/watch?v=JzZFccCEgGA) by the Net Ninja for more details on using the JavaScript Console.
