# System Patterns: KunaiCat Social Links Hub

## Architecture Overview
- Static site hosted on GitHub Pages
- Pure HTML/CSS implementation
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
   - social-button.html: Component template

4. Utils Directory
   - Reserved for future utility classes
   - Will contain shared styles
   - Helper functions
   - Responsive utilities 