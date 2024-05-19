import subprocess

def RunConan(build_type):
    subprocess.run((
        'conan', 'install', '.',
        '--build', 'missing',
        '--output-folder=./Dependencies',
        f'--settings=build_type={build_type}'
    ))

def RunPremake(action):
    subprocess.run((
        './vendor/premake/premake5.exe', 
        '--file=Build.lua',
        action
    ))


if __name__ == "__main__":
    RunConan("Debug")
    RunConan("Release")
    RunPremake("vs2022")
