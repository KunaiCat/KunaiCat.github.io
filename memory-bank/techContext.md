# Technical Context: KunaiCat Social Links Hub

## Technology Stack
- HTML5
- CSS3
  - CSS Variables
  - CSS Grid
  - CSS Imports
- Python 3
  - Template processing
  - JSON data handling
  - Recursive component resolution
- GitHub Pages (hosting)

## Development Environment
- Local development server: Python HTTP server (port 8000)
- Preview URL: http://localhost:8000
- Python script for HTML generation
- Manual deployment through GitHub Pages

## Browser Support
- Focus on modern browsers (Chrome, Firefox)
- No specific compatibility requirements
- No polyfills needed

## Dependencies
- Python 3.6+
- No external JavaScript libraries
- No CSS frameworks
- SVG icons (embedded)

## Development Tools
### Local Server
Start local preview:
```bash
python3 -m http.server 8000
```

### Site Generation
Generate site from templates:
```bash
python3 scripts/generate_site.py
```

### GitHub Pages Setup
- Repository name: KunaiCat.github.io
- Branch: main
- Custom domain: Configured via CNAME file

## File Structure
```
KunaiCat.github.io/
├── .github/
├── components/ (reference only)
│   └── social-button.html
├── templates/
│   ├── index.html.template
│   └── components/
│       └── social-button.html.template
├── scripts/
│   └── generate_site.py
├── data/
│   └── components/
│       └── social-button/
│           ├── default.json
│           ├── twitch.json
│           ├── discord.json
│           └── ...
├── styles/
│   ├── main.css
│   ├── variables.css
│   ├── components/
│   │   ├── grid.css
│   │   └── social-button.css
│   └── utils/
├── images/
│   └── kiriFavicon.ico
├── CNAME
├── index.html (generated)
└── README.md
```

## CSS Architecture
- CSS Variables for theming
- Mobile-first responsive design
- Component-based CSS organization
- Modular imports system

## Component Architecture
- Template-based components with `{{component.variant}}` syntax
- Reusable component patterns with variants
- Consistent styling through CSS variables
- Component-specific data files

## Python Template Processing
- Dot notation for component references
- Recursive template resolution
- Data merging between default and variant JSON files
- Fallback to default data when variant is missing properties
- Component composition through template references
- Error handling and validation
- Clean output formatting

## Performance Considerations
- No specific performance requirements
- Static content only
- Minimal asset size
- CSS imports for code organization
- No build process needed

## Development Workflow
1. Template Development
   - Update templates in templates/components/ directory
   - Use `{{component.variant}}` syntax for component references
   - Create component variants with shared structure
   - Maintain HTML validity

2. Data Management
   - Create component-specific data directories
   - Define default.json for each component type
   - Create variant-specific JSON files as needed
   - Structure data for consistency across variants

3. Site Generation
   - Run Python script to process templates recursively
   - Merge default and variant data automatically
   - Generate complete HTML output
   - Deploy to GitHub Pages

4. Testing Process
   - Local server preview
   - Verify all component variants render correctly
   - Mobile responsive testing
   - Cross-browser verification 