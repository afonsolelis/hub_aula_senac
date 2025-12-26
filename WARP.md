# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Hub de Aulas Senac is a static website for organizing and presenting educational content for SENAC courses. It features:
- A central hub (`index.html`) linking to three subjects
- Subject pages displaying lesson schedules
- Auto-generated slide presentations for each lesson
- Pure HTML/CSS frontend with Bootstrap 5 and Font Awesome

## Architecture

### Core Components

**Content Generation System** (`generate_slides.py`)
- Python script that automatically generates HTML slide files for lessons
- Reads subject configuration from `SUBJECTS` array (lines 8-30)
- Parses subject pages to extract lesson titles and descriptions using regex
- Generates slides from template (`SLIDE_TEMPLATE`, lines 32-196) 
- Updates lesson links in subject pages to point to generated slides
- Each generated slide has 5 sections: cover, agenda, concepts, details, conclusion

**Subject Structure**
- Three subjects configured: Qualidade de Software (TADS), Introdução à Lógica (Redes), TCC (Ciência da Computação)
- Each subject has:
  - Main page: `pages/{subject-name}.html`
  - Subfolder: `pages/{folder}/` containing generated lesson slides
  - Naming: lessons use prefix "Aula" or "Semana" + number → filename (e.g., "Aula 01" → `aula01.html`)

**Content Flow**
1. Subject pages list lessons with titles and descriptions
2. `generate_slides.py` extracts this information via regex
3. Script generates individual slide HTML files in subject subfolders
4. Script updates href links in subject pages to point to generated slides
5. Slides link back to their parent subject page

### File Structure
```
hub_aula_senac/
├── index.html                    # Main hub page
├── generate_slides.py            # Slide generator script
├── sources.json                  # Cloudinary image URLs
├── css/
│   ├── style.css                 # Main styles (cards, gradients, navbar)
│   └── slides.css                # Slide presentation styles
└── pages/
    ├── professor.html            # Professor profile page
    ├── qualidade-software.html   # Quality assurance subject
    ├── introducao-logica.html    # Logic programming subject
    ├── tcc.html                  # Thesis project subject
    ├── qualidade/                # Generated QA slides (aula01.html - aula16.html)
    ├── logica/                   # Generated logic slides (aula01.html - aula16.html)
    └── tcc/                      # Generated TCC slides (semana01.html - semana16.html)
```

## Common Development Commands

### Generate Slides
Run this after editing lesson titles/descriptions in subject pages:
```bash
python3 generate_slides.py
```

This will:
- Parse all subject HTML files defined in `SUBJECTS`
- Generate/update slide files in respective subfolders
- Update links in subject pages to point to generated slides

### Serve Locally
Since this is a static site, use any HTTP server:
```bash
python3 -m http.server 8000
```
Then open `http://localhost:8000`

### Git Operations
Standard git workflow applies. The repository is tracked with git.

## Key Implementation Details

### Adding New Lessons
To add lessons to an existing subject:
1. Edit the subject's HTML file (e.g., `pages/qualidade-software.html`)
2. Add a new lesson block following the existing pattern:
   ```html
   <div class="col-md-6">
     <a href="#" class="list-group-item...">
       <h5 class="mb-1 fw-bold text-dark">Aula XX</h5>
       <p class="mb-1 text-muted small">Lesson description</p>
     </a>
   </div>
   ```
3. Run `python3 generate_slides.py` to generate the slide and update links

### Adding New Subjects
To add a completely new subject:
1. Add configuration to `SUBJECTS` array in `generate_slides.py`:
   ```python
   {
       'file': 'new-subject.html',
       'folder': 'new-folder',
       'course_tag': 'Course Name',
       'subject_name': 'Subject Display Name',
       'prefix': 'Aula'  # or 'Semana'
   }
   ```
2. Create `pages/new-subject.html` with lesson list structure
3. Create `pages/new-folder/` directory
4. Add subject card to `index.html`
5. Run `generate_slides.py`

### Regex Pattern for Lesson Extraction
The script uses this pattern to find lessons (line 223-226):
```python
r'(<a\s+href=\")([^\"]*)(\"\s+class=\"list-group-item.*?<h5.*?>)(.*?)(</h5>.*?<p.*?>)(.*?)(</p>)'
```
Captures: opening tag → href → middle → title → middle → description → closing

### Styling Notes
- `css/style.css`: Main site styles using glassmorphism effects and gradient backgrounds
- `css/slides.css`: Slide-specific styles with clean white cards on light gray background
- Subject-specific gradients: `.bg-quality`, `.bg-logic`, `.bg-tcc`
- Slides use keyboard navigation (arrow keys) handled by inline JavaScript

### External Resources
- Bootstrap 5.3.0 (CDN)
- Font Awesome 6.0.0 (CDN)
- Images hosted on Cloudinary (URLs in `sources.json`)
- Senac logo: hardcoded Cloudinary URL used throughout
