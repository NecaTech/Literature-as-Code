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
            
    # 2. Check for agent/LLM (mocked for now)
    elif 'agent' in step:
        print(f"  (Mock) Agent '{step.get('agent')}' logic not implemented yet.")
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
        success = run_step(step)
        if not success:
            print("\nPipeline stopped due to error.")
            break
            
    print("\n" + "=" * 60)
    print("Pipeline Execution Finished")
    print("=" * 60)
