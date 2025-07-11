#!/usr/bin/env python3
"""
Email to Markdown converter for KFC Review emails.
Safely converts email files to markdown format for PR review.
"""

import re
import sys
import os
from datetime import datetime
from email import message_from_string
from email.policy import default
import html
import argparse


def clean_html(html_content):
    """Safely strip HTML tags and decode entities."""
    # Remove HTML tags
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    # Decode HTML entities
    clean_text = html.unescape(clean_text)
    # Clean up whitespace
    clean_text = re.sub(r'\n\s*\n', '\n\n', clean_text)
    return clean_text.strip()


def extract_text_content(msg):
    """Extract text content from email message."""
    content_parts = []
    
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    content_parts.append(payload.decode('utf-8', errors='ignore'))
            elif part.get_content_type() == "text/html":
                payload = part.get_payload(decode=True)
                if payload:
                    html_content = payload.decode('utf-8', errors='ignore')
                    clean_content = clean_html(html_content)
                    content_parts.append(f"[HTML Content - Cleaned]\n{clean_content}")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            content = payload.decode('utf-8', errors='ignore')
            if msg.get_content_type() == "text/html":
                content = clean_html(content)
            content_parts.append(content)
    
    return '\n\n---\n\n'.join(content_parts)


def email_to_markdown(email_file_path):
    """Convert email file to markdown format."""
    try:
        with open(email_file_path, 'r', encoding='utf-8', errors='ignore') as f:
            email_content = f.read()
        
        # Parse email using email library
        msg = message_from_string(email_content, policy=default)
        
        # Extract filename for title
        filename = os.path.basename(email_file_path)
        
        # Build markdown
        markdown = f"# Email: `{filename}`\n\n"
        
        # Add metadata
        markdown += "## Email Headers\n\n"
        
        # Key headers
        key_headers = ['From', 'To', 'Subject', 'Date', 'Reply-To', 'Message-ID']
        for header in key_headers:
            value = msg.get(header)
            if value:
                # Clean up header value
                clean_value = re.sub(r'\s+', ' ', str(value)).strip()
                markdown += f"**{header}:** `{clean_value}`\n\n"
        
        # Other headers
        other_headers = []
        for key, value in msg.items():
            if key not in key_headers and not key.startswith('X-'):
                clean_value = re.sub(r'\s+', ' ', str(value)).strip()
                other_headers.append(f"**{key}:** `{clean_value}`")
        
        if other_headers:
            markdown += "<details>\n<summary>Additional Headers</summary>\n\n"
            markdown += '\n\n'.join(other_headers)
            markdown += "\n\n</details>\n\n"
        
        # Add content
        markdown += "## Email Content\n\n"
        
        content = extract_text_content(msg)
        if content:
            # Split content into manageable chunks
            lines = content.split('\n')
            if len(lines) > 100:  # Limit for review
                content = '\n'.join(lines[:100])
                content += f"\n\n*[Content truncated - {len(lines)-100} more lines available]*"
            
            markdown += "```\n"
            markdown += content
            markdown += "\n```\n\n"
        else:
            markdown += "*No readable content found*\n\n"
        
        # Add file info
        markdown += "## File Information\n\n"
        file_size = os.path.getsize(email_file_path)
        markdown += f"- **Filename:** `{filename}`\n"
        markdown += f"- **Size:** {file_size} bytes\n"
        markdown += f"- **Processed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
        
        return markdown
    
    except Exception as e:
        error_md = f"# Email Parsing Error\n\n"
        error_md += f"**File:** `{os.path.basename(email_file_path)}`\n\n"
        error_md += f"**Error:** {str(e)}\n\n"
        error_md += "```\n"
        # Fallback to raw content (first 50 lines)
        try:
            with open(email_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()[:50]
                error_md += ''.join(lines)
        except:
            error_md += "Could not read file content"
        error_md += "\n```\n\n"
        return error_md


def main():
    parser = argparse.ArgumentParser(description='Convert email files to markdown')
    parser.add_argument('email_files', nargs='+', help='Email files to convert')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--combine', action='store_true', help='Combine all emails into one markdown file')
    
    args = parser.parse_args()
    
    if args.combine:
        # Combine all emails into one markdown
        combined_md = "# Email Sync Summary\n\n"
        combined_md += f"**Total emails:** {len(args.email_files)}\n\n"
        combined_md += f"**Processed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
        combined_md += "---\n\n"
        
        for email_file in args.email_files:
            if os.path.exists(email_file):
                combined_md += email_to_markdown(email_file)
                combined_md += "\n---\n\n"
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(combined_md)
            print(f"Combined markdown written to {args.output}")
        else:
            print(combined_md)
    else:
        # Process each email separately
        for email_file in args.email_files:
            if os.path.exists(email_file):
                markdown = email_to_markdown(email_file)
                
                if args.output:
                    base_name = os.path.splitext(os.path.basename(email_file))[0]
                    output_file = f"{base_name}.md"
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(markdown)
                    print(f"Markdown written to {output_file}")
                else:
                    print(markdown)
            else:
                print(f"Error: File {email_file} not found", file=sys.stderr)


if __name__ == "__main__":
    main() 