from helpers import copytree
import configparser
import shutil
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def generate():
    """ Runs through the scripts to generate an experiment's base files """

    print(color.BOLD + "\n - [STEP 1/2] Building experiment file structure - " + color.END)

    print(color.BOLD + "\nGenerating online experiment boilerplate..." + color.END)
    path = input("Path in which to build experiment folder: " + color.PURPLE)
    folder = input(color.END + "Name of experiment folder (leave blank to not encapsulate in folder): " + color.PURPLE)

    try:

        # Copy over the src directory into the tmp directory
        os.makedirs(os.path.dirname('tmp/'), exist_ok=True)
        copytree('src/', 'tmp/')

        # Build temporary files in tmp
        build_config()

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

        print(color.GREEN + color.BOLD + '\nFINISHED! ' + color.END + 'Built experiment boilerplate at ' + color.GREEN + experimentpath + color.END + '\n')

    finally:
        if os.path.exists('tmp/') and os.path.isdir('tmp/'):
            shutil.rmtree('./tmp/')

    

def build_config():
    """ Writes the new config into the tmp folder """
    c = configparser.ConfigParser()
    c.read('tmp/config.txt')

    print(color.END + color.BOLD + "\n - [STEP 2/2] Building config.txt - " + color.END)

    # Experiment configuration
    print(color.END + color.BOLD + "\nConfiguring experiment metadata..." + color.END)
    title = input("Experiment title: " + color.PURPLE)
    description = input(color.END + "Experiment description: " + color.PURPLE)
    amt_keywords = input(color.END + "Mechanical turk keywords: " + color.PURPLE)
    c['HIT Configuration']['title'] = title
    c['HIT Configuration']['description'] = description
    c['HIT Configuration']['amt_keywords'] = amt_keywords

    # Experiment admin configuration
    print(color.END + color.BOLD + "\nConfiguring experiment user metadata..." + color.END)
    email = input("Contact email on error: " + color.PURPLE )
    username = input(color.END + "Website admin username: " + color.PURPLE)
    password = input(color.END + "Website admin password: " + color.PURPLE)
    c['HIT Configuration']['email_on_error'] = email
    c['Server Parameters']['login_username'] = username
    c['Server Parameters']['login_pw'] = password

    with open('tmp/config.txt', 'w') as out:
        c.write(out)


if __name__ == "__main__":
    generate()