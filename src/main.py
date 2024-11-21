import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    
    os.makedirs(dir_path_public, exist_ok=True)
    
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content) 
    for entry in entries:
        
        entry_path = os.path.join(dir_path_content, entry)
        
        
        if os.path.isfile(entry_path):
            output_path = os.path.join(dest_dir_path, entry.replace('.md', '.html'))
            generate_page(entry_path, template_path, output_path)
        else:
            new_dest_dir = os.path.join(dest_dir_path, entry)
            os.makedirs(new_dest_dir, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, new_dest_dir)

main()
