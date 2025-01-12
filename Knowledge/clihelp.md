# Help on the CLI
For MAC

## basic commands

`mkdir` is the command to create a new directory or folder, example
> `mkdir new_home` creates a new directory called 'new_home'

`ls` is to list contents in a directory.  You can also target a directory to list contents with `ls <directory name>`

`cd` is to 'change directory.  
`cd..` will move you to the parent directory
`touch` will create a new file  

`source` runs commands from a file in the current shell session. This is particularly useful for loading environment variables or executing a series of shell commands without opening a new shell.

`echo` will print to the cli what goes after the command.  Use a `$` to call a variable from your `.bash_profile`.  Example:
>echo $USER


## Setting up the Environment

`env` Will display all configured environment variables.  These come from your `$/.bash_profile`
`~` is a simple way to move back to your home directory.

## .bash_profile
`echo` will echo text back, be sure to have a space.  
- `echo Hello World`
`alias` allows you to change or make short cuts.
- `alias p="pwd"`