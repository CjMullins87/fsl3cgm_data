# FreeStyle Libre Database Builder

Fetches user data from the FreeStyle LibreLinkUp app, then writes the data that was retrieved to a local SQLite database. End goal is to unify components into a callable script that can run in crontab to successfully store long-term CGM data for custom reporting.

# Shout-out

I built this repo after reading someone else's detailed writeup of the workflow;
honestly, it was impossible to find detailed documentation from FSL themselves.
If you'd like to review their work and read for yourselves what's under the hood,
I'd encourage you to check here:

[Notes from khskekec](https://gist.github.com/khskekec/6c13ba01b10d3018d816706a32ae8ab2)

[Notes from InventiveTalentDev](https://github.com/InventivetalentDev/LibreViewApi/blob/master/LibreLinkUpApi.md)
