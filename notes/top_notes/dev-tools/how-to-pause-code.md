# How to Pause Your Code With Breakpoints in Chrome DevTools

- https://developers.google.com/web/tools/chrome-devtools/javascript/breakpoints

- What are my learning goals for taking notes on this topic?
  - Learn about when to use each breakpoint type.

## What are the different breakpoint types? When should you use them?

- If you know exactly where the broken code is and want to pause execution when the line is reached regardless of other conditions, use the `line-of-code` breakpoint. Otherwise, use:
  - `Conditional line-of-code` breakpoints when you want to pause on a line of code only when (a) certain condition(s) is(are) true.
  - `DOM` breakpoints to pause when changes are made to the structure/content of the page using JavaScript.
  - `XHR` - **to be filled in**
  - `Event listener` breakpoints when you want to pause on code that runs in response to an event, e.g. `click`.
  - `Exception` - breakpoints when you want to pause on code that is causing an error message to be thrown (?),
  - `Function` breakpoints when you want to pause after the script calls for a specific function

### Line-of-code: What are two ways in which you can use line-of-code breakpoints in your code?

1. Click on the line number in the script located in the **Sources** tab of DevTools.

2. Type `debugger;` on the line where you want to pause. E.g.:

   ```JavaScript
   console.log('a'); // line 1
   console.log('b'); // line 2
   debugger; // pauses here, line 3
   console.log('c');
   ```

## Conditional line-of-code.

- How do you use conditional line-of-code breakpoints?
  - In the **sources** tab, right-click the line number of interest and select **Add conditional breakpoint** and enter the condition.
- How do you manage these breakpoints?

  - Use the **Breakpoints** pane underneath the sources tree display and check/un-check those breakpoints.

    - Right-click in pane to disable all breakpoints.

## DOM

- How do you use DOM breakpoints?
  - Go to **Elements** tab.
  - Right-click element of interest and expand `Break on...` menu to select one of the three options.
- What are the different types of DOM change breakpoints?
  1. subtree modifications - when the components contained with the element of interest are changed e.g. body tag is changed in the html tag ... Not triggered when attributes of child node are changed or when the current node, but not the children are changed.
  2. attribute modifications - changes to attributes in the elements
  3. node removal - when the element of interest is removed.

## XHR/Fetch breakpoints

- What are XHR/Fetch breakpoints?
  - Commands to the debugger to pause execution of the script when a part of a URL matches a specified substring.
- Why would you want to use them?
  - Sometimes your webpage will request an incorrect URL, so you want to figure out where that's happening, so you can fix it (e.g. when a URL has `org` in it)
- How do you use them?
  - **Sources** > XHR Breakpoints tab > `+` and then add the breakpoint for the string of interest

## Event listener breakpoints: What are and how can you use event listener breakpoints?

- Expand the **Event Listener Breakpoint** pane from the **Sources** Tab and select the event of interest to pause when that event occurs.

## Exception breakpoints: How do you use them?

- Click on the **Pause on exceptions** button in the **Sources** tab to pause on uncaught exceptions. To include **caught exceptions**, check that box below.

## Function breakpoints: How do you use function breakpoints?

- `debug(functionName)`, e.g. `debug(sum)` will pause when `sum()` is called after the `debug(sum)` call. 
- `ReferenceError` will occur if you try to debug a function that is out of scope, that is, private and hidden inside another function. To fix this, call debug on that function when that function is in scope, e.g. within the function it is in. 