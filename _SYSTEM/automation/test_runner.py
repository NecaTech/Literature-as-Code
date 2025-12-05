#!/usr/bin/env python3
"""
test_runner.py
Role: QA Engineer (LLM-as-a-judge)
Function: Evaluates a draft against defined criteria (Linting Rules & Unit Tests).
"""

import json
import os
import sys
import importlib.util
from pathlib import Path
from typing import Dict, List, Any

# Add project root to path to allow imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

def load_linting_rules(rules_dir: Path) -> List[Dict]:
    """Loads all JSON linting rules from the directory."""
    rules = []
    if not rules_dir.exists():
        print(f"⚠ Warning: Linting rules directory not found: {rules_dir}")
        return rules
        
    for file_path in rules_dir.glob("*.json"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                rule = json.load(f)
                rules.append(rule)
                print(f"✓ Loaded rule: {rule.get('name', 'Unknown')}")
        except Exception as e:
            print(f"✗ Error loading rule {file_path}: {e}")
    return rules

def run_linting(draft_text: str, rules: List[Dict]) -> Dict[str, Any]:
    """Applies simple regex/keyword based linting rules."""
    lint_results = {
        "score": 1.0,
        "issues": []
    }
    
    total_issues = 0
    
    for rule in rules:
        patterns = rule.get("patterns", [])
        rule_issues = 0
        
        for pattern in patterns:
            # Simple case-insensitive string match for now
            # Could be upgraded to Regex
            count = draft_text.lower().count(pattern.lower())
            if count > 0:
                rule_issues += count
                lint_results["issues"].append({
                    "rule": rule["name"],
                    "pattern": pattern,
                    "count": count,
                    "message": rule["message"]
                })
        
        total_issues += rule_issues

    # Simple scoring logic: -0.05 per issue, min 0
    lint_results["score"] = max(0.0, 1.0 - (total_issues * 0.05))
    return lint_results

def run_unit_tests(draft_text: str, spec: Dict, tests_dir: Path) -> List[Dict]:
    """Dynamically loads and runs python unit tests."""
    results = []
    
    if not tests_dir.exists():
        print(f"⚠ Warning: Unit tests directory not found: {tests_dir}")
        return results

    for file_path in tests_dir.glob("test_*.py"):
        try:
            # Dynamic import
            spec_loader = importlib.util.spec_from_file_location(file_path.stem, file_path)
            module = importlib.util.module_from_spec(spec_loader)
            spec_loader.loader.exec_module(module)
            
            if hasattr(module, "run_test"):
                print(f"Running test: {file_path.stem}...")
                test_result = module.run_test(draft_text, spec)
                results.append(test_result)
            
        except Exception as e:
            print(f"✗ Error running test {file_path}: {e}")
            results.append({
                "test_name": file_path.stem,
                "passed": False,
                "score": 0.0,
                "details": f"Exception: {e}"
            })
            
    return results

def evaluate_draft(draft_text: str, spec: Dict) -> Dict:
    """
    Main entry point for evaluation.
    """
    print("\n" + "="*40)
    print("TEST RUNNER - Starting Evaluation")
    print("="*40)
    
    # 1. Linting
    rules_dir = PROJECT_ROOT / "04_TESTS/linting_rules"
    rules = load_linting_rules(rules_dir)
    lint_report = run_linting(draft_text, rules)
    
    # 2. Unit Tests
    tests_dir = PROJECT_ROOT / "04_TESTS/unit_tests"
    unit_test_report = run_unit_tests(draft_text, spec, tests_dir)
    
    # 3. Aggregate Results
    report = {
        "linting": lint_report,
        "unit_tests": unit_test_report,
        "overall_score": 0.0
    }
    
    # Calculate overall score (50% linting, 50% unit tests)
    unit_test_avg = 0.0
    if unit_test_report:
        unit_test_avg = sum(t["score"] for t in unit_test_report) / len(unit_test_report)
        
    report["overall_score"] = (lint_report["score"] * 0.5) + (unit_test_avg * 0.5)
    
    print("\n" + "-"*40)
    print(f"EVALUATION COMPLETE")
    print(f"Overall Score: {report['overall_score']:.2f}/1.0")
    print(f"Linting Issues: {len(lint_report['issues'])}")
    print(f"Unit Tests Passed: {sum(1 for t in unit_test_report if t['passed'])}/{len(unit_test_report)}")
    print("-"*40 + "\n")
    
    return report

if __name__ == "__main__":
    # Test run
    dummy_spec = {"narrative_goal": "Survive", "emotional_beat": "Fear"}
    dummy_draft = "He felt sad. He said loudly, 'Why?'"
    evaluate_draft(dummy_draft, dummy_spec)
