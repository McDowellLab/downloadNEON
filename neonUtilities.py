import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import warnings
from rpy2.rinterface import RRuntimeWarning
warnings.filterwarnings("ignore", category=RRuntimeWarning)

base = importr('base')
utils = importr('utils')
stats = importr('stats')
utils.install_packages('devtools')
devtools = importr('devtools')
devtools.install_github('NEONScience/NEON-utilities/neonUtilities')
neonUtils = importr('neonUtilities')