import os
import re
import json

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(BASE_DIR, 'pages')

SUBJECTS = [
    {
        'file': 'qualidade-software.html',
        'folder': 'qualidade',
        'course_tag': 'TADS',
        'subject_name': 'Qualidade de Software',
        'prefix': 'Aula',
        'json_source': 'pages/qualidade/aulas.json'
    },
    {
        'file': 'introducao-logica.html',
        'folder': 'logica',
        'course_tag': 'Redes de Computadores',
        'subject_name': 'Introdução à Lógica',
        'prefix': 'Aula',
        'json_source': 'pages/logica/aulas.json'
    },
    {
        'file': 'tcc.html',
        'folder': 'tcc',
        'course_tag': 'Ciência da Computação',
        'subject_name': 'Trabalho de Conclusão',
        'prefix': 'Semana'
    }
]

SLIDE_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{lesson_title} - {subject_name}</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/slides.css">
</head>
<body class="slide-body">

    <div class="slide-container">

        <!-- Back Button -->
        <a href="../{parent_file}" class="btn btn-outline-secondary position-absolute top-0 start-0 m-4 rounded-pill">
            <i class="fas fa-arrow-left me-2"></i> Voltar
        </a>

        <!-- Slide 1: Cover -->
        <div class="slide active" id="slide-1">
            <div class="glass-cover text-center">
                <img src="https://res.cloudinary.com/dyhjjms8y/image/upload/v1759512534/logo-SENAC_k3d68v.png"
                     alt="Senac Logo" height="80" class="mb-4">
                <h5 class="text-uppercase text-secondary tracking-wider mb-2 fw-bold">{subject_name}</h5>
                <h1 class="display-3 fw-bold mb-4 text-black">{lesson_title}</h1>
                <hr class="border-secondary w-25 mx-auto my-4 opacity-100">
                <h3 class="fw-normal text-dark">Professor Afonso</h3>
                <span class="badge bg-danger mt-3 px-3 py-2 rounded-pill">2026.1</span>
            </div>
        </div>

        <!-- Slide 2: Agenda -->
        <div class="slide" id="slide-2">
            <h1 class="display-4 fw-bold mb-4 text-dark">Agenda</h1>
            <ul class="list-group list-group-flush fs-4 text-start bg-transparent">
                {agenda_html}
            </ul>
        </div>

        <!-- Slide 3: Content 1 -->
        <div class="slide" id="slide-3">
            <div class="text-center slide-content">
                <h2 class="display-5 fw-bold mb-4 text-dark">Conceitos Iniciais</h2>
                <p class="lead text-dark mb-5">Uma visão geral sobre {lesson_desc}.</p>
                <div class="row g-4">
                    <div class="col-md-4">
                        <div class="p-4 border border-dark-subtle rounded-4 bg-white shadow-sm">
                            <i class="fas fa-lightbulb fa-3x text-warning mb-3"></i>
                            <h4 class="text-dark">Ideia</h4>
                            <p class="text-secondary small">O conceito central explicado de forma simples.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-4 border border-dark-subtle rounded-4 bg-white shadow-sm">
                            <i class="fas fa-cogs fa-3x text-info mb-3"></i>
                            <h4 class="text-dark">Mecanismo</h4>
                            <p class="text-secondary small">Como funciona na prática e seus componentes.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-4 border border-dark-subtle rounded-4 bg-white shadow-sm">
                            <i class="fas fa-chart-line fa-3x text-success mb-3"></i>
                            <h4 class="text-dark">Resultado</h4>
                            <p class="text-secondary small">Os benefícios e impactos esperados.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 4: Content 2 -->
        <div class="slide" id="slide-4">
             <div class="text-center slide-content">
                <h2 class="display-5 fw-bold mb-4 text-dark">Aprofundamento</h2>
                <p class="fs-4 text-secondary">Detalhes técnicos importantes sobre o tema.</p>
                <div class="card border-0 shadow-lg mt-5 mx-auto" style="max-width: 800px;">
                    <div class="card-body p-5">
                         <blockquote class="blockquote mb-0">
                          <p class="text-dark">"A educação é a arma mais poderosa que você pode usar para mudar o mundo."</p>
                          <footer class="blockquote-footer mt-2">Nelson Mandela</footer>
                        </blockquote>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 5: Conclusion -->
        <div class="slide" id="slide-5">
             <div class="text-center slide-content">
                <h1 class="display-3 fw-bold mb-4 text-dark">Dúvidas?</h1>
                <p class="lead text-dark mb-5">Obrigado pela atenção!</p>
                <div class="d-flex justify-content-center gap-3">
                    <a href="#" class="btn btn-dark btn-lg rounded-pill px-5">Material Complementar</a>
                    <a href="../{parent_file}" class="btn btn-outline-dark btn-lg rounded-pill px-5">Voltar para Aulas</a>
                </div>
            </div>
        </div>

    </div>

    <!-- Footer Navigation -->
    <footer class="slide-footer">
        <div class="slide-controls">
            <button id="prevBtn" onclick="prevSlide()" disabled><i class="fas fa-chevron-left"></i></button>
            <button id="nextBtn" onclick="nextSlide()" class="ms-2"><i class="fas fa-chevron-right"></i></button>
        </div>

        <div class="text-center text-muted small d-none d-md-block">
            {subject_name} - {lesson_title}
        </div>

        <a href="../../index.html">
            <img src="https://res.cloudinary.com/dyhjjms8y/image/upload/v1759512534/logo-SENAC_k3d68v.png"
                 alt="Senac" height="30" class="opacity-75">
        </a>
    </footer>

    <script>
        let currentSlide = 1;
        const totalSlides = 5;

        function showSlide(n) {{
            // Remove active class from all slides
            document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));

            // Show current slide
            document.getElementById('slide-' + n).classList.add('active');

            // Update button states
            document.getElementById('prevBtn').disabled = (n === 1);
            document.getElementById('nextBtn').disabled = (n === totalSlides);
        }}

        function nextSlide() {{
            if (currentSlide < totalSlides) {{
                currentSlide++;
                showSlide(currentSlide);
            }}
        }}

        function prevSlide() {{
            if (currentSlide > 1) {{
                currentSlide--;
                showSlide(currentSlide);
            }}
        }}

        // Keyboard Navigation
        document.addEventListener('keydown', function(event) {{
            if (event.key === "ArrowRight") nextSlide();
            if (event.key === "ArrowLeft") prevSlide();
        }});
    </script>

