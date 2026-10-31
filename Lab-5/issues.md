| Issue | Type | Line(s) | Description | Fix Approach |
| ----- | ---- | ------- | ----------- | ------------ |
| SQL injection (B608) | Security, Medium | 11 | INSERT query built by string concatenation, so a crafted title can alter the query | Use ? placeholders with a parameter tuple |
| subprocess with shell=True (B602, B607, B404) | Security, Low | 3, 37 | Shell invoked and subprocess imported just to print a message | Remove subprocess, use print() |
| Hardcoded password (B105) | Security, Low | 7 | CURATOR_PASSWORD stored in source and never used | Remove it |
| Unused import (W0611, F401) | Quality | 2 | datetime imported but never used | Remove the import |
| Unused argument (W0613) | Quality | 15 | curator parameter never used in displayStatus | Remove the parameter |
| Naming (C0103) | Style | 10, 15, 24, 31, 36 | camelCase function names | Rename to snake_case |
| Missing docstrings (C0114, C0116) | Style | 1, 10, 15, 24, 31, 36, 40 | No module or function docstrings | Add docstrings |
| Unnecessary else (R1705) | Quality | 17 | else after return | Remove else, use a conditional expression |
| Crash on missing id | Bug | 16-17 | row[0] raises TypeError if the id does not exist | Check row is None first |
| Line too long (E501, C0301) | Style | 6, 11, 16, 26, 32 | Lines over 79 characters | Wrap lines |
| Blank lines and spacing (E303, E225) | Style | 24, 25 | Too many blank lines, total=0 | Fix spacing |
| Missing final newline (W292, C0304) | Style | end of file | File did not end with a newline | Add exactly one trailing newline |
