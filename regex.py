import re

# Sample text containing a Windows path with spaces
text = r'C:\Windows\Admin\Desktop\All Files\Interview-Programs\test.py and there is one C:\Windows\Admin\Desktop\mypython.py'

# Regular expression pattern for Windows file paths with spaces
pattern = r'[A-Za-z]:\\(?:[A-Za-z0-9_\\\-\s]+\\)*[A-Za-z0-9_\\\-\s]+\.[A-Za-z0-9]+'

