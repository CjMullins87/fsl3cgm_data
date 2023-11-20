# FreeStyle Libre Database Builder

Fetches user data from the FreeStyle LibreLinkUp app, then writes the data that was retrieved to a local SQLite database. End goal is to unify components into a callable script that can run in crontab to successfully store long-term CGM data for custom reporting.

# Shout-out

I built this repo after reading someone else's detailed writeup of the workflow;
honestly, it was impossible to find detailed documentation from FSL themselves.
If you'd like to review their work and read for yourselves what's under the hood,
I'd encourage you to check here:

[Notes from khskekec](https://gist.github.com/khskekec/6c13ba01b10d3018d816706a32ae8ab2)

[Notes from InventiveTalentDev](https://github.com/InventivetalentDev/LibreViewApi/blob/master/LibreLinkUpApi.md)

# Getting set up

## Authorization Information

In the top directory of this repo, on your local machine, you'll need to create an
`fsl3_credentials.json` file to store relevant authentication information. This package
expects that you set up your file in this way:

```
{
    "user_info": {
        "user_email": "",
        "password": "",
        "patient_id": ""
    },
    "auth": {
        "token": "",
        "expires": ""
    }
}
```

The package will read your `user_email` and `password`, then use these to
fetch your patient ID and authorization token, and write them into this json file.
The packaged `.gitignore` expects that any credentials end with a `_credentials.json` suffix, so this shouldn't get accidentally published unless you force git to include it
in your commits.