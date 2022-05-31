from os.path import join, dirname
from dotenv import load_dotenv
def load_env():
    print("Loading environment")
    dotenv_path = join(dirname(__file__), 'sample.envs')
    load_dotenv(dotenv_path)