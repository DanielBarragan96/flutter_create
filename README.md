# flutter_create

This batch file creates a new flutter project, afterwards runs a python script to update 
- minSdkVersion to 23 
- targetSdkVersion to 29
- compileSdkVersion to 29

Finally, the batch opens the project with Visual Studio Code

Its important to install [Flutter](https://flutter.dev/docs/get-started/install) and [Visual Studio Code](https://code.visualstudio.com/download)

# installation

First you need to install Python 3.7.1 and create an 
environment variable.

After this, create a misc_dir and if needed change this in the create_flutter_project.bat file. The default misc_dir is set to E:\Projects\Android\misc

Next step is to store **open_vscode.bat** and **update_sdk.py** in the defined misc_dir.

Finally, paste misc_dir create_flutter_project.bat in the folder where you want to create your project.

If create_flutter_project.bat is excecuted, it will open a new terminal and ask you to give a name to the preoject, write the name and press enter.

*It's that simple*
