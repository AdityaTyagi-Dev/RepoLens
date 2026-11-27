from pathlib import Path

IGNORED_DIRECTORIES = [
    # Version Control
    ".git", ".svn", ".hg", ".bzr",

    # Python
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".tox", ".nox", ".venv", "venv", "env", "site-packages", "htmlcov", ".hypothesis",

    # JavaScript / Node.js
    "node_modules", ".next", ".nuxt", ".output", ".svelte-kit", ".angular", ".parcel-cache", ".turbo", ".yarn", ".pnpm-store",

    # Build and distribution
    "build", "dist", "out", "target", "bin", "obj", "release", "debug",

    # IDE and editor
    ".idea", ".vscode", ".vs", ".fleet",

    # Framework and tool caches
    ".cache", ".gradle", ".terraform", ".serverless", ".webpack", ".sass-cache", ".eslintcache",

    # Operating System
    ".Trash", ".Trashes", "System Volume Information", "$RECYCLE.BIN"
]

IGNORED_FILES = [
    # Files to ignore by name
    ".DS_Store", "Thumbs.db", "desktop.ini", "npm-debug.log", "yarn-error.log", "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Pipfile.lock", "poetry.lock", ".env", ".gitignore", "LICENSE"
]

IGNORED_EXTENSIONS = [
    # Images
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".svg", ".ico", ".tiff", ".heic", 

    # Audio
    ".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".aiff",

    # Video
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp",

    # Documents
    ".pdf", ".doc", ".docx", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".rtf", ".epub",

    # Archives
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tgz", ".iso",

    # Executables and binaries
    ".exe", ".dll", ".so", ".dylib", ".bin", ".class", ".pyc", ".pyo", ".pyd", ".o", ".obj", ".a", ".lib", ".jar", ".war", 

    # Temporary and backup files
    ".tmp", ".temp", ".bak", ".old", ".swp", ".swo", ".orig", ".log",

    # Database and storage
    ".db", "sqlite", "sqlite3", ".mdb"
]

LANGUAGE = {
    ".py": "Python",
    ".pyw": "Python",
    ".pyi": "Python",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".hpp": "C++",
    ".hh": "C++",
    ".hxx": "C++",
    ".cs": "C#",
    ".js": "JavaScript",
    ".mjs": "JavaScript",
    ".cjs": "javaScript",
    ".jsx": "JavaScript",
    ".ts": "TypeScript",
    ".mts": "TypeScript",
    ".cts": "TypeScript",
    ".tsx": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".rake": "Ruby",
    ".php": "PHP",
    ".phtml": "PHP",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".kts": "Kotlin",
    ".dart": "Dart",
    ".r": "R",
    ".scala": "Scala",
    ".sc": "Scala",
    ".pm": "Perl",
    ".lua": "Lua",
    ".sh": "Shell",
    ".bash": "Shell",
    ".zsh": "Shell",
    ".ps1": "PowerShell",
    ".psm1": "PowerShell",
    ".mm": "Objective-C",
    ".jl": "Julia",
    ".hs": "Haskell",
    ".lhs": "Haskell",
    ".ex": "Elixir",
    ".exs": "Elixir",
    ".erl": "Erlang",
    ".hrl": "Erlang",
    ".clj": "Clojure",
    ".cljs": "Clojure",
    ".cljc": "Clojure",
    ".fs": "F#",
    ".fsi": "F#",
    ".fsx": "F#",
    ".vb": "Visual Basic",
    ".asm": "Assembly",
    ".s": "Assembly",
    ".sol": "Solidity",
    ".groovy": "Groovy",
    ".gvy": "Groovy",
    ".zig": "Zig",
    ".nim": "Nim",
    ".ml": "OCaml",
    ".mli": "OCaml",
    ".f": "Fortran",
    ".for": "Fortran",
    ".f90": "Fortran",
    ".f95": "Fortran",
    ".cob": "COBOL",
    ".cbl": "COBOL",
    ".sql": "SQL",
    ".wat": "WebAssembly",
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".json": "JSON",
    ".csv": "CSV",
    ".yaml": "YAML",
    ".md": "Markdown",
    ".xml": "XML",
    ".txt": "Text"
}

UNIQUE = {
    "Dockerfile": "Dockerfile",
    "Makefile": "Make",
    "Jenkinsfile": "Jenkins",
    "Gemfile": "Ruby"
}

SINGLE_LINE_COMMENTS = {
    "Python": "#",
    "Ruby": "#",
    "R": "#",
    "Perl": "#",
    "Shell": "#",
    "PowerShell": "#",
    "Julia": "#",
    "Elixir": "#",
    "Nim": "#",
    "Java": "//",
    "C": "//",
    "C++": "//",
    "C#": "//",
    "JavaScript": "//",
    "TypeScript": "//",
    "Go": "//",
    "Rust": "//",
    "PHP": ["//", "#"],
    "Swift": "//",
    "Kotlin": "//",
    "Dart": "//",
    "Solidity": "//",
    "Groovy": "//",
    "Zig": "//",
    "Objective-C": "//",
    "Scala": "//",
    "Lua": "--",
    "Haskell": "--",
    "SQL": "--",
    "Erlang": "%",
    "Clojure": ";",
    "Assembly": ";",
    "WebAssembly": ";;",
    "F#": "//",
    "Visual Basic": "'",
    "OCaml": None,
    "Fortran": "!",
    "COBOL": "*>"
}

