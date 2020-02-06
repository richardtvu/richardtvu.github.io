# The Pseudocode Programming Process

- [Coding Horror](https://blog.codinghorror.com/pseudocode-or-code/)
- [Steve Yegge](http://steve-yegge.blogspot.com/2008/02/portrait-of-n00b.html)
- [Wikihow](https://www.wikihow.com/Write-Pseudocode)

- What is the pseudocode programming process?

  - Start with the general idea of what you want to do with the program
  - Break it down until the next step becomes code and then code it
  - According to Wikihow, it's the process of outlining your code in a step-by-step manner. This process helps you think through program problems and as a byproduct help you communicate ideas to other people since you've written things out in an easy-to-understand manner.

- What should you remember when writing pseudocode? (Wikihow)

  - The pseudocode _explains_ what the code should do, not actually be the code, so it shouldn't contain actual code.
  - Keep it simple with minimal formatting.
  - Structure:

    - Begin with 1-2 sentences to explain purpose of code.
    - Write only **one statement per line**.

      - Each line of pseudocode should correspond to just one task / action for the computer to carry out.

    - Use white space and indentation to:

      - Separate blocks of text
      - Organize sub-sections under bigger blocks.

    - Capitalize key commands, if necessary, e.g. IF.
    - Write simply about what the program will do.
    - Make sure the pseudo-code is ordered in the way you want things tob e executed.
    - Explain things completely... Instead of variables, explain what it'll do with actual data?
    - Use standard programming structures.
    - Organize pseudocode with:

      - brackets if it's too big

- What is Wikihow's checklist of things the pseudo-code should fulfill? Copy-pasta... You should be able to answer the following questions by the end of the document:

  - Would this pseudocode be understood by someone who isn't familiar with the process?
  - Is the pseudocode written in such a way that it will be easy to translated it into a computing language?
  - Does the pseudocode describe the complete process without leaving anything out?
  - Is every object name used in the pseudocode clearly understood by the target audience?
  - If you find that a section of pseudocode needs elaboration or it doesn't explicitly outline a step that someone else might forget, go back and add the necessary information.

- Why is the PPP useful? According to comments on _Coding Horror_:

  - It allows you to communicate what code is doing to

    - non-coders, like business analysts who work with you.

      - e.g. When business rules change, documenting what each step of an algorithm does is useful in determining how to change the algorithm to fit the new rules.

    - teammates, when you're trying to get everyone on the same page

    - the future you / others trying to understand the code

  - Helps you visualize the _scope_ of the work and the _complexity_ of the work required.

  - Lets you abstract and look at things from a much higher-level than what programming languages can express

    - Gives you a high-level overview of what the code is supposed to do, so you have a guide on what to do next
    - Helps you explain the problem/action with the _minimum_ detail needed
    - Helps you think _beyond_ the box that a language typically constrains

  - Mimics the diffuse --> focused approach of learning in neuroscience. Starting with broad outline before diving into the details. Getting down the _design_ before diving into the _details_.

  - Helps you scaffold your understanding of code does by building on top of what you know about English

- According to _Steve Yegge_, pseudocode programming process is useful as a way to build up and internalize understanding of the code, to make use of the immensely complex and scary code that a junior has not adequately built an understanding of yet. As you increase in skill level, the amount of commenting decreases because you get more and more comfortable thinking in code. Your ability to _tolerate_ code compression increases: Just as you become more adept at reading difficult material, such as journal articles with experiene, so do you become more adept at reading dense, concise code.
