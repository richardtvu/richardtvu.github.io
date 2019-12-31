Tribute to Jordan Peterson
===

## What inspired me to start this project? 

I was listening to the Daily Software Engineer (or a podcast with a similar name) where Quincy Larson laid out his vision for what he wanted freeCodeCamp to be in the future. This listen sparked a desire to check out freeCodeCamp (FCC) and do one of the projects. I chose the Tribute Page project. Then, I thought about my heroes and the one that was above all the rest is Dr. Jordan Peterson.

I started listening to Dr. Jordan Peterson around Winter 2016 (give or take a year) in my senior year at Swarthmore College. Later on, in Spring, I found out that none of the graduate schools I applied to had accepted me. I was devastated, lost. I felt broken and worthless. I felt that it made sense and used that event and others to put myself down as someone who wasn't cut out as a competent person. However, hundreds of hours of Dr. Jordan Peterson's podcasts and lectures helped me come to terms with reality, helped me develop a hope that I can still make a meaningful difference in others' lives and develop meaning in my own. His thoughtful, optimistic (once you get past the cynicism that is necessary because of life's inherent suffering) outlook on life, and the fatherly nature of how he acted helped me to take a risk and become an educator for two years as I tested out whether that path was going to be meaningful to me and then switch over to technology as another leap of faith and opportunity to instruction.

Now, I'm doing level 1 helpdesk work and learning how to program on the side. I've toned down the self-criticism and have started taking better care of myself. I've begun a new course called *The Science of Well-Being* on Coursera and am more optimistic that with hard work, adherence to honesty and integrity and truth, and incremental development, I can become a better Rich. Of course, I still have my moments, hours, days, of doubt and despair or apathy and self-destruction, but those periods are less frequent and I recover and get back on my self-care routine much faster than before. I've acknowledged my shadow and work to integrate it rather than suppress it. I've worked to develop myself and climb the social hierarchy. I've worked to cultivate and practice my own set of moral principles (largely based on the principles laid out by Dr. Peterson). I'm on the hero's journey.

Dr. Peterson is the father that thousands, hundreds of thousands of men, perhaps even millions of men that never had a positive father figure to guide them. I wish to do what little I can and take a leap of faith that even if my tribute project isn't the best, at least it can promote some good ... whether it's in my own life or somebody else.

## What do I want my tribute page to look like? (December 29, 2019)

* Here are some ideas:
    - Navigation Bar on top with links to Dr. Jordan Peterson's YouTube, to his Website, ..., to a horizontally orientated timeline showing his rise to prominence, etc.
    - Make the tribute page look like a book:
        - Background: Wooden Table to Rest the Book On 
        - Laid out on a table. Each webpage has two "book pages" to mimic an actual book with a divide in the middle. 
        - A Front Page
            - Dr. Jordan Peterson's Name at the Top
            - Dr. Jordan Peterson's Portrait in the middle.
            - A Background Picture of Thick Book with a Clasp
                - The clasp should start off being closed. 
                - Once the user hovers over the clasp, the clasp should be shown as opened
        -  A Table of Contents on the Next Page with:
            - A Earmark at the Bottom with a Picture of a Thumb
                - When the user hovers over the thumb, a picture with a preview of the top-right hand corner of the next page should pop up. There should be a diagonal where the previous (current) page has been lifted up to reveal the next page. 
            - Background: 
                - Aged and yellowing paper 
                - Medieval Type Font (?) 
            - Hyper Links to:
                - A Timeline of Dr. Jordan Peterson's Rise to Fame
                - An Embedded Video with "A Message to Millenials." 
                - Extra Resources 
                    - Should contain links to Dr. Peterson's website, Quora/Wikipedia for his life, news articles/etc. 
    - BOOK MVP: 
        - Front Page (see above) w. 
            - Textbox called "OPEN" on the center right portion of the webpage instead of a clasp. 
            - Make the text a hyperlink to the table of contents
        - Table of Contents: 
            - A header saying "Table of Contents"
            - Bulleted list of links to pages 
            - A textbook in the top-right corner of the screen that says "NEXT"
            - Make the "NEXT" clickable 
        - Timeline: 
            - Make a horiztonally oriented webpage that scrolls to the right but not down. 
            - Clickable "NEXT" in top right corner. 
            - Clickable "BACK" in top left corner. 
        - Message to Millenials 
            - Centered heading saying "A Message to Millenials." 
            - Centered textbox with a border for where the video will be. 
            - Clickable "NEXT" in top right corner. 
            - Clickable "BACK" in top left corner. 
        - Extra resources:
            - Title: "Learn More About Dr. Peterson." 
            - Bulleted list of hyperlinks to his website, quora, wikipedia, news articles 

        
        

## Timeline: 

* December 30, 2019 / Monday: 
    - Today, my goal is to get the outline of the front page and the table of contents running.
        - [x] A Front Page

            - [x] Dr. Jordan Peterson's Name at the Top
            - [x] r. Jordan Peterson's Portrait in the middle.
            - [x] Textbox called "OPEN"
            - [x] Make the text a hyperlink to the table of contents

        - [x] Table of Contents: 
            - [x] A header saying "Table of Contents"
            - [x] Bulleted list of links to pages 
            - [x] Clickable NEXT button
            - [x] Include the block quote on the bottom of the webpage 
* December 31, 2019 / Tuesday: 
    - In my journaling session, I had some images pop up into my head about how I want my tribute to look. Imagine a rectangle that represents the web browser. The top part of it is going to be the bar. Whatever else that remains is going to be the "wood" table upon which the book will rest. IN the lower-left hand corner of the screen, there will be a candle that will "light" up the page for the user to see (perhaps, it should be a yellow-ish light?). 
        - In the beginning, when the book is closed. The book should be centered in the middle of the table, with the clasp, etc. pages, etc. 
        - Once the book is opened, it should look like an open book with a left and right page. The clasp should sitll be there, perhaps on the right or left side. Each time the page is flipped, the table, candle, clasp should remain there. 
    - By the way, I may have said "will" before, I don't mean that I intend to carry it to fruition. I mean "will" as in how it will look if I were to implement that idea. This project is more of an exploration for me than it is something that I *have* to complete. 
    - Thus, what do I want to do today? 
        - Since I completed the above placeholder content, now it's time to do the following: 
            - [x] Make the "OPEN" button in the front page positioned in the center-right of the page.
                - I think I can do this by using a flexbox and having the elements flow from left to right in a row, instead of a column. That way, the open will already be  positioned on the right. 
            - [x] Position the NEXT button at the top-right of the page. 
    - After positioning the table of contents' left and right pages, I noticed that there doesn't seem to be enough room for both a left and right side.... esp. if I want to make this a mobile-friendly website. Perhaps, I should split the left and right pages into their own separate webpages. Then, I can have the pages be bigger and still readable on a mobile device. Okay, supposing I did that, how would I want to change my timeline? I think that if I were to do that, to be consistent with the rest of my pages, I'd want my timeline to go from top to bottom instead of left to right, so that users can just scroll down. 
        - [ ] Split Table of Contents into two: (1) Table of Contents (with the links) and (2) Quote page. 

