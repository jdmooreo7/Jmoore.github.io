# let's start

How to create a swift file from Terminal
 `touch <filename.swift>`

 This creates the file, next update the file you can use nano or any text editor.  
 `nano filename.swift`

Once the file is created and you added content, for example:
`print("Hello World!")`

 you can compile from the command line.
 `swiftc filename.swift`.  

 last step is to run your program from the command line
 `./filename`

## Syntax

### Comments

- `//` allows you to put a single line of comment in your code
- `/*  */` allows you to have multiple lines of comments

### Variables

- `var` is a keyword used to declare a variable

>Varible names should be camelCase format
>
#### Type

- `Int`: integer number
- `Double`: floating-point number (example, 1.89)
- `String`: a sequence of charaters
- `Bool`: true/false values
- `:` is used to set the type

>[example]
var artist: String = "some letters"
Above enfources that the variable 'artist' will always be a string

#### Arithmetic Operators

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `%` modulo (divides and gives the remainder)

#### Compound Operators

Allow you to reference a variable twice.  Examples are:
-`+=` add and assign the sum
-`-=` subtract and assign the difference
-`*=` multiply and assign the product
-`/=` divide and assign the quotient
-`%=` divide and assign the remainder
When using compound operators be sure to have a space before and after.

### Constants

- `let` sets a varible as a constant immutable value
