# Active Context: KunaiCat Social Links Hub

## Current Focus
Documenting and testing the enhanced template-based site generation system with component variants, while planning for future blog functionality.

## Active Tasks
1. Documentation
   - Create comprehensive documentation for the component variant system
   - Update README with examples of using component.variant syntax
   - Add system diagrams for how template resolution works
   - Document data structure organization and conventions

2. Testing & Verification
   - Create additional component variants as examples
   - Test edge cases in component resolution
   - Verify browser compatibility
   - Ensure mobile responsiveness is maintained

3. Future Feature Planning
   - Research Markdown processing libraries for blog functionality
   - Design blog post component structure
   - Plan data organization for blog content
   - Sketch navigation component architecture

## Recent Changes
- Implemented component variant system with dot notation (`{{component.variant}}`)
- Created component-specific data directories with default.json files
- Implemented data merging between defaults and variants
- Updated template parser to support recursive component resolution
- Converted social_links.json to individual component JSON files
- Enhanced generator script with better error handling

## Next Steps
1. Create comprehensive documentation
2. Update README with usage examples
3. Add diagrams for template resolution process
4. Test with additional component types
5. Begin planning blog functionality implementation
6. Design navigation component with component variants

## Active Decisions
1. Template Reference Format
   - Use `{{component.variant}}` format for template references
   - Example: `{{social-button.twitch}}` to render a Twitch button
   - Fall back to default.json if no variant specified
   - Combine default and variant data when both exist

2. Data Organization
   - Directory structure mirrors component hierarchy
   - Each component type has its own data directory
   - Component variants stored as separate JSON files
   - Required default.json for each component type

3. Component Structure
   - Templates live in templates/components/ directory
   - Each component has a template file and multiple data files
   - Components use shared CSS variables
   - Components can be nested within other components

4. Development Workflow
   - Edit templates in templates/ directory
   - Create/edit component data in data/components/ directory
   - Run generator to process templates recursively
   - Deploy generated HTML to GitHub Pages

## Project Insights
- Dot notation provides a clean, intuitive component referencing system
- Default.json with variant overrides reduces duplication and ensures consistency
- Component-specific data files make the system more modular and extensible
- Recursive template processing handles nested components elegantly
- The system will scale well for blog functionality and future components
- Clear 1:1 mapping between templates and data improves maintainability 