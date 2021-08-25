import os

def get_file_extension(absolute_path):
    # unpacking the tuple
    file_name, file_extension = os.path.splitext(absolute_path)
    return file_name, file_extension


def absoluteFilePaths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


def main():
    print("Scanning current directory to detect tools to consider based on the types of files found...")
    print("")
    
    file_extensions_found = set()
    absolute_file_paths = absoluteFilePaths(".")
    
    for path in absolute_file_paths:
        absolute_file_path, suffix = get_file_extension(path)
        file_extensions_found.add(suffix)
        
    if len(file_extensions_found) > 1:
        print(f"We found {len(file_extensions_found)} different types of file extensions in your project.")
        print("Check out these use file scanners:")
        print("https://www.sonarqube.org/")
        print("https://semgrep.dev/")

    if ".html" in file_extensions_found:
        print("'.html'")
        print("Use - https://caniuse.com/")
    
    if ".css" in file_extensions_found:
        print("'.css'")
        print("Use - https://caniuse.com/")

    if ".svg" in file_extensions_found:
        print("'.svg'")
        print("Use - https://caniuse.com/")

    if ".py" in file_extensions_found:
        print("'.py'")
        print("Use - https://github.com/PyCQA/pylint")
        print("Use - https://github.com/PyCQA/flake8")
        print("Use - https://github.com/PyCQA/isort")
        print("Use - https://github.com/psf/black")
    
    if ".tf" in file_extensions_found:
        print("'.tf'")
        print("Use - https://github.com/tfsec/tfsec")
        print("Consider - https://github.com/gruntwork-io/terratest")

    if ".java" in file_extensions_found:
        print("Use - https://pitest.org/")

    if ".sh" in file_extensions_found:
        print("'.sh'")
        print("Use - https://www.shellcheck.net/")
        print("Use - https://explainshell.com/")

    if ".js" in file_extensions_found:
        print("'.js'")
        print("Consider - https://github.com/lirantal/lockfile-lint")
        print("Consider - https://www.sonarsource.com/js/")
        print("Use - https://caniuse.com/")
    

if __name__ == '__main__':
    main()