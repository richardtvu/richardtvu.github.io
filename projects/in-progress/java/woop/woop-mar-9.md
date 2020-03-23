# WOOP March 9, 2020 

- Wish: I wish to complete three pomodoros of Java in which I am focusing and actively learning. 

- Outcome: I will feel disciplined, learned, and satisfyingly fatigued and ready to go to sleep. I'd feel proud of myself, satisfied with my ability to work even late at night. I would feel the uplifting of my chest, the straightening of my back, the depening of my voice, the lowering of my vocal cords as I say out loud to myself, "I've completed another tasks thanks to the burgeoning discipline I'm developing." 

- Obstacle: Getting side-tracked to look at other websites, to go on mental escapades and being off topic in my thinking. Getting bored and tired and fed up with the feeling that the material is not worth knowing. Thinking it's incomprehsnible. Feeling negative emotions and faitgue that take away from my mfocus. 

- Planning: If I feel negative emotions or distraction, THEN I will say those emotions out loud and acknowledge them, followed by telling myself that these emotions are a normal part of growth.

Result: 
- I set up a new project, downloaded the source files, and put the chapter 2 source files into the new project. Now, I'm trying to work on getting JavaFx set up in Eclipse, but I don't know where my SDK is or how to get the JavaFx. So I'll return back to the command line section.
- I had skipped the part about obtaining the JDK and JavaFx, so it makes sense as to why I was lost on it! I tried to download OpenJDK13, but it's 198 MB and will take forever to download. I'll still attempt to download it and JavaFx. I am trying to download:
    - openjdk13.0.2                            - ~195 MB
        - downloaded from https://jdk.java.net/13/
        - decided not to download jdk-13.0.2+8 (no idea what the +8 means) - ~198 MB from https://adoptopenjdk.net/ - because it was only download around 1.5 KB/S....
    - JavaFx Linux SDK 13.0.2                    ~45 MB
        - Downloaded from https://gluonhq.com/products/javafx/
        - Surprisingly fast download, moved to `~/eclipse`

- I found out where my openjdk folder is while waiting for my download to finish! It's at `/usr/share/openjfx/lib`.
- I became more comfortable with using the command line to run java programs. I cd'd to the src folder, compiled some programs, and then ran them with `cd`, `javac` and `java` respectively. Then, I cd'd to the bin folder and ran some programs there too. 

- I technically didn't have to, but I wanted to install JDK 13, so I used the command `sudo mv eclipse/jdk-13.0.2/ /usr/lib/jvm/` to move my jdk folder into the jvm folder. 
    ```
    export J2SDKDIR=/usr/lib/jvm/jdk-13.0.2
    export J2REDIR=/usr/lib/jvm/jdk-13.0.2/jre
    export PATH=$PATH:/usr/lib/jvm/jdk-13.0.2/bin:/usr/lib/jvm/jdk-13.0.2/db/bin:/usr/lib/jvm/jdk-13.0.2/jre/bin
    export JAVA_HOME=/usr/lib/jvm/jdk-13.0.2
    export DERBY_HOME=/usr/lib/jvm/jdk-13.0.2/db
    source /etc/profile.d/oraclejdk.sh.
    ```
    - I ran the above, logged out and logged back in... but still my java version is shown as being 11... Which is annoying! This is when I stop! 

Next time.... continue with setting up JavaFx with 11!