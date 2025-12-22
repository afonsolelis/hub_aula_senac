import os
import re

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(BASE_DIR, 'pages')

SUBJECTS = [
    {
        'file': 'qualidade-software.html',
        'folder': 'qualidade',
        'course_tag': 'TADS',
        'subject_name': 'Qualidade de Software',
        'prefix': 'Aula'
    },
    {
        'file': 'introducao-logica.html',
        'folder': 'logica',
        'course_tag': 'Redes de Computadores',
        'subject_name': 'Introdução à Lógica',
        'prefix': 'Aula'
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
                <li class="list-group-item bg-transparent text-dark border-bottom border-dark-subtle"><i class="fas fa-check text-success me-3"></i> Tópico 1: Introdução</li>
                <li class="list-group-item bg-transparent text-dark border-bottom border-dark-subtle"><i class="fas fa-check text-success me-3"></i> Tópico 2: Conceitos Fundamentais</li>
                <li class="list-group-item bg-transparent text-dark border-bottom border-dark-subtle"><i class="fas fa-check text-success me-3"></i> Tópico 3: Aplicação Prática</li>
                <li class="list-group-item bg-transparent text-dark border-0"><i class="fas fa-check text-success me-3"></i> Tópico 4: Conclusão</li>
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

def process_subject(subject_info):
    file_path = os.path.join(PAGES_DIR, subject_info['file'])
    folder_path = os.path.join(PAGES_DIR, subject_info['folder'])

    if not os.path.exists(file_path):
        print(f"Skipping {subject_info['file']} (Not found)")
        return

    print(f"Processing {subject_info['subject_name']}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find lesson blocks
    # Looking for: <a href="..." ...> ... <h5 ...>Aula XX</h5> ... <p ...>Desc</p> ... </a>
    # We capture the whole A tag to replace the href

    # We need a robust regex to iterate over matches and update them.
    # Pattern explanation:
    # <a href="(.*?)" (capture href)
    # (.*?) (content before h5)
    # <h5.*?>(.*?)</h5> (capture title, e.g., Aula 01)
    # (.*?) (content before p)
    # <p.*?>(.*?)</p> (capture desc)

    pattern = re.compile(
        r'(<a\s+href=")([^"]*)("\s+class="list-group-item.*?<h5.*?>)(.*?)(</h5>.*?<p.*?>)(.*?)(</p>)',
        re.DOTALL
    )

    new_content = content
    offset = 0

    for match in pattern.finditer(content):
        # Groups:
        # 1: <a href="
        # 2: current_href (e.g. # or old link)
        # 3: " class=... ... <h5 ...>
        # 4: Lesson Title (e.g. Aula 01)
        # 5: </h5> ... <p ...>
        # 6: Description
        # 7: </p>

        old_href = match.group(2)
        lesson_title = match.group(4).strip()
        lesson_desc = match.group(6).strip()

        # Clean title for filename (Aula 01 -> aula01, Semana 01 -> semana01)
        # Remove accents/special chars just in case, though basic alphanumeric is expected
        clean_title = lesson_title.lower().replace(' ', '').replace('ã', 'a').replace('ç', 'c')

        filename = f"{clean_title}.html"
        full_slide_path = os.path.join(folder_path, filename)

        # Generate HTML content
        slide_html = SLIDE_TEMPLATE.format(
            lesson_title=lesson_title,
            subject_name=subject_info['subject_name'],
            lesson_desc=lesson_desc,
            parent_file=subject_info['file']
        )

        # Write slide file
        with open(full_slide_path, 'w', encoding='utf-8') as slide_file:
            slide_file.write(slide_html)

        print(f"  Generated {filename}")

        # Update Main File Link
        # structure is relative: folder/filename
        new_href = f"{subject_info['folder']}/{filename}"

        # Replace only this specific occurrence in the string
        # We replace the href part.
        # Since finditer gives us positions in the original string, we can construct the new string
        # But replacing repeatedly changes indices.
        # easier: using re.sub with a callback function

    def replacer(m):
        # m.group(4) is title
        title = m.group(4).strip()
        clean_title = title.lower().replace(' ', '').replace('ã', 'a').replace('ç', 'c')
        filename = f"{clean_title}.html"
        new_link = f"{subject_info['folder']}/{filename}"

        # Return reconstructed string with new link
        return f'{m.group(1)}{new_link}{m.group(3)}{m.group(4)}{m.group(5)}{m.group(6)}{m.group(7)}'

    new_content = pattern.sub(replacer, content)

    # Save updated subject page
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Updated links in {subject_info['file']}")

def main():
    for subject in SUBJECTS:
        process_subject(subject)
    print("All Done!")

if __name__ == "__main__":
    main()
