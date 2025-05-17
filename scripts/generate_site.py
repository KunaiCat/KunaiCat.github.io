#!/usr/bin/env python3
"""
KunaiCat Website Generator

This script generates the KunaiCat website using templates and JSON data.
"""

import json
import os
import re
import sys

# Get the project root directory (parent of scripts directory)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Change working directory to project root if needed
if os.getcwd() != PROJECT_ROOT:
    os.chdir(PROJECT_ROOT)
    print(f"Changed working directory to: {PROJECT_ROOT}")

# Path constants relative to project root
TEMPLATE_DIR = "templates"
DATA_DIR = "data"
COMPONENT_TEMPLATE_DIR = os.path.join(TEMPLATE_DIR, "components")
OUTPUT_DIR = "."  # Root directory for output

# Template file paths
INDEX_TEMPLATE_PATH = os.path.join(TEMPLATE_DIR, "index.html.template")
SOCIAL_BUTTON_TEMPLATE_PATH = os.path.join(COMPONENT_TEMPLATE_DIR, "social-button.html.template")

# Data file paths
SOCIAL_LINKS_DATA_PATH = os.path.join(DATA_DIR, "social_links.json")

# Output file paths
INDEX_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "index.html")


def load_template(template_path):
    """Load a template file and return its contents."""
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Template file not found: {template_path}")
        return None
    except Exception as e:
        print(f"Error loading template {template_path}: {e}")
        return None


def load_json_data(json_path):
    """Load JSON data from a file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: JSON file not found: {json_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file: {json_path}")
        return None
    except Exception as e:
        print(f"Error loading JSON {json_path}: {e}")
        return None


def replace_placeholders(template, replacements):
    """Replace placeholders in template with values."""
    result = template
    for placeholder, value in replacements.items():
        placeholder_pattern = f"{{{{{placeholder}}}}}"
        result = result.replace(placeholder_pattern, value)
    return result


def generate_social_buttons(social_links_data, button_template):
    """Generate HTML for all social buttons."""
    buttons_html = []
    
    for link in social_links_data.get("social_links", []):
        replacements = {
            "PLATFORM_URL": link.get("url", ""),
            "PLATFORM_NAME": link.get("platform", ""),
            "ICON_SVG": link.get("icon", "")
        }
        button_html = replace_placeholders(button_template, replacements)
        buttons_html.append(button_html)
    
    return "\n    ".join(buttons_html)


def generate_index_html(index_template, social_buttons_html):
    """Generate the index.html file."""
    replacements = {
        "SOCIAL_BUTTONS": social_buttons_html
    }
    return replace_placeholders(index_template, replacements)


def save_html(html_content, output_path):
    """Save HTML content to a file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"Successfully generated: {output_path}")
        return True
    except Exception as e:
        print(f"Error saving HTML to {output_path}: {e}")
        return False


def main():
    """Main function to generate the website."""
    print("KunaiCat Website Generator")
    print("-------------------------")
    print(f"Working Directory: {os.getcwd()}")
    
    # Load templates
    print("Loading templates...")
    index_template = load_template(INDEX_TEMPLATE_PATH)
    button_template = load_template(SOCIAL_BUTTON_TEMPLATE_PATH)
    
    if not index_template or not button_template:
        print("Failed to load required templates. Exiting.")
        return False
    
    # Load data
    print("Loading data...")
    social_links_data = load_json_data(SOCIAL_LINKS_DATA_PATH)
    
    if not social_links_data:
        print("Failed to load required data. Exiting.")
        return False
    
    # Generate components
    print("Generating social buttons...")
    social_buttons_html = generate_social_buttons(social_links_data, button_template)
    
    # Generate pages
    print("Generating index.html...")
    index_html = generate_index_html(index_template, social_buttons_html)
    
    # Save output
    print("Saving generated files...")
    save_html(index_html, INDEX_OUTPUT_PATH)
    
    print("-------------------------")
    print("Website generation complete!")
    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1) 