# quote template:
"""
[quote="The Official List of Rejected Suggestions"]
[/quote]
"""

tolorslist = {
  "1.1": """[quote="The Official List of Rejected Suggestions"][b]1.1 [url=https://scratch.mit.edu/discuss/topic/73978/?page=1#post-634620]"Broadcast received" boolean block[/url][/b]
This would allow a project to detect when a broadcast is sent.  But, there is a lot of ambiguity on how this would work.  Would it return true if the broadcast was fired since the project was created, since the green flag was clicked, or since something else was broadcasted?  The workaround is simple: use variables that change when a broadcast is received, then use the "equals" block.

However, the blocks "repeat until broadcast received" and "wait until broadcast received" are NOT rejected; you can discuss them on [url=https://scratch.mit.edu/discuss/topic/324844/]this topic[/url].

[scratchblocks]
<[message v] received? :: events>
[/scratchblocks]
[/quote]
""",
 "1.2": """[quote="The Official List of Rejected Suggestions"]
 [b]1.2 [url=https://scratch.mit.edu/discuss/topic/205920/?page=2#post-2070854]"When stop sign clicked" hat block[/url][/b]
This block would allow users to click the stop sign to run a script.  However, the stop sign is designed to stop all the scripts in the project.  With this block in place, more scripts will start when you want the project to stop, thus defeating the purpose of the stop sign.  This could also be rather confusing for the "stop all" block.  Regardless, there is a workaround that uses the "when (timer) > (number)" hat block; one such workaround can be found in [url=https://scratch.mit.edu/discuss/post/3547555/]this post[/url].

[scratchblocks]
when stop sign clicked :: events :: hat
[/scratchblocks]

[/quote]
""",
 "1.3": """[quote="The Official List of Rejected Suggestions"][b]1.3 [url=https://scratch.mit.edu/discuss/topic/355056/?page=1#post-3603084]"Pointing towards sprite" boolean block[/url][/b]
This block would allow a sprite to detect if it is pointing towards another sprite.  However, it is also rather ambiguous; does it return true if the sprite is pointing in any direction towards another sprite, or strictly at the center of the sprite?  Either way, it is relatively easy to work around, and the workaround depends on how you want the block to work.

[scratchblocks]
<pointing towards [sprite v]? :: sensing>
[/scratchblocks]
[/quote],
""",
 "1.4": """[quote="The Official List of Rejected Suggestions"]
 [b]1.4 [url=https://scratch.mit.edu/discuss/topic/144248/?page=3#post-1333242]Money blocks[/url][/b]
This block, and others, could be used to ask users to pay real money in order to do something in the project.  The problem with such money blocks is that many users on the website are young and do not quite know how money works (and most do not even have a credit card account).  Users could make projects which require others to pay a large amount of money in order to play the project.  Overall, it adds further complexity to the website, and would limit users' access, without any clear benefit towards the educational value.

[scratchblocks]
ask for [$ v] () and wait :: sensing
[/scratchblocks]
[/quote]""",
 "1.5": """
[quote="The Official List of Rejected Suggestions"]
[b]1.5 [url=https://scratch.mit.edu/discuss/topic/366316/?page=1#post-3669210]Social action reporter blocks[/url][/b]
This block could be used to obtain the current number of loves, favorites, or views of the project.  Similar blocks could return the number of loves or followers that the user or creator has.  But, project creators can easily use these blocks to prevent Scratchers from playing unless the project is given enough loves, favorites, and the like.  These blocks could also make people think that getting these social actions are important, or that Scratch is about fame.  In reality, if a user presses the love button on a project, it should be because they enjoyed the project, not because they are trying to reach some sort of goal.

This suggestion extends to all social actions, including views, loves, favorites, remixes, comments, and followers.

[scratchblocks]
(number of [loves v] :: sensing)
[/scratchblocks]
[/quote]
""",
 "1.6": """[quote="The Official List of Rejected Suggestions"]
 [b]1.6 [url=https://scratch.mit.edu/discuss/topic/348978/?page=1#post-3528653]Cloud lists[/url][/b]
Cloud variables currently have several restrictions.  There can be at most 10 cloud variables per project due to server costs.  New Scratchers cannot use cloud variables, for it is easy to misuse them.  Cloud variables can only support up to 256 numeric digits to restrict the creation of chat projects; for more information, see #3.1 on this list.  

This block would allow you to create lists to be stored on the servers for everyone to see, similar to cloud variables.  However, cloud lists would require similar restrictions as listed above, and the issues currently presented with cloud variables would only grow with the addition of cloud lists.  You can still use cloud variables to create a list which contains entries everyone can see, but the Scratch Team will not be adding an easy official way to make cloud lists.

[scratchblocks]
(☁ list :: list)
[/scratchblocks]
[/quote]""",
 "1.7": """[quote="The Official List of Rejected Suggestions"]
 [b]1.7 [url=https://scratch.mit.edu/discuss/topic/367418/?page=2#post-3684338]2D lists[/url][/b]
2D lists, also known as 2D arrays, nested lists, or matrices, are a type of data structure that allows you to put an entire list as an element of another list; that is, it allows you to put lists inside of lists.  These sorts of data structures are used widely in other programming languages.

This block, and others, would allow you to create 2D lists to store information, sort of like a table.  However, this is too complicated for what is supposed to be an introductory programming language.  In addition, there are workarounds possible by using an ordinary list and an indexing function.  For those who are interested, it may be worth checking out [url=https://snap.berkeley.edu/]Snap![/url].  It is a block-based programming language designed for more experienced programmers, and has more advanced data structures than Scratch does.

[scratchblocks]
add () to sublist () of [list v] :: list
[/scratchblocks]
[/quote]""",
 "1.8": """[quote="The Official List of Rejected Suggestions"]
 [b]1.8 [url=https://scratch.mit.edu/discuss/topic/982/?page=6#post-272115]3D Scratch[/url][/b]
This block, and others, could be used with a z-axis in the project stage to make it easier to create 3D projects.  But, Scratch is a language that is designed to be as easy as possible for beginners to learn.  Adding 3D features would make the language more difficult for beginners to understand, and a 3D engine is not exactly the purpose of Scratch.  This suggestion also includes the possibility for a virtual-reality features in Scratch, or "Scratch VR."  A lot of the same difficulties come up.

There is a similar program to Scratch that contains block programming with 3D features, called [url=https://education.mit.edu/project/starlogo-tng/]Starlogo TNG[/url]. You can also try [url=http://www.alice.org/]Alice[/url]; it is not exactly like Scratch, but has some similar features.

[scratchblocks]
go to x: () y: () z: () :: motion
[/scratchblocks]
[/quote]""",
 "1.9": """
[quote="The Official List of Rejected Suggestions"]
[b]1.9 [url=https://scratch.mit.edu/discuss/topic/97802/?page=4#post-3834969]Pi reporter block[/url][/b]
This block would return the mathematical constant pi (or π).  Although used extensively in math, it is not used very commonly in Scratch.  For those who do need to use pi, a decimal approximation is generally accurate enough.  Simply make a variable called "pi" and set it equal to 3.14159265.

[scratchblocks]
(pi :: operators)
[/scratchblocks]
[/quote]
""",
 "1.10": """
[quote="The Official List of Rejected Suggestions"]
[b]1.10 [url=https://scratch.mit.edu/discuss/topic/419282/?page=1#post-4186455]"Control mouse pointer" block[/url][/b]
This block, and others, could be used to hide the mouse pointer or change the way the mouse pointer looks in a project.  These blocks, however, do not significantly change the types of projects that can be created with Scratch; for more information, see [url=https://scratch.mit.edu/discuss/topic/190673/?page=5#post-3889314]this post[/url].  In addition, they may cause confusion to users, wondering where the mouse pointer went.  A feature to control the mouse pointer, including freezing it or preventing it from leaving the project screen, poses similar confusing problems.

[scratchblocks]
hide mouse pointer :: looks
[/scratchblocks]
[/quote]
""",
 "1.11": """
[quote="The Official List of Rejected Suggestions"]
[b]1.11 [url=https://scratch.mit.edu/discuss/topic/405581/?page=1#post-4034761]"Forever if" C block[/url][/b]
This block was in the Scratch 1.4 editor, and worked the same as putting an "if" block inside the existing "forever" loop.  It was removed in Scratch 2.0 because many beginning Scratchers found it to be confusing.  The aforementioned workaround, evidently, is simple and more intuitive.

[scratchblocks]
forever if <> { } :: control cap
[/scratchblocks]

[/quote]
""",
 "1.12": """
[quote="The Official List of Rejected Suggestions"]
[b]1.12 [url=https://scratch.mit.edu/discuss/topic/411208/?page=1#post-4094599]Letters in cloud variables[/url][/b]
Some users would like an easy way to set cloud variables to values which include letters.  Such a feature was present in the beta version of Scratch 2.0.  However, allowing letters in cloud variables would cause a lot of moderation issues.  For instance, it would make it too easy to make inappropriate cloud chat projects; for more information, see #3.1 on this list.  Hence the feature was removed, and so cloud variables can now only be set to numeric values.

By encoding and decoding, it is possible to simulate letters in cloud variables, but in reality they are just using numbers in cloud variables and letters in normal variables.

[/quote]
"""
}