</body>
</html>
"""

def get_lesson_number(title):
    # Extracts number from "Aula 05" -> 5
    match = re.search(r'\d+', title)
    if match:
        return int(match.group(0))
    return None

def process_subject(subject_info):
    file_path = os.path.join(PAGES_DIR, subject_info['file'])
    folder_path = os.path.join(PAGES_DIR, subject_info['folder'])

    if not os.path.exists(file_path):
        print(f"Skipping {subject_info['file']} (Not found)")
        return

    print(f"Processing {subject_info['subject_name']}...")

    # Load JSON data if available
    json_lessons = {}
    if 'json_source' in subject_info:
        json_path = os.path.join(BASE_DIR, subject_info['json_source'])
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
                # Map by number for easy lookup
                for item in data:
                    json_lessons[item['numero']] = item
            print(f"  Loaded JSON data from {subject_info['json_source']}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find lesson blocks
    # Pattern to match the new structure:
    # <a href="LOGICA/FILENAME.HTML" ...> ... <h5 ...>TITLE</h5> ... <p ...>Aula XX</p>
    pattern = re.compile(
        r'(<a\s+href=")([^"]*)("\s+class="list-group-item.*?<h5.*?>)(.*?)(</h5>.*?<p.*?>)(.*?)(</p>)',
        re.DOTALL
    )

    new_content = content

    for match in pattern.finditer(content):
        # Groups:
        # 2: href (e.g. logica/filename.html)
        # 4: Title (e.g. Introdução...)
        # 6: Description (e.g. Aula 01)

        href = match.group(2)
        lesson_title = match.group(4).strip()
        lesson_desc_field = match.group(6).strip() # "Aula 01"

        # Logic for filename generation matching regenerate_cards.py
        # We RE-GENERATE the filename from the Title to ensure consistency,
        # OR we trust the HREF if regenerate_cards already ran.
        # Since regenerate_cards ran, header hrefs are correct.
        # But we need to write the file to the location specified by the href.

        # Extract filename from href
        if '/' in href:
            filename = href.split('/')[-1]
        else:
            filename = href

        # Double check filename against title just in case?
        # No, trust the HREF because that's what the link points to.

        full_slide_path = os.path.join(folder_path, filename)

        # Get Lesson Number from "Aula XX"
        lesson_num = get_lesson_number(lesson_desc_field)

        # Dynamic Agenda generation
        agenda_html = ""

        if lesson_num in json_lessons:
             # Use JSON content
             raw_content = json_lessons[lesson_num].get('conteudo', '')
             if isinstance(raw_content, list):
                 topics = raw_content
             else:
                 topics = [t.strip() for t in re.split(r'[.;]', raw_content) if t.strip()]

             for topic in topics:
                 agenda_html += f'<li class="list-group-item bg-transparent text-dark border-bottom border-dark-subtle"><i class="fas fa-check text-success me-3"></i> {topic}</li>\\n'
        else:
            agenda_html = """
                <li class="list-group-item bg-transparent text-dark border-bottom border-dark-subtle"><i class="fas fa-check text-success me-3"></i> Tópico 1</li>
            """

        # Generate HTML content
        # Note: lesson_desc is used in the slide. "Aula 01" is maybe too short for "Uma visão geral sobre {lesson_desc}".
        # But we don't have the old description anymore in the HTML.
        # We can pull description from JSON if we want?
        # JSON has 'conteudo'.
        # For now, let's just use the Title as description or generic.
        # Actually, using "Aula 01" as description in "Uma visão geral sobre Aula 01" is okay.

        slide_html = SLIDE_TEMPLATE.format(
            lesson_title=lesson_title,
            subject_name=subject_info['subject_name'],
            lesson_desc=lesson_desc_field,
            parent_file=subject_info['file'],
            agenda_html=agenda_html
        )

        # Write slide file
        with open(full_slide_path, 'w', encoding='utf-8') as slide_file:
            slide_file.write(slide_html)

        print(f"  Generated {filename}")

    # skipped link update logic because regenerate_cards.py handles it for Logic,
    # and for others we assume links are correct or manual. if we needed we would duplicate the logic.
    print(f"Processed {subject_info['file']}")

def main():
    for subject in SUBJECTS:
        process_subject(subject)
    print("All Done!")

if __name__ == "__main__":
    main()
