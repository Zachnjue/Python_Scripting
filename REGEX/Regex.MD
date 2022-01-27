- The regex is a procedure in any language to look for a specified pattern in a given text

- re is the module to perform regex in python i.e. use import re in scripts

- There are different operations in re like:

  - search, match, finditer, findall, split, sub, etc

- Syntax:

  - re.search(pattern, text)
  - re.match(pattern, text)
  - re.finditer(pattern, text)
  - re.findall(pattern, text)

  - search - user r'pattern'

- simple examples of patterns"

  - "python" - search the whole word
  - "python[23]" - search for "python2" and "python3"

- Rules to create a pattern
- a, x, 9 - ordinary characters that match themsleves
- [abc] - matches a or b or c
- [a-c] - matches a or b or c
- [a-zA-Z0-9] - matches any letter from (a to z) or (A to Z) or (0 to 9)
- \w - Matches any single letter, digit or underscore but does not match any space & hyphens i.e. A-Z,a-z,0-9,\_
- \W - Matches any character but part of \w
- \d - Matches decimal digit 0-9
- . - Matches any single character except newline character
- ^ - matches the word tt the beginning of a given text
- $ - Matches the word at the end of a given text
- \b - Matches a word with a space on the left
- \B - Empty string not at the beginnnins or end of a word i.e. no space on the left
- \t, \n, \r - Matches tab, newline, return respectively.

More Rules:
{2} - indicate the number of times
{2,4} - indicates 2,3 or 4 times
{2,} - 2 or more times
? - once or none

Simple Flags for Regex:
re.I - re.IDNORECASE - makes the regular expression case-insensitive
re.L - re.LOCALE - The behaviour of some special sequences like \w,\W,\b,\s,\S will be made dependedant on the local i.e. user's language, country also
re.M - re.MULTILINE - ^ and $ will match the beginning and at the end of each line and not at the beginning and the end of the string
re.S - re.DOTALL - The dot "." will match every character plus the newline
re.U - re.UNICODE - Makes \w,\W,\b,\B,\d,\D,\s,\S dependent on Unicode character properties
re.X - re.VERBOSE - Allowing "verbose regular expressions", i.e. whitespace are ignored. This means that spaces, tabs and carriage retuens are not matched as such.If you want to match a space in a verbose regular expressio, you'll need to escape by escaping it with a backlash in front of it or include it in a charater class. # are also ignored, except, when in a character class or preceded by an non-escaped backlash. Everything flowing a "#" will be ignored until the end of the line, so that this character can be used to start a comment 