MULTILINE_COMMENTS = {
    "Python": [('"""', '"""'), ("'''", "'''")],
    "Java": [("/*", "*/")],
    "C": [("/*", "*/")],
    "C++": [("/*", "*/")],
    "C#": [("/*", "*/")],
    "JavaScript": [("/*", "*/")],
    "TypeScript": [("/*", "*/")],
    "Go": [("/*", "*/")],
    "Rust": [("/*", "*/")],
    "PHP": [("/*", "*/")],
    "Swift": [("/*", "*/")],
    "Kotlin": [("/*", "*/")],
    "Dart": [("/*", "*/")],
    "Scala": [("/*", "*/")],
    "Lua": [("--[[", "]]")],
    "Julia": ["#=", "=#"],
    "Haskell": ["{-", "-}"],
    "F#": [("(*", "*)")],
    "OCaml": [("(*", "*)")],
    "Nim": [("#[", "]#")],
    "Groovy": [("/*", "*/")],
    "Solidity": [("/*", "*/")],
    "Zig": [("/*", "*/")],
    "Fortran": None,
    "COBOL": None,
    "Visual Basic": None,
    "Shell": None,
    "Perl": None,
    "Ruby": None,
    "R": None,
    "Elixir": None,
    "Erlang": None,
    "Clojure": None,
    "Assembly": None,
    "WebAssembly": None,
    "Objective-C": [("/*", "*/")]

}

def filter_directories(all_directories):
    filtered = all_directories.copy()
    ignored_folders = []
    for directory in all_directories:
        splited_directory = list(Path(directory).parts)
        for item in splited_directory:
            if item in IGNORED_DIRECTORIES:
                filtered.remove(directory)
                ignored_folders.append(item)
                break
    return [filtered, ignored_folders]

def filter_files(scanner_output):
    ignored_folders = filter_directories(scanner_output['directory'])[1]
    files = scanner_output['file'].copy()
    for file in scanner_output['file']:
        ignored = False
        for sub in list(Path(file).parts):
            if sub in ignored_folders:
                files.remove(file)
                ignored = True
                break
        if ignored:
            continue
        elif Path(file).suffix in IGNORED_EXTENSIONS:
            files.remove(file)
            continue
        elif Path(file).name in IGNORED_FILES:
            files.remove(file)
            continue
    return files


def identify_language(scanner_output):
    files = filter_files(scanner_output)
    language = {}
    for file in files:
        if Path(file).suffix.lower() in LANGUAGE:
            language[file] = LANGUAGE[Path(file).suffix.lower()]
        else:
            if Path(file).name in UNIQUE:
                language[file] = UNIQUE[Path(file).name]
            else:
                language[file] = None
    return language

def read_source_files(scanner_output):
    language = identify_language(scanner_output)
    source_code = {}
    for file in language:
        with open(file, 'r', encoding='utf-8', errors='replace') as f:
            source_code[file] = (language[file], f.readlines())
    return source_code

def calculate_file_statistics(scanner_output):
    source_code = read_source_files(scanner_output)
    lines_analysis = {}
    total_files = 0
    for file in source_code:
        total_files += 1
        if Path(file).suffix.lower() in [".md", ".mdx", ".txt", ".rst", ".adoc", ".json", ".csv", ".tsv", ".xml", ".yaml", ".yml", ".toml", ".markdown", ".mdown", ".mkd", ".text", ".asciidoc", ".org"]:
            continue
        total_lines = len(source_code[file][1])
        blank_lines = 0
        comment_lines = 0
        code_lines = 0
        long_code_lines = 0
        long_comment_lines = 0
        inside_comment = False

        for line in source_code[file][1]:
            line = line.strip()
            if line == '':
                blank_lines += 1
                continue

            language = source_code[file][0]
            length_of_line = len(line)

            if inside_comment:
                comment_lines += 1

                for start, end in MULTILINE_COMMENTS.get(language, []):
                    if end in line:
                        inside_comment = False
                        break
                continue
            multiline_found = False
            for start, end in MULTILINE_COMMENTS.get(language, []):
                if start in line:
                    comment_lines += 1
                    multiline_found = True
                    if end not in line[line.index(start) + len(start):]:
                        inside_comment = True
                    break
            if multiline_found:
                continue
            elif ((isinstance(SINGLE_LINE_COMMENTS.get(language), str) and line.startswith(SINGLE_LINE_COMMENTS[language])) or (isinstance(SINGLE_LINE_COMMENTS.get(language), list) and any(line.startswith(symbol) for symbol in SINGLE_LINE_COMMENTS[language]))):
                comment_lines += 1
                if length_of_line >= 100:
                    long_comment_lines += 1
                continue
            else:
                code_lines += 1
                if length_of_line >= 100:
                    long_code_lines += 1
        comment_density = None if not total_lines else (comment_lines / (comment_lines + code_lines)) * 100
        lines_analysis[file] = (language, {
            "total_lines": total_lines,
            "blank_lines": blank_lines,
            "comment_lines": comment_lines,
            "code_lines": code_lines,
            "comment_density": comment_density,
            "long_code_lines": long_code_lines,
            "long_comment_lines": long_comment_lines,
            })
    return lines_analysis, total_files

