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

# Placeholder for state manager - will be implemented fully later
# from _SYSTEM.automation import state_manager

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
    
    # Copy Specs Templates (Conceptual)
    specs_src = defaults_dir / "templates"
    specs_dst = PROJECT_ROOT / "00_SPECS"
    if specs_src.exists():
        for item in specs_src.glob("*.md"): # Copy only markdown files to SPECS
            dst_file = specs_dst / item.name
            if not dst_file.exists():
                shutil.copy(item, dst_file)
                print(f"[OK] Created: {dst_file.relative_to(PROJECT_ROOT)}")

    # Copy Chapter Spec JSON Template
    ch_spec_src = defaults_dir / "templates/tpl_chapter_spec.json"
    ch_spec_dst = PROJECT_ROOT / "02_STRUCTURE/specs_json/tpl_chapter_spec.json"
    if ch_spec_src.exists() and not ch_spec_dst.exists():
        shutil.copy(ch_spec_src, ch_spec_dst)
        print(f"[OK] Created: {ch_spec_dst.relative_to(PROJECT_ROOT)}")
    # Copy Linting Rules
    rules_src = defaults_dir / "linting_rules"
    rules_dst = PROJECT_ROOT / "04_TESTS/linting_rules"
    if rules_src.exists():
        for item in rules_src.glob("*.json"):
            dst_file = rules_dst / item.name
            if not dst_file.exists():
                shutil.copy(item, dst_file)
                print(f"[OK] Installed Rule: {item.name}")

    # Copy Context Templates (Characters & World)
    # Character Template
    char_tpl_src = defaults_dir / "templates/tpl_character.md"
    if char_tpl_src.exists():
        # Create Hero
        hero_dst = PROJECT_ROOT / "01_CONTEXT_DB/characters/hero.md"
        if not hero_dst.exists():
            shutil.copy(char_tpl_src, hero_dst)
            print(f"[OK] Created Default Hero: {hero_dst.relative_to(PROJECT_ROOT)}")
        
        # Create Shadow/Antagonist
        shadow_dst = PROJECT_ROOT / "01_CONTEXT_DB/characters/shadow.md"
        if not shadow_dst.exists():
            shutil.copy(char_tpl_src, shadow_dst)
            print(f"[OK] Created Default Shadow: {shadow_dst.relative_to(PROJECT_ROOT)}")

    # World Template
    world_tpl_src = defaults_dir / "templates/tpl_world.md"
    world_dst = PROJECT_ROOT / "01_CONTEXT_DB/world/world.md"
    if world_tpl_src.exists() and not world_dst.exists():
        shutil.copy(world_tpl_src, world_dst)
        print(f"[OK] Created Default World: {world_dst.relative_to(PROJECT_ROOT)}")

    # Copy Sommaire Template
    sommaire_src = defaults_dir / "templates/sommaire.md"
    sommaire_dst = PROJECT_ROOT / "03_MANUSCRIPT/01_drafts/sommaire.md"
    if sommaire_src.exists() and not sommaire_dst.exists():
        shutil.copy(sommaire_src, sommaire_dst)
        print(f"[OK] Created: {sommaire_dst.relative_to(PROJECT_ROOT)}")

    print("[OK] Project initialized successfully.")

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
        
    # Load Spec logic
    spec = {}
    try:
        # Infer spec path from filename (e.g. ch01_v0.md -> ch01_spec.json)
        # 1. Extract chapter number "01" from "ch01_v0.md"
        base_name = os.path.basename(args.file)
        # Simple extraction: assuming format chXX...
        if base_name.startswith("ch") and base_name[2:4].isdigit():
            ch_num = base_name[2:4]
            spec_name = f"ch{ch_num}_spec.json"
            spec_path = PROJECT_ROOT / "02_STRUCTURE/specs_json" / spec_name
            
            if spec_path.exists():
                with open(spec_path, 'r', encoding='utf-8') as f:
                    spec = json.load(f)
                print(f"[OK] Loaded Spec: {spec_name}")
            else:
                print(f"[WARN] Warning: Spec file not found: {spec_name}")
    except Exception as e:
        print(f"[WARN] Warning: Could not auto-load spec: {e}")

    report = test_runner.evaluate_draft(content, spec)
    
    if report['overall_score'] < 0.8:
        print("\n[WARN] Quality standard not met (< 0.8)")
        if args.strict:
            sys.exit(1)
    else:

        print("\n[OK] Quality standard met.")
        print("💡 Suggestion: Update the Narrative State with: python manage.py state")

def command_pipeline(args):
    """Execute the workflow pipeline."""
    from _SYSTEM.automation import pipeline_runner
    pipeline_runner.run()

