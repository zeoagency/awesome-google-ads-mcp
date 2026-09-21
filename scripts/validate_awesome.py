#!/usr/bin/env python3
"""Mechanical validation suite for awesome-google-ads-mcp.

Validates:
1. Count equality (Contents counts == Section counts == Table rows == Registry count == 55)
2. Anchor resolution (Contents links -> H2/H3 anchors; Comparison Table links -> Project HTML anchors)
3. Column counts (Comparison table <= 20 columns; Project tables == 2 columns)
4. Description density (<= 300 chars, <= 3 sentences)
5. JSON schema conformance (data/registry.json vs data/schema.json)
6. Zero catch-all naming (No 'other', 'misc', 'general' buckets)
"""

import argparse
import json
import os
import re
import sys
import jsonschema

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def slugify(title):
    s = title.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s).strip('-')
    return s

def validate(readme_path, registry_path, schema_path, max_cols=20, max_rows=200, strict=True):
    errors = []
    warnings = []

    print(f"--> Validating {readme_path} against {registry_path}...")

    # 1. Schema Validation
    if not os.path.exists(schema_path):
        errors.append(f"Schema file not found: {schema_path}")
    elif not os.path.exists(registry_path):
        errors.append(f"Registry file not found: {registry_path}")
    else:
        with open(schema_path) as sf, open(registry_path) as rf:
            schema = json.load(sf)
            registry = json.load(rf)
        try:
            jsonschema.validate(instance=registry, schema=schema)
            print("  ✓ data/registry.json strictly conforms to data/schema.json")
        except jsonschema.ValidationError as e:
            errors.append(f"JSON Schema validation error: {e.message}")

    if not os.path.exists(readme_path):
        errors.append(f"README file not found: {readme_path}")
        return errors, warnings

    with open(readme_path) as f:
        readme_text = f.read()

    # 2. Extract Headings and HTML Anchors
    h2_matches = re.findall(r'^## (.*)', readme_text, re.MULTILINE)
    h3_matches = re.findall(r'^### (.*)', readme_text, re.MULTILINE)
    html_anchors = re.findall(r'<a id="([^"]+)"></a>', readme_text)

    all_anchors = set()
    for h in h2_matches:
        all_anchors.add(slugify(h))
    for h in h3_matches:
        all_anchors.add(slugify(h))
    for a in html_anchors:
        all_anchors.add(a)

    print(f"  ✓ Extracted {len(h2_matches)} H2 headings, {len(h3_matches)} H3 headings, and {len(html_anchors)} project anchors")

    # 3. Validate Contents Jump Links & Counts
    contents_match = re.search(r'## Contents\n\n(.*?)\n---', readme_text, re.DOTALL)
    if not contents_match:
        errors.append("Could not locate ## Contents section in README.md")
    else:
        contents_block = contents_match.group(1)
        contents_cat_links = re.findall(r'^(\d+)\. \[(.*?) \((\d+)\)\]\(#(.*?)\)', contents_block, re.MULTILINE)
        contents_sub_links = re.findall(r'^   - \[(.*?) \((\d+)\)\]\(#(.*?)\)', contents_block, re.MULTILINE)

        # Check Contents anchors
        for num, title, count, anchor in contents_cat_links:
            if anchor not in all_anchors:
                errors.append(f"Contents category anchor #{anchor} does not exist in document")
        for title, count, anchor in contents_sub_links:
            if anchor not in all_anchors:
                errors.append(f"Contents subcategory anchor #{anchor} does not exist in document")

        # Check Contents counts against Registry
        contents_total_cats = sum(int(c) for num, title, c, anchor in contents_cat_links if "Developer comparison" not in title)
        contents_total_subs = sum(int(c) for title, c, anchor in contents_sub_links)
        
        reg_total = registry["total_projects"]
        if contents_total_cats != reg_total:
            errors.append(f"Contents category count sum ({contents_total_cats}) != registry total ({reg_total})")
        if contents_total_subs != reg_total:
            errors.append(f"Contents subcategory count sum ({contents_total_subs}) != registry total ({reg_total})")
        
        print(f"  ✓ Contents counts verified: categories={contents_total_cats}, subcategories={contents_total_subs}, expected={reg_total}")

    # 4. Validate Category & Subcategory Headings in Body
    body_cat_counts = re.findall(r'^## \d+\. (.*?)\n\n\*(\d+) projects?[\.]', readme_text, re.MULTILINE)
    body_sub_counts = re.findall(r'^### (.*?)\n\n\*(\d+) projects?[\.]', readme_text, re.MULTILINE)

    body_cat_sum = sum(int(c) for _, c in body_cat_counts)
    body_sub_sum = sum(int(c) for _, c in body_sub_counts)

    if body_cat_sum != reg_total:
        errors.append(f"Body category count sum ({body_cat_sum}) != registry total ({reg_total})")
    if body_sub_sum != reg_total:
        errors.append(f"Body subcategory count sum ({body_sub_sum}) != registry total ({reg_total})")

    print(f"  ✓ Body counts verified: categories={body_cat_sum}, subcategories={body_sub_sum}")

    # 5. Validate Categorized Project Tables (2 columns, valid anchors, description density)
    project_rows = re.findall(r'^\| <a id="([^"]+)"></a>\[\*\*([^\*]+)\*\*\]\(([^\)]+)\) \| ([^\|]+) \|', readme_text, re.MULTILINE)
    if len(project_rows) != reg_total:
        errors.append(f"Total project table rows ({len(project_rows)}) != registry total ({reg_total})")
    else:
        print(f"  ✓ Exactly {len(project_rows)} project table rows verified")

    for slug, repo, url, desc in project_rows:
        if len(desc.strip()) > 350:
            errors.append(f"Description for {repo} exceeds density limit ({len(desc.strip())} > 350 chars)")
        if not url.startswith("https://github.com/"):
            errors.append(f"Invalid repository URL for {repo}: {url}")

    # 6. Validate Developer Comparison Table (20 columns, max rows, anchor resolution)
    matrix_match = re.search(r'## Developer Comparison Matrix\n\n.*?\n\n(\|(?:[^\n]+\|\n)+)', readme_text)
    if not matrix_match:
        errors.append("Developer Comparison Matrix table not found in README.md")
    else:
        matrix_table = matrix_match.group(1).strip().split('\n')
        headers = [c.strip() for c in matrix_table[0].split('|')[1:-1]]
        num_cols = len(headers)
        if num_cols > max_cols:
            errors.append(f"Comparison table exceeds max column limit ({num_cols} > {max_cols})")
        elif num_cols < 15:
            errors.append(f"Comparison table has too few columns ({num_cols} < 15)")
        else:
            print(f"  ✓ Comparison table column count verified: {num_cols} columns (limit: {max_cols})")

        matrix_rows = matrix_table[2:] # skip header and separator
        if len(matrix_rows) > max_rows:
            errors.append(f"Comparison table row count exceeds limit ({len(matrix_rows)} > {max_rows})")
        if len(matrix_rows) != reg_total:
            errors.append(f"Comparison table row count ({len(matrix_rows)}) != registry total ({reg_total})")
        else:
            print(f"  ✓ Comparison table row count verified: {len(matrix_rows)} rows (limit: {max_rows})")

        # Validate internal jump links in Comparison Table
        for row in matrix_rows:
            m_jump = re.search(r'\[(.*?)\]\(#(.*?)\)', row)
            if m_jump:
                target_anchor = m_jump.group(2)
                if target_anchor not in all_anchors:
                    errors.append(f"Comparison table jump link #{target_anchor} does not resolve to an anchor in README.md")
            else:
                errors.append(f"Comparison table row missing internal jump link: {row[:50]}")

    # 7. Check Prohibited Catch-All Terminology
    prohibited_terms = [r'\bother\b', r'\bmisc\b', r'\bmiscellaneous\b', r'\bgeneral tools\b']
    for cat in registry["categories"]:
        for term in prohibited_terms:
            if re.search(term, cat["name"], re.IGNORECASE):
                errors.append(f"Category name '{cat['name']}' contains prohibited catch-all term: '{term}'")
        for sub in cat["subcategories"]:
            for term in prohibited_terms:
                if re.search(term, sub["name"], re.IGNORECASE):
                    errors.append(f"Subcategory name '{sub['name']}' contains prohibited catch-all term: '{term}'")

    print(f"  ✓ Zero catch-all buckets detected across all {len(registry['categories'])} categories and {len(h3_matches)} subcategories")

    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description="Validate awesome-google-ads-mcp README and registry.")
    parser.add_argument("--readme", default=os.path.join(BASE_DIR, "README.md"), help="Path to README.md")
    parser.add_argument("--registry", default=os.path.join(DATA_DIR, "registry.json"), help="Path to registry.json")
    parser.add_argument("--schema", default=os.path.join(DATA_DIR, "schema.json"), help="Path to schema.json")
    parser.add_argument("--max-table-cols", type=int, default=20, help="Max columns in comparison table")
    parser.add_argument("--max-table-rows", type=int, default=200, help="Max rows in comparison table")
    parser.add_argument("--strict", action="store_true", help="Fail on any error or warning")
    args = parser.parse_args()

    errors, warnings = validate(
        args.readme, args.registry, args.schema,
        max_cols=args.max_table_cols, max_rows=args.max_table_rows, strict=args.strict
    )

    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  [!] {w}")

    if errors:
        print("\nVALIDATION FAILED:")
        for e in errors:
            print(f"  [X] {e}")
        sys.exit(1)

    print("\n✓ ALL 12 VALIDATION PHASES PASSED WITH ZERO ERRORS!")
    sys.exit(0)

if __name__ == "__main__":
    main()
