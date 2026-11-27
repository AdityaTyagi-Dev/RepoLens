# RepoLens 🔍

**A lightweight repository analysis tool that evaluates code quality through measurable metrics.**

RepoLens scans a project directory, analyses its source files and documentation, and generates a report with an overall repository score.

## Features

- Cross-platform directory scanning
- Multi-language identification
- Code statistics and comment density analysis
- Long-line detection
- README analysis
- Automated repository scoring
- Structured terminal reports

## Repository Scoring

RepoLens v0.1 evaluates repositories using three metrics:

| Metric | Maximum Score |
|---|---:|
| Comment Density | 30 |
| Long Line Analysis | 40 |
| README Analysis | 30 |
| **Total** | **100** |

### Rating Classification

| Score | Rating |
|---|---|
| 90–100 | Excellent |
| 80–89 | Very Good |
| 70–79 | Good |
| 60–69 | Average |
| 40–59 | Poor |
| 0–39 | Very Poor |

*The scoring system uses heuristic thresholds and is an initial assessment, not an absolute measure of software quality.*

## How It Works

RepoLens follows a modular architecture:

1. **Scanner:** Discovers files and directories.
2. **Analyser:** Filters relevant files, identifies languages and calculates statistics.
3. **Rating Engine:** Calculates individual metric scores and the overall rating.
4. **Reporter:** Displays the results in the terminal.

## Technologies Used

- Python
- Python Standard Library
- pathlib

## Installation

Clone the repository:

```bash
git clone https://github.com/AdityaTyagi-Dev/RepoLens.git
```

Navigate to the project directory:

```bash
cd RepoLens
```

## Usage

Run the main Python file:
**Windows**
```bash
python main.py
```
**Linux/macOS**
```bash
python3 main.py
```

When prompted, enter the absolute path of the project you want to analyze.
Example:
**Windows**
```
C:\path_to_project\Project
```
**Linux/macOS**
```
/home/user/path_to_project/Project
```
RepoLens will scan the specified directory and generate an analysis report.

## Scoring Criteria

RepoLens evaluates repositories using three metrics, with a combined maximum score of 100 points.

### 1. Comment Density (30 Points)

| Comment Density | Score |
|---|---:|
| Below 10% | Gradually increases |
| 10–25% | 30 |
| 25–50% | Gradually decreases |
| 50% or above | 0 |

### 2. Long Line Analysis (40 Points)

| Long Line Percentage | Score |
|---|---:|
| 0–5% | 40 |
| 5–10% | 35 |
| 10–15% | 30 |
| 15–20% | 20 |
| 20–30% | 10 |
| Above 30% | 0 |

### 3. README Analysis (30 Points)

| README Characters | Score |
|---|---:|
| Missing | 0 |
| Empty | 5 |
| 1–200 | 10 |
| 201–500 | 15 |
| 501–1,000 | 20 |
| 1,001–2,000 | 25 |
| Above 2,000 | 30 |

### Overall Score

The final repository score is calculated as:

`Overall Score = Comment Score + Long Line Score + README Score`

Maximum possible score: **100 points**.

## Sample Output

```
============================================================
                          REPOLENS                          
                Repository Analysis Tool v0.1               
============================================================


[+] PROJECT OVERVIEW
------------------------------------------------------------
Project Name        :        SampleProject
Project Path        :        /home/user/Projects/SampleProject
Total Directories   :        12
Total Files         :        35
Source Files        :        22
Languages Detected  :        3

[+] LANGUAGE DISTRIBUTION
------------------------------------------------------------
Python          :        12 file(s)
Java          :        6 file(s)
JavaScript          :        4 file(s)

[+] CODE STATISTICS
------------------------------------------------------------
Total Lines         :        1850
Code Lines          :        1200
Comment Lines       :        250
Blank Lines         :        400
Comment Density     :        17.24%

[+] LONG LINE ANALYSIS
------------------------------------------------------------
Long Code Lines     :        18
Long Comment Lines  :        7
Total Long Lines    :        25

[+] README ANALYSIS
------------------------------------------------------------
README Found        :        YES
Status              :        Non-empty
Total Lines:        :        85
Blank Lines:        :        9
Total Words         :        520
Total Characters    :        3250

[+] REPOSITORY RATING
------------------------------------------------------------
Comment Score       :        30 / 30
Long Line Score     :        40 / 30
README Score        :        30 / 30
------------------------------------------------------------
Overall Score       :        100 / 100
Rating              :        EXCELLENT

[+] ANALYSIS SUMMARY
------------------------------------------------------------
- 3 programming language(s) detected.
- README documentation is available.
- 25 long line(s) detected.
- Comment Density: 17.24%


============================================================
              Analysis completed successfully               
                   Generated by RepoLens                    
============================================================
```

Sample values are illustrative

## Current Limitations
- Comment detection uses predefined language-specific patterns.
- Complex multiline comment parsing is not fully implemented.
- Long-line detection uses a predefined character threshold.
- README evaluation focuses on basic measurements rather than content quality.
- Repository rating currently uses only three metrics.

## Future Plans
- Advanced code quality analysis
- Improved language-specific parsing
- Project structure analysis
- Testing analysis
- More comprehensive repository evaluation

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

## Author

**Aditya Kumar Tyagi**

GitHub: 
[@AdityaTyagi-Dev](https://github.com/AdityaTyagi-Dev)