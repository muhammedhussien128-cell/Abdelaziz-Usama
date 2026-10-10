import os
import zipfile
import shutil

desktop = r'C:\Users\Enter Computer\Desktop'
downloads = r'C:\Users\Enter Computer\Downloads'
scratch_project = r'C:\Users\Enter Computer\.gemini\antigravity\scratch\abdelaziz-portfolio'

zip_path = os.path.join(desktop, 'abdelaziz_portfolio_project.zip')
rar_path = os.path.join(desktop, 'abdelaziz_portfolio_project.rar')

files_to_include_from_downloads = [
    'portfolio_abdelaziz_premium.html',
    'portfolio_abdelaziz.html',
    'portfolio_abdelaziz_backup.html',
    'Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf',
    'Database.xlsx',
    'Production Order Visual Report.xlsx',
    'MISUO - Abdelaziz Usama Mahmoud.xlsx'
]

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add standalone HTMLs, PDFs, and Excel project files
    for fname in files_to_include_from_downloads:
        fpath = os.path.join(downloads, fname)
        if os.path.exists(fpath):
            zipf.write(fpath, arcname=fname)
            print(f"Added {fname}")

    # Add React Vite project source files (excluding node_modules & dist)
    for root, dirs, files in os.walk(scratch_project):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if 'dist' in dirs:
            dirs.remove('dist')
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, os.path.dirname(scratch_project))
            zipf.write(full_path, arcname=rel_path)
            print(f"Added {rel_path}")

# Make a copy with .rar extension for user preference
shutil.copyfile(zip_path, rar_path)

print(f"Successfully created archives on Desktop:")
print(f"1. {zip_path}")
print(f"2. {rar_path}")
