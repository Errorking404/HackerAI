import sys, os, platform, importlib.util

arch = platform.machine()

if arch == 'aarch64':
    so_path = os.path.join(os.path.dirname(__file__), 'bin/hacker_64.so')
elif arch in ['armv7l', 'armv8l']:
    so_path = os.path.join(os.path.dirname(__file__), 'bin/hacker_32.so')
else:
    raise ImportError(f"Unsupported Termux arch: {arch}")

spec = importlib.util.spec_from_file_location(
    "hacker_core_encoded",
    so_path
)

hacker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hacker)

sys.modules['hacker'] = hacker
