> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/syntax-glob.html
> Downloaded: 2026-10-18

# Working with glob patterns in syntax

When you specify the files or paths that are used in pipeline artifacts or source locations, you can specify the artifact depending on the action type. For example, for the S3 action, you specify the S3 object key. 

For triggers, you can specify filters. You can use glob patterns to specify filters. The following are examples.

When the syntax is "glob" then the String representation of the path is matched using a limited pattern language with a syntax that resembles regular expressions. For example: 
 `*.java` Specifies a path that represents a file name ending in .java 
` *.*` Specifies file names containing a dot 
 `*.{java,class}` Specifies file names ending with .java or .class 
 `foo.?` Specifies file names starting with foo. and a single character extension 

The following rules are used to interpret glob patterns: 
To specify zero or more characters of a name component in directory boundaries, use `*`. 
 To specify zero or more characters of a name component crossing directory boundaries, use `**`. 
To specify one character of a name component, use `?`. 
To escape characters that would otherwise be interpreted as special characters, use the backslash character (`\`). 
To specify a single character out of a set of characters, use `[ ]`. 
To specify a single file that is in the root of your build location or source repository location, use `my-file.jar`. 
To specify a single file in a subdirectory, use `directory/my-file.jar` or `directory/subdirectory/my-file.jar`. 
To specify all files, use `"**"`. The `**` glob pattern indicates to match any number of subdirectories. 
To specify all files and directories in a directory named `directory`, use `"directory/**"`. The `**` glob pattern indicates to match any number of subdirectories. 
To specify all files in a directory named `directory`, but not any of its subdirectories, use `"directory/*"`. 
 Within a bracket expression the `*`, `?` and `\` characters match themselves. The (-) character matches itself if it is the first character within the brackets, or the first character after the `!` if negating. 
 The `{ }` characters are a group of subpatterns, where the group matches if any subpattern in the group matches. The `","` character is used to separate the subpatterns. Groups cannot be nested.
