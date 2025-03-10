#!/usr/bin/env python3
#ddev-generated

import os
import re
import sys

def find_env_example_file():
    env_example = os.path.join(os.getcwd(), ".env.example")
    if os.path.isfile(env_example):
        return env_example
    else:
        return None

def update_env_file(env_file):
    try:
        # Read file content
        with open(env_file, 'r') as f:
            content = f.read()

        # Create backup
        backup_file = env_file + ".bak"
        with open(backup_file, 'w') as f:
            f.write(content)

        # Check if OCTANE_SERVER already exists with value frankenphp
        if re.search(r"^OCTANE_SERVER=frankenphp$", content, re.MULTILINE):
            os.remove(backup_file)
            return True

        # Check if OCTANE_SERVER exists with another value
        if re.search(r"^OCTANE_SERVER=", content, re.MULTILINE):
            # Replace existing value
            content = re.sub(r"^OCTANE_SERVER=.*$", "OCTANE_SERVER=frankenphp", content, flags=re.MULTILINE)
        else:
            # Add variable at the end
            if content and not content.endswith("\n"):
                content += "\n"
            content += "OCTANE_SERVER=frankenphp\n"

        # Write updated content
        with open(env_file, 'w') as f:
            f.write(content)

        os.remove(backup_file)
        return True

    except Exception as e:
        if os.path.exists(backup_file):
            os.replace(backup_file, env_file)
        return False

def main():
    os.chdir('/app')

    env_file = find_env_example_file()
    if not env_file:
        sys.exit(1)

    if not update_env_file(env_file):
        sys.exit(1)

if __name__ == "__main__":
    main()