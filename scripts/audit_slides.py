import os

root_dir = r"\\wsl.localhost\Ubuntu\home\afonsolelis\aulas_senac\pages"

print(f"Auditing {root_dir}...")

missing_standard_js = []
missing_fullscreen = []
missing_progress_bar = []

total_slides = 0

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(subdir, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it is a slide file
            if 'class="slide"' in content:
                total_slides += 1
                
                if "standard_slides.js" not in content:
                    missing_standard_js.append(filepath)
                
                if 'id="fullscreenBtn"' not in content:
                    missing_fullscreen.append(filepath)
                
                if 'id="progressBar"' not in content:
                    missing_progress_bar.append(filepath)

print(f"\n--- Audit Results ---")
print(f"Total Slide Files Found: {total_slides}")

if missing_standard_js:
    print(f"\n[FAIL] Missing standard_slides.js ({len(missing_standard_js)} files):")
    for f in missing_standard_js:
        print(f"  - {f}")
else:
    print("\n[OK] All slides use standard_slides.js")

if missing_fullscreen:
    print(f"\n[FAIL] Missing Fullscreen Button ({len(missing_fullscreen)} files):")
    for f in missing_fullscreen:
        print(f"  - {f}")
else:
    print("\n[OK] All slides have Fullscreen Button")

if missing_progress_bar:
    print(f"\n[FAIL] Missing Progress Bar ({len(missing_progress_bar)} files):")
    for f in missing_progress_bar:
        print(f"  - {f}")
else:
    print("\n[OK] All slides have Progress Bar")

if not missing_standard_js and not missing_fullscreen and not missing_progress_bar:
    print("\nSUCCESS: All slides are fully standardized!")
else:
    print("\nWARNING: Some slides are missing standard features.")
