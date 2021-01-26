# Levy Decision Lab Online Experiment Boilerplate!

Boilerplate code for generating the foundation of your own online experiment, as well as a setup script which uploads your code to Heroku easily and links it to the PsiTurk experiment. The experiment is setup for jsPsych + PsiTurk MTurk experiments, but the structure PsiTurk uses can easily be repurposed if you don't need MTurk. I'm working on a more concrete non-MTurk pipeline, but that will be helped much more with an actual example of a non-MTurk experiment.

Requires Python 3. You may also need to replace `python` and `pip` in this tutorial with `python3` and `pip3` depending on your system.

## Usage

### Part 1: Generate the boilerplate

1. Clone this repo somewhere on your computer. It doesn't matter where, as the generation script builds the boilerplate experiment folder externally.
```
git clone https://github.com/LevyDecisionNeuroLab/levylab-online-experiments.git
```
2. Install the requirements for the generation script. (Only configparser at the moment).
```
cd /path/to/levylab-online-experiment
pip install -r requirements.txt
```
3. Run the generation walkthrough script!
```
python generation.py
```

You can now navigate with `cd` into wherever you generated the experiment boilerplate and begin development! Run the command `psiturk` to start the PsiTurk CLI (which will manage our server stuff) and then type `server on`. This will run the local dev server on `http://0.0.0.0:22362` through which you can test your experiment. To do so, you need to generate a debug URL as if you are an MTurk worker––this is done by running the command `debug` in the `psiturk` CLI.

### Part 2: Upload the experiment to Heroku
After you're mostly happy with your experiment and want to run it publicly, you're ready to begin with the next step and upload to Heroku. 

1. Navigate into your experiment directory (where `config.txt` is, among the other files) 
```
cd /path/to/my-experiment
```
2. Install the setup script requirements
```
pip install -r internals/setup-requirements.txt
```
3. Run the setup walkthrough script! You'll need to use your Heroku account's API token. You can either create your own account and join the Levy Lab team or you can ask Ruby for the credentials for the Levy Lab account.
```
python internals/setup.py
```

Once you finish with the walkthrough script, you'll be given a URL with which you can access your experiment much like you did locally. This time, however, the codebase it is pulling from is a git remote `heroku/master` you can push to to update production. You can now create publicly accessible MTurk HITs in the local PsiTurk CLI. Just run `psiturk` and then `hit create` (note you do not need to run the local server, HITs are stored on the Amazon MTurk account itself which is common between the local and production/Heroku servers). Refer to the PsiTurk docs for more info about what you can do and the structure of a PsiTurk experiment.

Email evan.kirkiles@yale.edu if you have any questions or suggestions at all!
