"""
Small utility helpers used by backend.
"""
import os


def project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def read_env():
    env = {}
    env_path = os.path.join(project_root(), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip().strip('"')
    return env
