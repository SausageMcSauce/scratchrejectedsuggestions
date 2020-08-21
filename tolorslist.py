# quote template:
# [quote="The Official List of Rejected Suggestions"]
# [/quote]

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
"""
 "1.3": """[quote="The Official List of Rejected Suggestions"][b]1.3 [url=https://scratch.mit.edu/discuss/topic/355056/?page=1#post-3603084]"Pointing towards sprite" boolean block[/url][/b]
This block would allow a sprite to detect if it is pointing towards another sprite.  However, it is also rather ambiguous; does it return true if the sprite is pointing in any direction towards another sprite, or strictly at the center of the sprite?  Either way, it is relatively easy to work around, and the workaround depends on how you want the block to work.

[scratchblocks]
<pointing towards [sprite v]? :: sensing>
[/scratchblocks]
[/quote]
"
}