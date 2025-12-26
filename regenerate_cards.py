import json
import re
import unicodedata

COURSES = [
    {
        'json': 'pages/logica/aulas.json',
        'html': 'pages/introducao-logica.html',
        'folder': 'logica',
        'start_week': 6,
        'inject_nav_cards': True,
        'header_snippet': 'Cronograma de Aulas'
    },
    {
        'json': 'pages/qualidade/aulas.json',
        'html': 'pages/qualidade-software.html',
        'folder': 'qualidade',
        'start_week': 6,
        'inject_nav_cards': True,
        'header_snippet': 'Cronograma de Aulas'
    },
    {
        'json': 'pages/tcc/aulas.json',
        'html': 'pages/tcc.html',
        'folder': 'tcc',
        'start_week': 6,
        'inject_nav_cards': False,
        'header_snippet': 'Cronograma de Entregas'
    }
]

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def generate_cards_for_course(course):
    json_path = course['json']
    html_path = course['html']
    folder = course['folder']
    start_week = course['start_week']
    inject_nav_cards = course.get('inject_nav_cards', True) # Default to True
    header_snippet = course.get('header_snippet', 'Cronograma de Aulas')

    print(f"Processing {html_path}...")

    with open(json_path, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    cards_html = ""
    current_week = start_week

    for lesson in lessons:
        # Check for Carnival Week (Week 8)
        if current_week == 8:
             carnival_card = f"""
            <!-- Semana 08: Carnaval -->
            <div class="col-md-6">
              <div class="list-group-item border border-warning rounded shadow-sm p-3 h-100 d-flex flex-column bg-warning-subtle">
                <div class="d-flex w-100 justify-content-between mb-2">
                  <h5 class="mb-1 fw-bold text-dark">Feriado: Carnaval</h5>
                  <span class="badge bg-warning text-dark border fw-normal"><i class="fas fa-umbrella-beach me-1"></i>
                    Semana 08</span>
                </div>
                 <p class="mb-1 text-muted small">Não haverá aula</p>
              </div>
            </div>
            """
             cards_html += carnival_card.strip() + "\n\n"
             current_week += 1

        num = lesson['numero']
        title = lesson['titulo']

        # Determine icon and badge based on title keywords
        if lesson.get('avaliacao', False) or 'Avaliação' in title or 'Prova' in title or 'Entrega' in title or 'Banca' in title:
             if 'Banca' in title or 'Final' in title:
                 badge_class = "bg-success text-white"
                 icon = "fas fa-flag-checkered"
             else:
                 badge_class = "bg-danger text-white"
                 icon = "fas fa-exclamation-circle"
        else:
            badge_class = "bg-light text-dark"
            icon = "far fa-calendar-alt"

        # Calculate Date (approximate based on start week)
        # Week 6 = Feb 1 (Sat)
        # Week 7 = Feb 8, etc.
        # This logic is purely visual "Semana X" for now as per request "troque a data pela semana do ano"
        # User said "igual fizemos nas outras aulas", which used "Semana 06", "Semana 07" badges.

        week_text = f"Semana {current_week:02d}"

        # Clean title for filename (Strict accent removal)
        state_title = remove_accents(title.lower()).replace(' ', '').replace(':', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '')
        filename = f"{folder}/{state_title}.html"

        card = f"""
            <!-- Aula {num:02d} -->
            <div class="col-md-6">
              <a href="{filename}"
                class="list-group-item list-group-item-action border border-light rounded shadow-sm p-3 h-100 d-flex flex-column bg-white">
                <div class="d-flex w-100 justify-content-between mb-2">
                  <h5 class="mb-1 fw-bold text-dark">{title}</h5>
                  <span class="badge {badge_class} border fw-normal"><i class="{icon} me-1"></i>
                    {week_text}</span>
                </div>
                 <p class="mb-1 text-muted small">Aula {num:02d}</p>
              </a>
            </div>
            """
        cards_html += card.strip() + "\n\n"
        current_week += 1

    with open(html_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Locate 'Cronograma'
    cronograma_idx = -1
    for i, line in enumerate(lines):
        if header_snippet in line:
            cronograma_idx = i
            break

    if cronograma_idx == -1:
        print(f"Could not find '{header_snippet}' header in {html_path}")
        return

    # Check/Inject Nav Cards
    has_nav_cards = False
    # Only check/inject if configured
    if inject_nav_cards:
        for i, line in enumerate(lines):
            if "Entrega de Atividades" in line:
                has_nav_cards = True
                break

        # Prepare Nav Cards HTML (Standard)
        nav_cards_html = f"""
              <!-- Project and Activity Cards -->
              <div class="row g-3 mb-4">
                <div class="col-md-4">
                  <a href="{folder}/projeto_descricao.html"
                    class="card h-100 border-0 shadow-sm text-decoration-none bg-primary text-white hover-scale">
                    <div class="card-body text-center d-flex flex-column justify-content-center align-items-center p-4">
                      <i class="fas fa-project-diagram fa-3x mb-3"></i>
                      <h5 class="card-title fw-bold">Descrição do Projeto</h5>
                      <p class="card-text small text-white-50">Detalhes e requisitos do projeto semestral.</p>
                    </div>
                  </a>
                </div>
                <div class="col-md-4">
                  <a href="https://forms.google.com/PLACEHOLDER" target="_blank"
                    class="card h-100 border-0 shadow-sm text-decoration-none bg-success text-white hover-scale">
                    <div class="card-body text-center d-flex flex-column justify-content-center align-items-center p-4">
                      <i class="fas fa-upload fa-3x mb-3"></i>
                      <h5 class="card-title fw-bold">Entrega do Projeto</h5>
                      <p class="card-text small text-white-50">Envie aqui o link do seu projeto final.</p>
                    </div>
                  </a>
                </div>
                <div class="col-md-4">
                  <a href="https://forms.google.com/PLACEHOLDER" target="_blank"
                    class="card h-100 border-0 shadow-sm text-decoration-none bg-info text-white hover-scale">
                    <div class="card-body text-center d-flex flex-column justify-content-center align-items-center p-4">
                      <i class="fas fa-tasks fa-3x mb-3"></i>
                      <h5 class="card-title fw-bold">Entrega de Atividades</h5>
                      <p class="card-text small text-white-50">Envio de exercícios semanais.</p>
                    </div>
                  </a>
                </div>
              </div>
        """

        if not has_nav_cards:
            lines.insert(cronograma_idx + 1, nav_cards_html)
            print("  Inserted Navigation Cards.")
        # Re-evaluate has_nav_cards for lesson replacement logic?
        # Lesson replacement logic needs to find the "row g-3" that follows the nav cards.
        # Now that we inserted them, the file structure in memory 'lines' has them.

    # Now Find Lesson Row (The next <div class="row g-3"> after nav cards)
    # Nav cards block has <div class="row g-3 mb-4">.
    # Lesson row has <div class="row g-3">.

    start_lesson_row = -1

    # Searching in 'lines' (which might have been modified)
    # We look for <div class="row g-3">.
    # Note: nav cards used "row g-3 mb-4". Lesson used "row g-3". Note the exact match difference or position.

    found_nav = False

    for i in range(cronograma_idx, len(lines)):
        line = lines[i]
        if 'class="row g-3 mb-4"' in line:
            found_nav = True
        elif 'class="row g-3"' in line and 'mb-4' not in line:
            # Found lesson row start
            start_lesson_row = i
            break

    if start_lesson_row == -1:
        print("Could not find lesson row start.")
        # If we didn't find it, maybe the file only has the list?
        return

    # Find end of lesson row
    count = 0
    end_lesson_row = -1
    for i in range(start_lesson_row, len(lines)):
        line = lines[i]
        count += line.count('<div')
        count -= line.count('</div')
        if count == 0:
            end_lesson_row = i
            break

    if end_lesson_row == -1:
        print("Could not find lesson row end.")
        return

    # Replace content
    # Same logic: lines[:start_lesson_row+1] + cards + lines[end_lesson_row:]

    final_content = "".join(lines[:start_lesson_row+1]) + "\n" + cards_html + "\n" + "".join(lines[end_lesson_row:])

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"  Regenerated {html_path}")


def main():
    for course in COURSES:
        generate_cards_for_course(course)

if __name__ == "__main__":
    main()
