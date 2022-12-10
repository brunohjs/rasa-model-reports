# This script is responsable for launching new app releases.
import logging
import subprocess
import sys


logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
MAIN_BRANCH = "main"


def get_version():
    logging.info("Getting last version")
    subprocess.run(["git", "fetch", "--all"], shell=False)
    versions = subprocess.check_output(["git", "tag"]).decode('ascii').strip().split('\n')
    version = versions[-1] if versions and versions[0] else 'v0.0.0'
    logging.info(f"Last version: {version}")
    version = version.replace('v', '').split('.')
    if len(sys.argv) > 1:
        if sys.argv[1] == "major":
            version[0] = str(int(version[0]) + 1)
            version[1] = "0"
            version[2] = "0"
        elif sys.argv[1] == "minor":
            version[1] = str(int(version[1]) + 1)
            version[2] = "0"
        elif sys.argv[1] == "path":
            version[2] = str(int(version[2]) + 1)
        logging.info(f"New version {sys.argv[1]}")
    else:
        version[2] = str(int(version[2]) + 1)
        logging.info("New path version")
    version = ".".join(version)
    logging.info(f"New version: {version}")
    return version


def release(version):
    branch_name = subprocess.check_output(["git", "branch", "--show-current"]).decode('ascii')
    logging.info(f"Current branch: {branch_name}")
    if branch_name != MAIN_BRANCH:
        logging.info(f"Switching to branch {MAIN_BRANCH}")
        subprocess.run(["git", "checkout", MAIN_BRANCH], shell=True)
    logging.info(f"Updating branch {MAIN_BRANCH}")
    subprocess.run(["git", "pull"], shell=True)
    logging.info("Updating package.json file")
    # json_file = json.load(open("package.json"))
    # json_file["version"] = version
    # json.dump(json_file, open("package.json", "w"), indent=2)
    # logging.info("Commitando atualização")
    # subprocess.run(["git", "add", "package.json"], shell=True)
    # subprocess.run(["git", "commit", "-m", f"Nova versão lançada {version}"], shell=True)
    # subprocess.run(["git", "push"], shell=True)
    # logging.info("Commitando tag")
    # subprocess.run(["git", "tag", f"{version}"], shell=True)
    # subprocess.run(["git", "push", "--tags"])
    logging.info(f"Finished process. New version {version}")


if __name__ == "__main__":
    version = get_version()
    release(version)
