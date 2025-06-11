import re

def detect_format(text):
    """
    Detects if the text is in LaTeX, Markdown, or plaintext format
    Returns: 'latex', 'markdown', or 'plaintext'
    """
    # LaTeX detection patterns
    latex_patterns = [
        r'\\begin\{.*\}',  # LaTeX environments
        r'\\[a-zA-Z]+',    # LaTeX commands
        r'\$.*\$',         # Inline math
        r'\$\$.*\$\$'      # Display math
    ]
    
    # Markdown detection patterns
    markdown_patterns = [
        r'#{1,6}\s',       # Headers
        r'\*\*.*\*\*',     # Bold
        r'\*.*\*',         # Italic
        r'\[.*\]\(.*\)',   # Links
        r'```.*```',       # Code blocks
        r'^\s*[-*+]\s',    # Lists
        r'^\s*\d+\.\s'     # Numbered lists
    ]
    
    # Check for LaTeX
    for pattern in latex_patterns:
        if re.search(pattern, text):
            return 'latex'
    
    # Check for Markdown
    for pattern in markdown_patterns:
        if re.search(pattern, text):
            return 'markdown'
    
    return 'plaintext'

def assert_upload(data):
    errstring = ""
    
    # Check required fields
    if "username" not in data:
        errstring += "User field missing! "
    elif not data["username"].strip():
        errstring += "Username cannot be empty! "
        
    if "actual_data" not in data:
        errstring += "Actual data field missing! "
    elif not data["actual_data"].strip():
        errstring += "Content cannot be empty! "
    elif len(data["actual_data"]) > 10000:  # Reasonable limit for text content
        errstring += "Content exceeds maximum length of 10000 characters! "
    
    if errstring:
        raise ValueError(errstring)
    
    # Detect format
    format_type = detect_format(data["actual_data"])
    
    return {
        "status": "No issues",
        "format": format_type
    }