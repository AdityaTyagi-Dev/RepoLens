from repolens.scanner import check_items
from repolens.analyser import calculate_project_statistics
from repolens.analyser import analyze_readme
from repolens.analyser import total_score
from repolens.reporter import report_everything
from pathlib import Path

path = Path(input("Enter the path to repository: "))

scanner_output = check_items(path)
project_statistics = calculate_project_statistics(scanner_output)
readme_analysis_data = analyze_readme(path)
comment_score, long_line_score, readme_score, score, rating = total_score(project_statistics, readme_analysis_data)

report_everything(project_statistics, path, readme_analysis_data, comment_score, long_line_score, readme_score, score, rating)