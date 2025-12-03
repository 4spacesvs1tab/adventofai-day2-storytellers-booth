#!/usr/bin/env python3
"""
Test script to verify all fortune teller functionalities work correctly.
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def test_help():
    """Test help command."""
    print("Testing help command...")
    code, stdout, stderr = run_command("python3 fortune_teller/main.py --help")
    if code == 0 and "Madame Zelda's Winter Fortune Teller" in stdout:
        print("✅ Help command works correctly")
        return True
    else:
        print("❌ Help command failed")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False

def test_list():
    """Test list personalities command."""
    print("Testing list personalities command...")
    code, stdout, stderr = run_command("python3 fortune_teller/main.py --list")
    if code == 0 and "Mysterious" in stdout and "Festive" in stdout:
        print("✅ List personalities command works correctly")
        return True
    else:
        print("❌ List personalities command failed")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False

def test_random_fortune():
    """Test generating a random fortune."""
    print("Testing random fortune generation...")
    code, stdout, stderr = run_command("python3 fortune_teller/main.py")
    if code == 0 and "whispers" in stdout and "Radiation Levels" in stdout:
        print("✅ Random fortune generation works correctly")
        return True
    else:
        print("❌ Random fortune generation failed")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False

def test_specific_personality():
    """Test generating a fortune with specific personality."""
    print("Testing specific personality fortune generation...")
    code, stdout, stderr = run_command("python3 fortune_teller/main.py --personality mysterious")
    if code == 0 and "Mysterious Morgan" in stdout and "Radiation Levels" in stdout:
        print("✅ Specific personality fortune generation works correctly")
        return True
    else:
        print("❌ Specific personality fortune generation failed")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False

def test_multiple_fortunes():
    """Test generating multiple fortunes."""
    print("Testing multiple fortune generation...")
    code, stdout, stderr = run_command("python3 fortune_teller/main.py --number 2")
    if code == 0 and stdout.count("whispers") == 2 and stdout.count("Radiation Levels") == 2:
        print("✅ Multiple fortune generation works correctly")
        return True
    else:
        print("❌ Multiple fortune generation failed")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False

def test_invalid_personality():
    """Test handling of invalid personality."""
    print("Testing invalid personality handling...")
    code, stdout, stderr = run_command("python3 fortune_teller/main.py --personality invalid")
    # Argparse returns exit code 2 for invalid choices
    if code == 2 and "invalid choice" in stderr:
        print("✅ Invalid personality handling works correctly")
        return True
    else:
        print("❌ Invalid personality handling failed")
        print(f"Exit code: {code}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False

def main():
    """Run all tests."""
    print("Running Fortune Teller CLI Tests\n")
    
    tests = [
        test_help,
        test_list,
        test_random_fortune,
        test_specific_personality,
        test_multiple_fortunes,
        test_invalid_personality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Tests completed: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
