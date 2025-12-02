#!/usr/bin/env python3
"""
context_assembler.py
Role: RAG Primitive
Function: Reads a JSON Chapter Spec and fetches the content of referenced files.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).parent.parent.parent


def load_spec(spec_path: str) -> Dict:
    """
    Parses the JSON spec file.
    
    Args:
        spec_path: Path to the JSON chapter spec file
        
    Returns:
        Dictionary containing the parsed spec
        
    Raises:
        FileNotFoundError: If spec file doesn't exist
        json.JSONDecodeError: If spec file is invalid JSON
    """
    full_path = PROJECT_ROOT / spec_path
    
    if not full_path.exists():
        raise FileNotFoundError(f"Spec file not found: {full_path}")
    
    with open(full_path, 'r', encoding='utf-8') as f:
        spec = json.load(f)
    
    print(f"✓ Loaded spec: {spec.get('chapter_id', 'unknown')}")
    return spec


def fetch_context(context_paths: List[str]) -> Dict[str, str]:
    """
    Reads the content of each file in the list.
    
    Args:
        context_paths: List of relative file paths from project root
        
    Returns:
        Dictionary mapping file paths to their contents
    """
    context_content = {}
    
    for path in context_paths:
        full_path = PROJECT_ROOT / path
        
        if not full_path.exists():
            print(f"⚠ Warning: File not found: {path}")
            context_content[path] = f"[FILE NOT FOUND: {path}]"
            continue
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                context_content[path] = content
                print(f"✓ Loaded: {path} ({len(content)} chars)")
        except Exception as e:
            print(f"✗ Error reading {path}: {e}")
            context_content[path] = f"[ERROR: {e}]"
    
    return context_content


def assemble_prompt(spec: Dict, context_content: Dict[str, str]) -> str:
    """
    Combines spec and context into a single prompt for the LLM.
    
    Args:
        spec: The chapter specification
        context_content: Dictionary of file contents
        
    Returns:
        Formatted prompt string ready for LLM
    """
    prompt_parts = []
    
    # Header
    prompt_parts.append("# CONTEXT ASSEMBLY FOR CHAPTER GENERATION\n")
    
    # Spec Summary
    prompt_parts.append("## CHAPTER SPECIFICATION")
    prompt_parts.append(f"ID: {spec.get('chapter_id')}")
    prompt_parts.append(f"Title: {spec.get('title')}")
    prompt_parts.append(f"Act: {spec.get('act')}")
    prompt_parts.append(f"Beat: {spec.get('beat')}")
    prompt_parts.append(f"Narrative Goal: {spec.get('narrative_goal')}")
    prompt_parts.append(f"Emotional Beat: {spec.get('emotional_beat')}\n")
    
    # Context Files
    prompt_parts.append("## LOADED CONTEXT\n")
    
    for path, content in context_content.items():
        prompt_parts.append(f"### [{path}]")
        prompt_parts.append(content)
        prompt_parts.append("")
    
    # Constraints
    if 'constraints' in spec:
        prompt_parts.append("## CONSTRAINTS")
        for key, value in spec['constraints'].items():
            prompt_parts.append(f"- {key}: {value}")
        prompt_parts.append("")
    
    return "\n".join(prompt_parts)


def run(spec_path: str, output_file: Optional[str] = None) -> str:
    """
    Main execution function.
    
    Args:
        spec_path: Path to the JSON spec file
        output_file: Optional path to save assembled context
        
    Returns:
        The assembled prompt string
    """
    print("=" * 60)
    print("CONTEXT ASSEMBLER - Starting")
    print("=" * 60)
    
    # Load spec
    spec = load_spec(spec_path)
    
    # Extract context paths from spec
    # For now, we look for characters in required_characters
    context_paths = []
    
    if 'required_characters' in spec:
        for char_id in spec['required_characters']:
            context_paths.append(f"01_CONTEXT_DB/characters/{char_id}.md")
    
    if 'settings' in spec:
        for setting in spec['settings']:
            loc_id = setting.get('location_id')
            if loc_id:
                context_paths.append(f"01_CONTEXT_DB/world/{loc_id}.md")
    
    print(f"\nFetching {len(context_paths)} context files...")
    
    # Fetch context
    context_content = fetch_context(context_paths)
    
    # Assemble prompt
    prompt = assemble_prompt(spec, context_content)
    
    # Save if requested
    if output_file:
        output_path = PROJECT_ROOT / output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(prompt)
        print(f"\n✓ Context saved to: {output_file}")
    
    print("=" * 60)
    print(f"Total context size: {len(prompt)} characters")
    print("=" * 60)
    
    return prompt


if __name__ == "__main__":
    # Example usage
    result = run(
        "02_ARCHITECTURE/specs_json/ch01_spec.json",
        "05_BUILD/logs/ch01_context.txt"
    )
    print("\nContext assembly complete.")
