import sys
import subprocess

# parser = argparse.ArgumentParser(description='Run danila-miner.')

args = sys.argv[1:] 

danila_args_idx = -1

for a in args:
    if not a[0].isupper():
        danila_args_idx = args.index(a)
        break

print("OCMonitor args:")
print(args[:danila_args_idx])

print("Echoing other args:")
subprocess.run(["danila-miner"] + args[danila_args_idx:])


