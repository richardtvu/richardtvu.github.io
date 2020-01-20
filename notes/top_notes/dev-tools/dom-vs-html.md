# HTML vs. the DOM 

- https://developers.google.com/web/tools/chrome-devtools/dom/#appendix

- What is the difference between HTML and the DOM? 
    - "tree of objects" 
    - "nodes, representing the page's content"
    - HTML = "initial page content"
    - DOM = "current page content", the content that remains after JavaScript changes the content on the page. 
        - DOM = [Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) that represents the web content and is what is modified by JavaScript. Without it, you can't modify the webpage using JavaScript or another language 

- Things you can do by editing the DOM:
    - Hide/delete/change the style of a node.
    - reference the node via $0 in the console.
    - Force the state, e.g. always hover. 
    - Copy the JS path . 