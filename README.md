# Hey [join the discord](https://discord.gg/Y837qFC2mZ) and DM me about coaching services
Or if you have ideas for this site let me know


# KunaiCat Social Links Hub

A simple, modular website showcasing KunaiCat's social media links, built with HTML, CSS, and Python-based template generation.

## Project Structure

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
├── components/ (reference only)
│   └── social-button.html
├── images/
│   └── kiriFavicon.ico
└── memory-bank/ (documentation)
```

## Features

- Modular component-based architecture
- CSS variables for consistent theming
- Responsive design for mobile and desktop
- Python-based template generation
- JSON data source for social links

## Template System

Templates use double curly braces (`{{PLACEHOLDER}}`) format for dynamic content insertion. For example:

```html
<a href="{{PLATFORM_URL}}" class="link-wrapper">
  <div class="container">
    <h3 class="social-icon">
      {{ICON_SVG}}
      <span>{{PLATFORM_NAME}}</span>
    </h3>
  </div>
</a>
```

## Development

### Local Development Server

To preview the site locally:

```bash
python -m http.server 8000
```

Then visit http://localhost:8000 in your browser.

### Generating the Site

To generate the site from templates:

```bash
python scripts/generate_site.py
```

### Adding a New Social Link

1. Add the new platform to `data/social_links.json`
2. Run the generator script
3. Test the generated site

## Future Plans

- Blog functionality with Markdown processing
- Gallery pages
- Navigation components
- CI/CD workflow with GitHub Actions
