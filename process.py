#!/usr/bin/env python

import markdown  # Home-page: https://Python-Markdown.github.io/
import sys

def markdown_to_html(markdown_text):
    # Create a Markdown instance
    md = markdown.Markdown(extensions=['extra'])
    
    # Convert Markdown to HTML
    html_content = md.convert(markdown_text)
    
    # Wrap the converted content in a complete HTML structure
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Converted Markdown</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    return full_html


def main():
    markdown_text = open(sys.argv[1]).read()
    html_output = markdown_to_html(markdown_text)
    print(html_output)

if __name__ == '__main__':
    main()
