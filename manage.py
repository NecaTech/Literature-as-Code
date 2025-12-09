#!/usr/bin/env python3
"""
manage.py
Role: Unified CLI Entry Point
Function: Orchestrates project tasks (init, assemble, lint, pipeline).
"""

import argparse
import sys
import os
from pathlib import Path
import shutil

# Ensure we can import from _SYSTEM
PROJECT_ROOT = Path(__file__).parent.resolve()
sys.path.append(str(PROJECT_ROOT))

try:
    from _SYSTEM.automation import context_assembler, test_runner
    # Pipeline runner will be imported dynamically or added later
except ImportError as e:
    print(f"Error importing automation modules: {e}")
    print("Ensure _SYSTEM/automation/ contains __init__.py")
    sys.exit(1)

def command_init(args):
    """Initialize a new project structure."""
    print("Initializing Literature as Code project...")
    
    # 1. Ensure directories exist
    dirs = [
        "00_SPECS", "00_SPECS/.system",
        "01_CONTEXT_DB/characters", "01_CONTEXT_DB/world",
        "02_STRUCTURE/specs_json",
        "03_MANUSCRIPT/01_drafts", "03_MANUSCRIPT/02_staging", "03_MANUSCRIPT/03_master",
        "04_TESTS/linting_rules", "04_TESTS/unit_tests",
        "05_BUILD/logs"
    ]
    
    for d in dirs:
        (PROJECT_ROOT / d).mkdir(parents=True, exist_ok=True)
        
    # 2. Copy templates if directories are empty
    defaults_dir = PROJECT_ROOT / "_SYSTEM/defaults"
    
    # Copy Specs Templates
    specs_src = defaults_dir / "templates"
    specs_dst = PROJECT_ROOT / "00_SPECS"
    if specs_src.exists():
        for item in specs_src.glob("*"):
            dst_file = specs_dst / item.name
            if not dst_file.exists():
                shutil.copy(item, dst_file)
                print(f"✓ Created: {dst_file.relative_to(PROJECT_ROOT)}")
                
    # Copy Linting Rules
    rules_src = defaults_dir / "linting_rules"
    rules_dst = PROJECT_ROOT / "04_TESTS/linting_rules"
    if rules_src.exists():
        for item in rules_src.glob("*.json"):
            dst_file = rules_dst / item.name
            if not dst_file.exists():
                shutil.copy(item, dst_file)
                print(f"✓ Installed Rule: {item.name}")

    # Copy Sommaire Template
    sommaire_src = defaults_dir / "templates/sommaire.md"
    sommaire_dst = PROJECT_ROOT / "03_MANUSCRIPT/01_drafts/sommaire.md"
    if sommaire_src.exists() and not sommaire_dst.exists():
        shutil.copy(sommaire_src, sommaire_dst)
        print(f"✓ Created: {sommaire_dst.relative_to(PROJECT_ROOT)}")

    print("✓ Project initialized successfully.")

def command_assemble(args):
    """Run Context Assembler."""
    print(f"Running Context Assembler for {args.spec}...")
    try:
        context_assembler.run(args.spec, args.output)
    except Exception as e:
        print(f"Error during assembly: {e}")
        sys.exit(1)

def command_lint(args):
    """Run Linting/Test Runner."""
    print(f"Running Linter on {args.file}...")
    
    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        sys.exit(1)
        
    with open(args.file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Load specs mock or real? For now, empty spec if not provided
    # ideally we find the matching spec for the chapter
    spec = {} 
    
    report = test_runner.evaluate_draft(content, spec)
    
    if report['overall_score'] < 0.8:
        print("\n⚠ Quality standard not met (< 0.8)")
        if args.strict:
            sys.exit(1)
    else:
        print("\n✓ Quality standard met.")

def command_pipeline(args):
    """Execute the workflow pipeline."""
    from _SYSTEM.automation import pipeline_runner
    pipeline_runner.run()

def main():
    parser = argparse.ArgumentParser(description="Literature as Code - Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # INIT
    parser_init = subparsers.add_parser("init", help="Initialize project structure")
    
    # ASSEMBLE
    parser_assemble = subparsers.add_parser("assemble", help="Assemble context for a chapter")
    parser_assemble.add_argument("spec", help="Path to JSON spec file")
    parser_assemble.add_argument("-o", "--output", help="Output file for assembled prompt")
    
    # LINT
    parser_lint = subparsers.add_parser("lint", help="Lint a manuscript file")
    parser_lint.add_argument("file", help="Path to markdown file to lint")
    parser_lint.add_argument("--strict", action="store_true", help="Fail with exit code 1 if score < 0.8")
    
    # PIPELINE
    parser_pipe = subparsers.add_parser("pipeline", help="Run the full workflow pipeline")
    
    args = parser.parse_args()
    
    if args.command == "init":
        command_init(args)
    elif args.command == "assemble":
        command_assemble(args)
    elif args.command == "lint":
        command_lint(args)
    elif args.command == "pipeline":
        command_pipeline(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
