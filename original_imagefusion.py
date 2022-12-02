
from google.colab import drive
drive.mount('/content/drive/')

!ls "/content/drive/MyDrive/"

import os
# Set your working directory to a folder in your Google Drive. This way, if your notebook times out,
# your files will be saved in your Google Drive!
# the base Google Drive directory
root_dir = "/content/drive/MyDrive/"
# # choose where you want your project files to be saved
# project_folder = "Colab Notebooks/My Project Folder/"
# def create_and_set_working_directory(project_folder):
 # # # #
# check if your project folder exists. if not, it will be created.
#if os.path.isdir(root_dir + project_folder) == False:
 # os.mkdir(root_dir + project_folder)
  #print(root_dir + project_folder + ' did not exist but was created.')
  # change the OS to use your project folder as the working directory
os.chdir("/content/drive/MyDrive/Dissertation/ORG_Imagefusion")
# ----------------------------------------------------------------------------
  # create a test file to make sure it shows up in the right place
# !touch 'new_file_in_working_directory.txt'
# print('\nYour working directory was changed to ' + root_dir + 'PROF_CODE' + \
        # "\n\nAn empty text file was created there. You can also run !pwd to confirm the current working directory." )
# ------------------------------------------------------------------------------
# create_and_set_working_directory(project_folder)

!ls "/content/drive/MyDrive/Dissertation/ORG_Imagefusion"

!pip3 install visdom

!pip3 install einops

#pip install matplotlib

!pip3 install rasterio

!pip3 install fiona


!pip3 install pyproj  


!pip3 install shapely
!pip3 install kornia

!pip3 install  rtree

# Commented out IPython magic to ensure Python compatibility.
# %run train.py

# Commented out IPython magic to ensure Python compatibility.
# %run predict.py