def calculate_project_statistics(scanner_output):
    lines_analysis, total_files = calculate_file_statistics(scanner_output)
    all_filtered_directories = filter_directories(scanner_output['directory'])[0]
    file_by_language = {}
    total_lines = 0
    blank_lines = 0
    comment_lines = 0
    code_lines = 0
    long_code_lines = 0
    long_comment_lines = 0
    comment_density = None
    for file in lines_analysis:
        total_lines += lines_analysis[file][1]["total_lines"]
        blank_lines += lines_analysis[file][1]["blank_lines"]
        comment_lines += lines_analysis[file][1]["comment_lines"]
        code_lines += lines_analysis[file][1]["code_lines"]
        long_comment_lines += lines_analysis[file][1]["long_comment_lines"]
        long_code_lines += lines_analysis[file][1]["long_code_lines"]
        if lines_analysis[file][0] not in file_by_language:
            file_by_language[lines_analysis[file][0]] = 1
        else:
            file_by_language[lines_analysis[file][0]] += 1
    comment_density = (comment_lines / (comment_lines + code_lines)) * 100 if total_lines else None
    project_statistics = {
        "total_directories": len(all_filtered_directories),
        "total_files": total_files,
        "source_files": len(lines_analysis),
        "languages": file_by_language,
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "code_lines": code_lines,
        "comment_density": comment_density,
        "long_comment_lines": long_comment_lines,
        "long_code_lines": long_code_lines,
        "long_lines": long_code_lines + long_comment_lines
    }

    return project_statistics

def find_readme(path):
    for name in path.iterdir():
        name2 = name.name
        if name.is_file() and name2.lower().startswith("readme"):
            if name2.lower() == "readme" or (name2.lower().startswith("readme.") and Path(name2.lower()).suffix in [".md", ".markdown", ".mdown", ".mkd", ".rst", ".txt", ".text", ".adoc", ".asciidoc", ".org", ".html"]):
                return name
    return False

def analyze_readme(path):
    file = find_readme(path)
    if not file:
        return {
            "found": False,
            "empty": None,
            "total_lines": None,
            "total_words": None,
            "total_chars": None,
            "blank_lines": None
    }
    total_lines = 0
    total_words = 0
    total_chars = 0
    blank_lines = 0
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        data = f.readlines()

    for line in data:
        line = line.strip()
        total_lines += 1
        total_words += len(line.split(' '))
        total_chars += len(line)
        if line == "":
            blank_lines += 1

    empty = "Empty" if not total_chars else "Non-empty"
    readme_analysis = {
        "found": True,
        "empty": empty,
        "total_lines": total_lines,
        "total_words": total_words,
        "total_chars": total_chars,
        "blank_lines": blank_lines
    }

    return readme_analysis

def comment_score(project_statistics):
    comment_density = round(project_statistics['comment_density'], 2)
    if comment_density < 10:
        return int(comment_density * 3)
    elif comment_density <= 25:
        return 30
    elif comment_density <= 30:
        return 24
    elif comment_density <= 40:
        return 12
    else:
        return 0

def long_line_score(project_statistics):
    long_percentage = (project_statistics['long_lines'] / (project_statistics['comment_lines'] + project_statistics['code_lines'])) * 100
    if long_percentage < 5:
        return 40
    elif long_percentage < 10:
        return 35
    elif long_percentage < 15:
        return 30
    elif long_percentage < 20:
        return 20
    elif long_percentage < 30:
        return 10
    else:
        return 0

def readme_score(readme_analysis):
    if not readme_analysis['found']:
        return 0
    elif readme_analysis['empty'] == 'Empty':
        return 5
    elif readme_analysis['total_chars'] <= 200:
        return 10
    elif readme_analysis['total_chars'] < 500:
        return 15
    elif readme_analysis['total_chars'] < 1000:
        return 20
    elif readme_analysis['total_chars'] < 2000:
        return 25
    else:
        return 30


def total_score(project_statistics, readme_analysis):
    comment_s = comment_score(project_statistics)
    long_line_s = long_line_score(project_statistics)
    readme_s = readme_score(readme_analysis)
    score = comment_s + long_line_s + readme_s

    if score < 39:
        return (comment_s, long_line_s, readme_s, score, "POOR")
    elif score < 59:
        return (comment_s, long_line_s, readme_s, score, "NEEDS IMPROVEMENT")
    elif score < 69:
        return (comment_s, long_line_s, readme_s, score, "AVERAGE")
    elif score < 79:
        return (comment_s, long_line_s, readme_s, score, "GOOD")
    elif score < 89:
        return (comment_s, long_line_s, readme_s, score, "VERY GOOD")
    return (comment_s, long_line_s, readme_s, score, "EXCELLENT")