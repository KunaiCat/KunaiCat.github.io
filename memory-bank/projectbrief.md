# Project Brief: KunaiCat Social Links Hub

## Core Requirements
- Social media links with consistent styling
- Mobile-responsive design
- Preserve existing color scheme and styling
- Keep codebase modular and maintainable
- Use component.variant format for template references (e.g., `{{social-button.twitch}}`)
- Implement component-specific data with default.json fallbacks

## Current Scope
- Social media links hub with styled button components
- Single page implementation
- Manual testing and deployment
- Python-based HTML generation from templates
- Component variant system with dot notation
- Default data with variant overrides

## Future Scope (Not Currently Active)
- Blog functionality
- Gallery pages
- Header/sidebar navigation component
- Additional social links
- Custom static site generator using Python
- CI/CD workflow with GitHub Actions for automatic builds
- Markdown-to-HTML conversion for blog posts

## Out of Scope
- Analytics tracking
- SEO optimization
- Automated testing/deployment (currently)
- Browser compatibility beyond modern browsers
- Complex animations/interactions

## Immediate Focus
1. Enhance templating system with component.variant format
2. Reorganize data structure for component-specific JSON files
3. Implement default.json with variant overrides
4. Create recursive template processing
5. Maintain modular structure for future expansion 