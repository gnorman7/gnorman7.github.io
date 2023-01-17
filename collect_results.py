import numpy as np
import os
import glob
import shutil
import subprocess

def copy_embed_upload_new_figures():
    # %%

    # Copy figures

    today = np.datetime64('today')
    date_str = str(today)

    analysis_path = r'/Users/grant/Documents/personal_projs/productivity/'
    # analysis_path = r'/mnt/c/Users/grant/Documents/personal_projs/productivity/'
    website_path = r'/Users/grant/Documents/personal_projs/gnorman7.github.io/'
    # website_path = r'./'

    analysis_fig_folder = r'figs_for_export'
    analysis_fig_folder = os.path.join(analysis_path,analysis_fig_folder)

    website_fig_folder = os.path.join(website_path,r'docs/assets/images')
    today = np.datetime64('today')
    date_str = str(today)
    website_fig_folder = os.path.join(website_fig_folder,date_str)

    os.makedirs(website_fig_folder,exist_ok=True)

    filename = '*.svg'
    cp_src = os.path.join(analysis_fig_folder,filename)

    # cp functioanlity with * wildcard
    for file in glob.glob(cp_src):
        shutil.copy(file, website_fig_folder)


    # %%

    # Create md file that points to figures
    website_weekly_updates_folder = os.path.join(website_path,'docs/weekly_updates/_posts')
    md_filename = f'{date_str}-weekly_summary.md'
    md_filename = os.path.join(website_weekly_updates_folder,md_filename)

    update_template_filename = 'update_template.md'
    update_template_filename = os.path.join(website_path,update_template_filename)
    with open(update_template_filename,'r') as file:
        template_str = file.read()

    update_str = template_str.replace('DATE',date_str)

    file = open(md_filename,'w')
    file.write(update_str)
    file.close()


    # %% Update website via git commit, git push\

    subprocess.run(["git","checkout","gh-pages"])

    # Only update what is needed
    git_add_files = [website_fig_folder,md_filename]
    for file in git_add_files:
        subprocess.run(["git","add",file])

    # git commit -m "auto update generate"
    subprocess.run(["git","commit","-m","auto update generate"])

    subprocess.run(["git","push"])

# importing sys
 
# adding Folder_2 to the system path
copy_embed_upload_new_figures()