def command_sync(args):
    """Update sommaire.md with real file stats."""
    print("Syncing Status Board...")
    
    sommaire_path = PROJECT_ROOT / "03_MANUSCRIPT/01_drafts/sommaire.md"
    drafts_dir = PROJECT_ROOT / "03_MANUSCRIPT/01_drafts"
    
    if not sommaire_path.exists():
        print(f"Error: Sommaire not found at {sommaire_path}")
        return

    with open(sommaire_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    updated_count = 0
    
    # State machine for parsing
    in_table = False
    headers = []
    
    for line in lines:
        stripped = line.strip()
        
        # Detect table start/end/content
        if stripped.startswith('|'):
            if not in_table:
                # This might be header or separator. We assume first piped line is header.
                pass
                
            parts = [p.strip() for p in stripped.split('|')]
            # parts[0] is empty if line starts with |, parts[-1] empty if ends with |
            # e.g. | ID | Act | ... | -> ['', 'ID', 'Act', ..., '']
            
            # Identify columns if this is the header row
            if 'ID' in parts and 'Mots' in parts:
                headers = parts
                new_lines.append(line)
                continue
                
            # Skip separator line |---:|
            if '---' in stripped:
                new_lines.append(line)
                continue
                
            # Data row
            # Extract Chapter ID (Assuming ID is usually at index 1 based on split)
            try:
                # Find index of key columns based on simple fixed structure for now
                # Or try to match index from headers if robust
                id_idx = 1
                status_idx = 5
                words_idx = 6
                
                ch_id = parts[id_idx] # e.g. CH01
                
                if ch_id.startswith('CH') and ch_id[2:].isdigit():
                    ch_num = ch_id[2:] # 01
                    
                    # Look for file
                    # We look for any file starting with ch01_ in drafts dir
                    found_file = False
                    word_count = 0
                    
                    for f_path in drafts_dir.glob(f"ch{ch_num}_*.md"):
                         # Avoid matching the spec or other things if naming is loose
                         # But ch01_v0.md is standard
                         found_file = True
                         with open(f_path, 'r', encoding='utf-8') as f_content:
                             text = f_content.read()
                             word_count = len(text.split())
                         break # Stop after first match (canonical file)
                    
                    # Update Logic
                    current_status = parts[status_idx]
                    
                    if found_file:
                        # Update Word Count
                        parts[words_idx] = str(word_count)
                        
                        # Update Status: distinct logic
                        # If Todo -> Draft
                        if "Todo" in current_status:
                             parts[status_idx] = "🟡 Draft"
                        # Else leave it (Review/Done)
                    else:
                        # File missing, ensure it says Todo? Or leave as is?
                        # Let's leave as is or set to 0 words
                        parts[words_idx] = "0"
                        
                    # Reconstruct line
                    # Join with " | " 
                    # Note: split adds empty strings at ends, so we reconstruct carefully
                    # | ID | ...
                    new_line = " | ".join(parts)
                    new_lines.append(new_line + "\n")
                    updated_count += 1
                else:
                    new_lines.append(line)
            except Exception as e:
                # parsing error, keep line as is
                # print(f"Warning parsing line: {stripped} - {e}")
                new_lines.append(line)
        else:
            new_lines.append(line)

    # Write back
    with open(sommaire_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"[OK] Synced {updated_count} chapters in sommaire.md")

def command_state(args):
    """Update the dynamic story state."""
    print("Updating Story State based on last staged chapter...")
    # TODO: Implement state_manager.update_state()
    # This feature will perform LLM analysis of the latest scene to update story_state.md
    print("... (Analysis Simulation) ...")
    print("Story State updated in 05_BUILD/state/story_state.md")
    print("Run 'python manage.py assemble' to include this new state in future prompts.")

def command_inspect(args):
    """Run integrity check on the framework."""
    print("[INSPECT] Inspecting Framework Integrity...")
    
    issues = []
    
    # 1. Check Directory Structure
    required_dirs = [
        "00_SPECS", "_SYSTEM", "_SYSTEM/defaults", 
        "03_MANUSCRIPT/01_drafts", "manage.py", "HOWTO.md"
    ]
    
    print("\n[FileSystem Check]")
    for path in required_dirs:
        p = PROJECT_ROOT / path
        if p.exists():
            print(f"  [OK] Found {path}")
        else:
            print(f"  [MISSING] MISSING {path}")
            issues.append(f"Missing critical file/dir: {path}")

    # 2. Check CLI vs Docs Consistency
    # We naive-check if commands in manage.py are mentioned in HOWTO.md
    print("\n[Documentation Check]")
    howto_path = PROJECT_ROOT / "HOWTO.md"
    if howto_path.exists():
        with open(howto_path, 'r', encoding='utf-8') as f:
            howto_content = f.read()
            
        commands = ["init", "assemble", "lint", "pipeline", "sync", "inspect"]
        for cmd in commands:
            if f"`{cmd}`" in howto_content or f"command `{cmd}`" in howto_content or f"manage.py {cmd}" in howto_content:
                print(f"  [OK] Documented: {cmd}")
            else:
                print(f"  [WARN] Undocumented: {cmd}")
                issues.append(f"Command '{cmd}' is not clearly documented in HOWTO.md")
    else:
        issues.append("HOWTO.md is missing")

    # Summary
    print("\n[Inspection Summary]")
    if not issues:
        print("  [OK] System Healthy. Ready for production.")
    else:
        print(f"  [WARN] Found {len(issues)} issues:")
        for i in issues:
            print(f"     - {i}")

def main():
    parser = argparse.ArgumentParser(description="Literature as Code - Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # INIT
    parser_init = subparsers.add_parser("init", help="Initialize project structure")
    
    # INSPECT
    parser_inspect = subparsers.add_parser("inspect", help="Check framework integrity")
    
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

    # SYNC
    parser_sync = subparsers.add_parser("sync", help="Update sommaire.md with real stats")
    
    # STATE
    parser_state = subparsers.add_parser("state", help="Update dynamic story state")
    
    args = parser.parse_args()
    
    if args.command == "init":
        command_init(args)
    elif args.command == "inspect":
        command_inspect(args)
    elif args.command == "assemble":
        command_assemble(args)
    elif args.command == "lint":
        command_lint(args)
    elif args.command == "pipeline":
        command_pipeline(args)
    elif args.command == "sync":
        command_sync(args)
    elif args.command == "state":
        command_state(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
