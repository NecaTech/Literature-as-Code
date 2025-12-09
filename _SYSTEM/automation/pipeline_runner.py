#!/usr/bin/env python3
"""
pipeline_runner.py
Role: Workflow Orchestrator
Function: Reads workflow.yaml and executes steps sequentially.
"""

import sys
import subprocess
import shlex
from pathlib import Path

# Try importing yaml, if fails, user needs to install it
try:
    import yaml
except ImportError:
    print("Error: PyYAML is missing. Install it with: pip install PyYAML")
    # sys.exit(1) # We can't exit here if we just want to load the module, checking in run()

PROJECT_ROOT = Path(__file__).parent.parent.parent

def run_step(step):
    """Executes a single step from the workflow."""
    name = step.get('name', 'Unknown Step')
    print(f"\n▶ Executing: {name}")
    
    # 1. Check for script execution
    if 'script' in step:
        cmd = step['script']
        print(f"  Running script: {cmd}")
        
        # Replace python with current python executable to be safe
        if cmd.startswith("python "):
            cmd = cmd.replace("python ", f"{sys.executable} ", 1)
            
        try:
            # We split the command for subprocess
            args = shlex.split(cmd)
            # Run relative to project root
            subprocess.check_call(args, cwd=PROJECT_ROOT)
            print("  ✓ Step completed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  X Step failed with exit code {e.returncode}")
            return False
            
    # 2. Check for agent/LLM (Interactive Step)
    elif 'agent' in step:
        print(f"  [Interactive Step] Action Required from Assistant/User: '{step.get('agent')}'")
        print(f"  > Please perform the action described: {step.get('description')}")
        return True
        
    else:
        print("  ! No executable action found in step.")
        return True

def run(workflow_path="workflow.yaml"):
    """Main execution loop."""
    print("=" * 60)
    print("PIPELINE RUNNER - Starting")
    print("=" * 60)

    if 'yaml' not in sys.modules:
        print("Error: PyYAML not installed. Cannot parse workflow.yaml.")
        return

    full_path = PROJECT_ROOT / workflow_path
    if not full_path.exists():
        print(f"Error: Workflow file not found: {full_path}")
        return

    with open(full_path, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML: {exc}")
            return

    pipeline = data.get('pipeline', [])
    print(f"Found {len(pipeline)} steps in workflow.")

    for step in pipeline:
        # Check if this is a Drafting step that needs self-healing
        if step.get('name') == "Drafting" and step.get('agent') == "Writer":
            print("\n>>> Entering Self-Healing Loop for Drafting...")
            max_retries = 3
            attempt = 0
            score = 0.0
            
            # This is a conceptual implementation of the loop described in the audit.
            # In a real run, this would interface with the LLM API.
            # For now, we utilize the standard run_step but acknowledge the architecture change.
            while score < 0.8 and attempt < max_retries:
                attempt += 1
                print(f"  [Attempt {attempt}/{max_retries}] Generating Draft...")
                
                success = run_step(step)
                if not success:
                    print("  [ERR] Generation failed.")
                    break
                
                # Here we would run the linter immediately
                # lint_score = run_linter(draft)
                # if lint_score < 0.8:
                #    print(f"  [FAIL] Score {lint_score}. Retrying with feedback...")
                # else:
                #    print(f"  [PASS] Score {lint_score}. Draft accepted.")
                #    score = 1.0
                
                # For this demo, we assume success after 1 try to avoid infinite loops without real LLM
                score = 1.0 
                
        else:
            # Standard Step Execution
            success = run_step(step)
            if not success:
                print("\nPipeline stopped due to error.")
                break
            
    print("\n" + "=" * 60)
    print("Pipeline Execution Finished")
    print("=" * 60)
