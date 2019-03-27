## What we're working with

- The solution can be expected to work in a network semi-actively so we can assume to have a reliable network connection. 
- The files we want to transfer are simple text files so it doesn't require massive amounts of bandwidth
- They do contain information that needs to be transferred securely
- Needs to be possible to automate

## Thoughts

Setting up a webserver with something like **python-SimpleHTTPServer** is an option and using wget, but that just seems a bit much for 
a simple text file. And I'm not certain how secure that might be, since obiviously we don't want to leak any data accidentally.

Are there really other good options to use than **scp** or **sftp**? Might be later on, but for the pilot I think using the most simple solution
might be better, any extra hassle takes time.

## scp vs sftp

I think it comes down to speed. Both use SSH, so they're both as reliable in terms of security.

Using SSH enables using keys for authorization, so both can presumably automated using a single bash script.

We only need to move a single file that and rewriting over said file is not a problem.

We don't need to manage the sent file or directory it goes into in any way after the file transfer is complete.

I think **scp** is the way to go here. For now.
