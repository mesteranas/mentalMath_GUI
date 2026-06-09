import shutil
import os
import subprocess
import UniversalSpeech
pyqt_path = os.path.dirname(UniversalSpeech.__file__)

if os.path.exists("mentalMath_build"):
    print("removing mentalMath_build")
    shutil.rmtree("mentalMath_build")
# Create a version resource file for Windows executables.
version_info = r'''
# UTF-8
#
# For more details about fixed file info 'ffi' see:
# https://docs.microsoft.com/en-us/windows/win32/menurc/vs-versioninfo
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x4,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          '040904B0',
          [
            StringStruct('CompanyName', 'mister anas '),
            StringStruct('FileDescription', 'Mental Math GUI aims to make mental arithmetic training accessible, enjoyable, and efficient for blind and visually impaired users around the world.'),
            StringStruct('FileVersion', '1.0.0.0'),
            StringStruct('InternalName', 'mental math'),
            StringStruct('OriginalFilename', 'mentalMath.exe'),
            StringStruct('ProductName', 'mental math'),
            StringStruct('ProductVersion', '1.0.0.0'),
            StringStruct('LegalCopyright', '© 2026 ; Mister Anas')
          ]
        )
      ]
    ),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
'''

# Write version info to a file.
version_file_path = "version_file.txt"
with open(version_file_path, "w", encoding="utf-8") as vf:
    vf.write(version_info.strip())

include_files = [
    ("data/sounds", "data/sounds"),
    ("data/help", "data/help")
]

# Dynamically add language resource files from the "data/languages" folder.
for languageFolder in os.listdir("data/languages"):
    languagesFolder = os.path.join("data", "languages", languageFolder)
    if os.path.isdir(languagesFolder):
        langNameFile = os.path.join(languagesFolder, "langName.translation")
        langContent = os.path.join(languagesFolder, "LC_MESSAGES", "mentalMath_GUI.mo")
        include_files.append((langNameFile, langNameFile))
        include_files.append((langContent, langContent))
dll_files =os.listdir(os.path.join(pyqt_path,"lib64"))
for file in dll_files:
    include_files.append((os.path.join(pyqt_path, "lib64", file), os.path.join("_internal", "UniversalSpeech","lib64",file)))


print("Converting to exe, please wait...")

# Run PyInstaller with windowed mode, and version file options.
command = [
    "pyinstaller",
    "-w",
    f"--version-file={version_file_path}",
    "mentalMath.py"
]

run = subprocess.run(command)

if run.returncode == 0:
    print("PyInstaller build successful.")
    # Assuming that the built executable is in the folder "dist/mentalMath"
    target_dir = os.path.join("dist", "mentalMath")
    for src, dest in include_files:
        dest_path = os.path.join(target_dir, dest)
        dest_folder = os.path.dirname(dest_path)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        try:
            if os.path.isdir(src):
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(src, dest_path)
            else:
                shutil.copy2(src, dest_path)
            print(f"Copied {src} to {dest_path}")
        except Exception as e:
            print(f"Error copying {src} to {dest_path}: {e}")
    print("All include files have been copied.")
else:
    print("PyInstaller build failed.")
print("removing version file")
try:
    os.remove(version_file_path )
    print
    ("removed")
except:
    print("error while removing")
print("removing build folder")
try:
    shutil.rmtree("build")
    print("done")
except:
    print("error")
print("removing MentalMath.spec")
try:
    os.remove("mentalMath.spec")
    print("done")
except:
    print("error")
print("editing some files")
try:
    shutil.copytree("dist/mentalMath","mentalMath_build")
    print("done")
    shutil.rmtree("dist")
    print("done")
except:
    print("error")