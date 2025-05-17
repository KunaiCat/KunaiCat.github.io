# Active Context: KunaiCat Social Links Hub

## Current Focus
Enhancing the template-based site generation system with a more modular component approach using dot notation and component variants.

## Active Tasks
1. Enhanced Templating System Implementation
   - Develop component variant system with dot notation (`{{component.variant}}`)
   - Create component-specific data directories with default.json files
   - Implement data merging between defaults and variants
   - Update template parser to support recursive component resolution

2. Data Structure Reorganization
   - Convert single social_links.json to component-specific JSON files
   - Create default.json for each component type
   - Implement variant-specific data files (twitch.json, discord.json, etc.)
   - Establish clear 1:1 mapping between templates and data

3. Generator Refactoring
   - Enhance template parser to identify component.variant syntax
   - Create component resolution logic
   - Implement recursive rendering pipeline
   - Add error handling for missing templates/data

4. Documentation Updates
   - Document new templating system architecture
   - Create examples of component variants
   - Update README with new generator usage
   - Add system diagrams for template resolution

## Recent Changes
- Implemented initial Python-based template generation system
- Created JSON data source for social links
- Developed template engine with placeholder replacement
- Planned enhanced templating system with component variants
- Designed more modular data structure approach

## Next Steps
1. Create new directory structure for component-specific data
2. Update template parser to handle dot notation
3. Implement data merging between default and variant JSONs
4. Convert existing social links to use variant system
5. Test component variant rendering
6. Document the new templating approach

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
   - Run generator to process all templates recursively
   - Deploy generated HTML to GitHub Pages

## Project Insights
- Dot notation provides a clean, intuitive component referencing system
- Default.json with variant overrides reduces duplication and ensures consistency
- Component-specific data files make the system more modular and extensible
- New system will scale better for blog functionality and future components
- Clear 1:1 mapping between templates and data improves maintainability 