#!/usr/bin/env python3
"""
KunaiCat Website Generator

This script generates the KunaiCat website using templates and component variants.
It supports dot notation for component references (e.g., {{component.variant}})
and provides default data fallback.
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
DATA_DIR = "data/components"
COMPONENT_TEMPLATE_DIR = os.path.join(TEMPLATE_DIR, "components")
OUTPUT_DIR = "."  # Root directory for output

# Output file paths
INDEX_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "index.html")

# Regular expression for finding component references
COMPONENT_PATTERN = r"\{\{([\w-]+)(?:\.([\w-]+))?\}\}"


def load_template(template_name):
    """Load a template file and return its contents.
    
    Args:
        template_name (str): Name of the template without extension
                             (e.g., 'social-button' or 'index')
    
    Returns:
        str: Template contents or None if not found
    """
    # Determine if this is a component or a regular template
    if template_name == "index":
        template_path = os.path.join(TEMPLATE_DIR, f"{template_name}.html.template")
    else:
        template_path = os.path.join(COMPONENT_TEMPLATE_DIR, f"{template_name}.html.template")
    
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Template file not found: {template_path}")
        return None
    except Exception as e:
        print(f"Error loading template {template_path}: {e}")
        return None


def load_component_data(component, variant=None):
    """Load component data with fallback to default.
    
    Args:
        component (str): Component name (e.g., 'social-button')
        variant (str, optional): Variant name (e.g., 'twitch')
    
    Returns:
        dict: Merged data from default and variant
    """
    # Always load default data first
    component_dir = os.path.join(DATA_DIR, component)
    default_path = os.path.join(component_dir, "default.json")
    
    try:
        with open(default_path, 'r', encoding='utf-8') as file:
            default_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: Default data file not found: {default_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file: {default_path}")
        return {}
    except Exception as e:
        print(f"Error loading default data {default_path}: {e}")
        return {}
    
    # If no variant is specified, return default data
    if not variant:
        return default_data
    
    # Load variant-specific data and merge with default
    variant_path = os.path.join(component_dir, f"{variant}.json")
    
    try:
        with open(variant_path, 'r', encoding='utf-8') as file:
            variant_data = json.load(file)
            # Merge with default, letting variant override default values
            return {**default_data, **variant_data}
    except FileNotFoundError:
        print(f"Warning: Variant data file not found: {variant_path}")
        print(f"Using default data for {component}")
        return default_data
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file: {variant_path}")
        return default_data
    except Exception as e:
        print(f"Error loading variant data {variant_path}: {e}")
        return default_data


def render_component(component, variant=None):
    """Render a component with its data.
    
    Args:
        component (str): Component name
        variant (str, optional): Variant name
    
    Returns:
        str: Rendered HTML for the component
    """
    print(f"Rendering component: {component}" + (f".{variant}" if variant else ""))
    
    # Load the component template
    template = load_template(component)
    if not template:
        return f"<!-- Error: Could not load template for {component} -->"
    
    # Load component data (with variant if specified)
    data = load_component_data(component, variant)
    if not data:
        return f"<!-- Error: Could not load data for {component}.{variant or 'default'} -->"
    
    # Process the template recursively to handle nested components
    return process_template(template, data)


def process_template(template_content, data=None):
    """Process a template, replacing placeholders with values and resolving nested components.
    
    Args:
        template_content (str): Template content
        data (dict, optional): Data for simple variable replacement
    
    Returns:
        str: Processed template with all placeholders replaced
    """
    # First replace any simple placeholders if data is provided
    if data:
        for key, value in data.items():
            placeholder = f"{{{{{key}}}}}"
            template_content = template_content.replace(placeholder, str(value))
    
    # Find and replace all component references
    def replace_component(match):
        component = match.group(1)
        variant = match.group(2)  # Will be None if no variant specified
        
        # Render the referenced component
        return render_component(component, variant)
    
    # Apply component replacement until no more matches are found
    prev_content = ""
    current_content = template_content
    
    while prev_content != current_content:
        prev_content = current_content
        current_content = re.sub(COMPONENT_PATTERN, replace_component, prev_content)
    
    return current_content


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
    
    # Load and process the index template
    print("Processing index template...")
    index_template = load_template("index")
    
    if not index_template:
        print("Failed to load index template. Exiting.")
        return False
    
    # Process the template (this will recursively handle all component references)
    print("Resolving component references...")
    processed_html = process_template(index_template)
    
    # Save the generated HTML
    print("Saving generated files...")
    success = save_html(processed_html, INDEX_OUTPUT_PATH)
    
    print("-------------------------")
    if success:
        print("Website generation complete!")
        return True
    else:
        print("Website generation failed!")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1) 