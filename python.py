# -------------------------------------------------------------
# Using Rpy2
# -------------------------------------------------------------

# activate numpy->Robject conversion
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()

# import interpreter
import rpy2.robjects as robjects
R=robjects.r

# import graphics device
from rpy2.robjects.packages import importr
grdevices = importr('grDevices')

grdevices.X11()

# ... plotting

grdevices.dev_off()

# -------------------------------------------------------------
# Multi-Page pdf plot with matplotlib
# -------------------------------------------------------------

from matplotlib.backends.backend_pdf import PdfPages # multi-page plot
figfile=os.path.join("pics",os.path.basename(dbname)+".pdf")
print(">> saving to '%s'"%figfile)
pp = PdfPages(figfile)

# pl.plot(...)

pp.savefig() # per figure

pp.close()

# -------------------------------------------------------------
# long title, guaranteed to fit w matplotlib
# -------------------------------------------------------------

from textwrap import wrap
titlab=("\n".join(wrap(os.path.basename(dbname),width=70)))
pl.title(titlab, fontsize='x-small')

# -------------------------------------------------------------
# small paramstring function
# -------------------------------------------------------------
def paramstring( **kwargs ):
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]+"_" \
           +"_".join(["%s=%s"%(str(k),str(kwargs[k])) for k in kwargs.keys()])


# -------------------------------------------------------------
# method for convenient parameter handling
# -------------------------------------------------------------

# set everything in a string in python syntax
par_s="""
n=500
alpha=2.0
nbatches=1000
mu=.99
eta=.0002
tau_m=0.010
tau_s=tau_m/4.
lmax=50000
"""

# eval' it into a dict
pars={}
exec(par_s,{},pars)

# parse cmd-line and overwrite dict
for arg in sys.argv[1:]:
    k,v=arg.split('=')
    print(">> cmdline: found %s=%s"%(k,v))
    pars[k]=eval(v)

# put everything in the local namespace
print(pars)
locals().update(pars)
