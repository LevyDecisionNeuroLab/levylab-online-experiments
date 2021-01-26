from helpers import copytree
import configparser
import shutil
import os

def generate():
    """ Runs through the scripts to generate an experiment's base files """

    # TODO: Copy src folder into a tmp folder

    print("\nGenerating online experiment boilerplate...")
    path = input("Path in which to build experiment folder: ")
    folder = input("Name of experiment folder (leave blank to not encapsulate in folder): ")

    try:

        # Copy over the src directory into the tmp directory
        os.makedirs(os.path.dirname('tmp/'), exist_ok=True)
        copytree('src/', 'tmp/')

        # Build temporary files in tmp
        # build_config()

        # Copy tmp folder to desired directory with new name
        fullpath = os.path.abspath(path.strip())
        experimentpath = None
        if not folder:
            experimentpath = fullpath
            copytree('tmp/', experimentpath)
        else:
            experimentpath = os.path.join(fullpath, folder)
            if os.path.exists(experimentpath) and os.path.isdir(experimentpath):
                shutil.rmtree(experimentpath)
            os.makedirs(experimentpath, exist_ok=True)
        copytree('tmp/', experimentpath)

    finally:
        if os.path.exists('tmp/') and os.path.isdir('tmp/'):
            shutil.rmtree('./tmp/')

    

def build_config():
    """ Writes the new config into the tmp folder """
    c = configparser.ConfigParser()
    c.read('tmp/config.txt')

    print("\n - STEP 2: Building config.txt - ")

    # Experiment configuration
    print("\nConfiguring experiment metadata...")
    title = input("Experiment title: ")
    description = input("Experiment description: ")
    amt_keywords = input("Mechanical turk keywords: ")
    c['HIT Configuration']['title'] = title
    c['HIT Configuration']['description'] = description
    c['HIT Configuration']['amt_keywords'] = amt_keywords

    # Experiment admin configuration
    print("\nConfiguring experiment user metadata...")
    email = input("Contact email on error: ")
    username = input("Website admin username: ")
    password = input("Website admin password: ")
    c['HIT Configuration']['email_on_error'] = email
    c['Server Parameters']['login_username'] = username
    c['Server Parameters']['login_pw'] = password

    with open('tmp/config.txt', 'w') as out:
        c.write(out)


if __name__ == "__main__":
    generate()