#!/usr/bin/env python3
"""
build_chapter.py
Role: Orchestrator
Function: Manages the pipeline (Context -> Draft -> Review).
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# Import local modules
# Import local modules
try:
    import context_assembler
    import test_runner
except ImportError:
    # Fallback for when running from root
    from . import context_assembler, test_runner

def mock_llm_generate(system_prompt: str, user_prompt: str) -> str:
    """
    Simulates an LLM response for testing purposes.
    Replace this with actual API call (Gemini/OpenAI).
    """
    print(f"\n[LLM] System Prompt loaded ({len(system_prompt)} chars).")
    print("[LLM] Generating draft (Simulated)...")
    return """
    The rain lashed against the windowpane. John stared at the glass, his reflection distorted by the water.
    "I can't believe it," he said softly.
    The letter lay on the table. It was a catalyst for change, a disruption of his ordinary world.
    He picked it up. The paper felt heavy. He knew he had to make a choice.
    """

def save_draft(chapter_id: str, content: str, version: str = "v0") -> Path:
    """Saves the generated draft to disk."""
    filename = f"{chapter_id}_{version}.md"
    output_dir = PROJECT_ROOT / "03_MANUSCRIPT/01_drafts"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Draft saved to: {output_path}")
    return output_path

def save_report(chapter_id: str, report: dict, version: str = "v0") -> Path:
    """Saves the build report."""
    filename = f"{chapter_id}_{version}_report.json"
    output_dir = PROJECT_ROOT / "05_BUILD/logs"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
        
    print(f"✓ Report saved to: {output_path}")
    return output_path

def load_system_prompt(prompt_name: str) -> str:
    """Loads a system prompt from the prompts directory."""
    path = PROJECT_ROOT / "_SYSTEM/prompts" / prompt_name
    if not path.exists():
        print(f"⚠ Warning: System prompt not found: {path}")
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def run_pipeline(chapter_id: str, dry_run: bool = False):
    print(f"Starting build for Chapter {chapter_id}...")
    
    # 1. Locate Spec
    spec_path = f"02_STRUCTURE/specs_json/{chapter_id}_spec.json"
    
    try:
        # 2. Load Context
        context_prompt = context_assembler.run(spec_path)
        spec = context_assembler.load_spec(spec_path)
        
        # 3. Load System Prompt
        system_prompt = load_system_prompt("prompt_writer_agent.md")
        
        # 4. Generate Draft
        if dry_run:
            print("[Dry Run] Skipping LLM generation.")
            draft_text = "Dry run placeholder text."
        else:
            draft_text = mock_llm_generate(system_prompt, context_prompt)
            
        # 5. Save Draft
        save_draft(chapter_id, draft_text)
        
        # 6. Run Tests
        report = test_runner.evaluate_draft(draft_text, spec)
        
        # 7. Save Report
        save_report(chapter_id, report)
        
        print("\nBuild Pipeline Complete. 🚀")
        
    except Exception as e:
        print(f"\n❌ Build Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a chapter from spec.")
    parser.add_argument("chapter_id", help="ID of the chapter (e.g., ch01)")
    parser.add_argument("--dry-run", action="store_true", help="Skip LLM generation")
    
    args = parser.parse_args()
    run_pipeline(args.chapter_id, args.dry_run)
