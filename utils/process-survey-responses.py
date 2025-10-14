#!/usr/bin/env python3
"""
survey_to_md.py

Usage:
    python survey_to_md.py input.xlsx output_folder/

Reads an Excel or CSV file of survey responses and writes one Markdown file per response.
The output contains:
  - YAML front matter (title, summary, tags)
  - One line of project attribution
  - The full long summary as-is (no added headings)
  - Optional links at the bottom as a markdown table

Dependencies:
    pip install pandas openpyxl python-slugify
"""

import sys
import re
import pandas as pd
from pathlib import Path
from slugify import slugify


# --- Column normalisation mapping ---
COLUMN_MAP = {
    'id': 'id',
    'email': 'email',
    'name': 'name',
    'name2': 'name2',
    'job title': 'job_title',
    'team': 'team',
    'date you completed the mres': 'mres_date',
    'what is/was the title of your project?': 'title',
    'please give us a one sentence summary of your project': 'one_sentence_summary',
    'give a summary of your project in a few paragraphs, include the process of deciding your project, as well as any summary of results': 'long_summary',
    'please share any useful links related to your project (e.g. repository link, documentation link etc) if applicable.': 'links',
    'which domain area was your project': 'domain_area',
    'techniques used in your project': 'techniques',
    'which of the following project types was your project:': 'project_type',
    'what data type(s) did you use': 'data_types',
    'what coding language(s) did you use?': 'coding_languages',
    'what is your project status': 'project_status',
}


# --- Helpers ---
def normalize_columns(cols):
    mapping = {}
    for c in cols:
        c_norm = c.strip().lower()
        if c_norm in COLUMN_MAP:
            mapping[c] = COLUMN_MAP[c_norm]
        else:
            mapping[c] = c_norm.replace(' ', '_')
    return mapping


def escape_single_quote(s):
    return s.replace("'", "''")


def parse_tags_from_row(row):
    tags = []
    for field in ['domain_area', 'techniques', 'project_type', 'data_types', 'coding_languages', 'project_status']:
        val = row.get(field)
        if not val or (isinstance(val, float) and pd.isna(val)):
            continue
        parts = re.split(r'[;,]+', str(val))
        for p in parts:
            p_clean = p.strip()
            if p_clean:
                p_upper = p_clean.upper()
                if p_upper not in tags:
                    tags.append(p_upper)
    return tags


def format_links_table(links_value):
    """
    Try to produce a markdown table for links.
    If the links_value looks like a URL, wrap it in markdown format.
    """
    if not links_value or not isinstance(links_value, str):
        return ""

    links_value = links_value.strip()
    if not links_value:
        return ""

    # Try to extract URLs
    urls = re.findall(r'(https?://[^\s\)]+)', links_value)
    if not urls:
        # Just show whatever is there
        return f"\n\nOutput|Link\n---|---\n{links_value}| "

    # Example heuristic: if only one URL, make it the link target
    rows = []
    for url in urls:
        # A simple guess for description
        desc = "Code and Documentation - private while under development" if "github" in url.lower() else "Project Link"
        rows.append(f"{desc}|[Link]({url})")

    table = "Output|Link\n---|---\n" + "\n".join(rows)
    return "\n\n" + table


# --- Markdown builder ---
def build_markdown(row):
    title = row.get('title') or 'Untitled'
    summary = row.get('one_sentence_summary') or ''
    long_summary = row.get('long_summary') or ''
    author = row.get('name') or row.get('name2') or ''
    job_title = row.get('job_title') or ''
    team = row.get('team') or ''
    mres_date = row.get('mres_date') or ''
    tags = parse_tags_from_row(row)
    links = row.get('links') or ''

    # --- YAML front matter ---
    yaml_lines = [
        '---',
        f"title: '{escape_single_quote(title)}'",
        f"summary: '{escape_single_quote(summary)}'",
        "tags: [" + ', '.join([f"'{t}'" for t in tags]) + "]",
        '---',
        ''
    ]

    # --- Attribution line ---
    author_line = f"*This project was completed by {author}*"
    extras = []
    if job_title:
        extras.append(job_title)
    if team:
        extras.append(f"in the {team} Team")
    if extras:
        author_line += ', ' + ', '.join(extras)
    if mres_date:
        author_line += ', as part of the Data Science MRes at the University of Leeds.'

    # --- Compose body ---
    body = f"{author_line}\n\n{long_summary.strip()}"

    # --- Add links table if applicable ---
    links_section = format_links_table(links)
    if links_section:
        body += links_section

    return '\n'.join(yaml_lines) + body +'\n#'


# --- File processing ---
def process_dataframe(df, out_dir):
    col_map = normalize_columns(list(df.columns))
    df_renamed = df.rename(columns=col_map)
    out_dir.mkdir(parents=True, exist_ok=True)

    for idx, row_series in df_renamed.iterrows():
        row = {k: (None if (isinstance(v, float) and pd.isna(v)) else v) for k, v in row_series.items()}
        md_text = build_markdown(row)
        rid = str(row.get('id') or idx)
        name = str(row.get('name') or row.get('name2') or 'unknown')
        fname = f"{rid}-{slugify(name)}.md"
        with open(out_dir / fname, 'w', encoding='utf-8') as f:
            f.write(md_text)
        print(f"Wrote {fname}")


# --- Input / main ---
def read_input(path):
    if path.suffix.lower() in ('.xls', '.xlsx'):
        return pd.read_excel(path, engine='openpyxl')
    elif path.suffix.lower() == '.csv':
        return pd.read_csv(path)
    else:
        raise ValueError("Unsupported input format. Provide .xlsx or .csv")


def main(argv):
    if len(argv) < 3:
        print("Usage: python utils/process-survey-responses.py input.xlsx output_folder/")
        sys.exit(1)
    input_path = Path(argv[1])
    out_dir = Path(argv[2])
    df = read_input(input_path)
    process_dataframe(df, out_dir)


if __name__ == '__main__':
    main(sys.argv)
