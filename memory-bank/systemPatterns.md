# System Patterns: KunaiCat Social Links Hub

## Architecture Overview
- Static site hosted on GitHub Pages
- Pure HTML/CSS implementation
- Python-based template generation
- No JavaScript frameworks or dependencies
- Component-based modular structure

## Component Architecture
### Current Structure
```
KunaiCat.github.io/
├── index.html
├── styles/
│   ├── main.css
│   ├── variables.css
│   ├── components/
│   │   ├── grid.css
│   │   └── social-button.css
│   └── utils/
├── components/
│   └── social-button.html
├── images/
│   └── kiriFavicon.ico
└── CNAME
```

### Planned Template Generation Structure
```
KunaiCat.github.io/
├── index.html (generated)
├── templates/
│   ├── index.html.template
│   └── components/
│       └── social-button.html.template
├── scripts/
│   └── generate_site.py
├── data/
│   └── social_links.json
├── styles/
│   ├── main.css
│   ├── variables.css
│   ├── components/
│   │   ├── grid.css
│   │   └── social-button.css
│   └── utils/
├── components/ (for reference)
│   └── social-button.html
├── images/
│   └── kiriFavicon.ico
└── CNAME
```

## Design Patterns
1. CSS Variables
   - Global theme configuration in variables.css
   - Color scheme
   - Spacing and layout
   - Transitions
   - Responsive breakpoints

2. Grid System
   - 2-column desktop layout
   - Single column mobile layout
   - Responsive breakpoint at 600px
   - CSS Grid implementation

3. Component Patterns
   - Template-based components
   - Consistent button styling
   - Icon + text layout
   - Hover effects
   - Border accents

4. Template System
   - Double curly brackets for placeholders: `{{PLACEHOLDER}}`
   - Python-based template processing
   - JSON data sources
   - Component composition

## Implementation Guidelines
1. CSS Organization
   - CSS variables for theme values
   - Component-specific stylesheets
   - Base styles in main.css
   - Mobile-first media queries

2. HTML Structure
   - Semantic HTML elements
   - Component-based architecture
   - Clear component boundaries
   - Template-driven development

3. Component Design
   - Self-contained styles
   - Reusable templates
   - Minimal dependencies
   - SVG icon integration

4. Template Usage
   - Use `{{PLACEHOLDER}}` format for all template variables
   - Keep templates as close as possible to final HTML
   - Document all placeholder variables
   - Design for reusability

## File Responsibilities
1. variables.css
   - Global theme configuration
   - Spacing constants
   - Breakpoints
   - Animation timings

2. main.css
   - CSS imports
   - Base reset
   - Typography
   - Layout fundamentals

3. Component Files
   - grid.css: Layout system
   - social-button.css: Button styling
   - social-button.html.template: Component template

4. Python Scripts
   - generate_site.py: Main site generation script
   - Template processing
   - Data loading and injection
   - File output management 