
VERSION_DATE = "2026.10.08 (c)"

print( "* pyprover9 by Brandon Bennett" )
print( "* a Colab front-end for Prover9 by William McCune")
print( "  Created September 2023 " )
print( "  This version date:", VERSION_DATE )
print()
print( """Provides:
  pyprover9.prove( assumptions, goal )
  pyprover9.input( p9inputString )
  pyprover9.full_output()
  pyprover9.p9file( assumptions, goal )
  pyprover9.p9download( assumptions, goal )
  pyprover9.template( "probset/probname.p9" )
  pyprover9.editor( problem="probset/probname.p9", savefile="save.p9")
""" )

print("""Tutorial Notebooks:
  KRR_Taster.ipynb : https://colab.research.google.com/drive/1ffDxgVh3nc7aV13u25JYF1iJSSxrlM-1
  This is an easy introduction to Knowledge Representation and Reasoning using Prover9.
  It it includes several problem examples for you to code up and solve using the prover.

  KRR_with_Prover9.ipynb : https://colab.research.google.com/drive/1RkO7JVpYvd3TxALJNBgE1N69WZ21X8Ej
  Another introducton with slightly more advanced examples and illustration of functions provided by pyprover9. 
""")

from .pyprover9 import prove, input, full_output, p9file
from .show_html import get_problem, display_problem_html

import os

def template(fname):
    d = os.path.dirname(__file__)
    respath = os.path.join( d, "problems", fname )
    with open( respath ) as f:
        content = f.read()
    return content


try:
    from google.colab import files as colab_files
except ImportError:
    colab_files = None

try:
    from IPython.display import FileLink, display
except ImportError:
    FileLink = None
    display = None


def p9download(assumptions, goal, fname, template=None):
    content = p9file(assumptions, goal, template=template)

    os.makedirs("tmp", exist_ok=True)

    if not fname.endswith(".p9"):
        fname += ".p9"

    path = os.path.join("tmp", fname)

    with open(path, "w") as f:
        f.write(content)

    if colab_files is not None:
        colab_files.download(path)
        return

    if FileLink is not None and display is not None:
        link = FileLink(path, result_html_prefix="Download Prover9 file: ")
        display(link)
        return

    print(f"Prover9 file written to: {path}")

#def p9download( assumptions, goal, fname, template = None ):
#    content = p9file( assumptions, goal, template=template )
#    if not os.path.exists('tmp'):
#        os.makedirs('tmp')
#    if not fname.endswith('.p9'):
#      fname += ".p9"
#    path = os.path.join( 'tmp', fname )
#    with open( path, "w") as f:
#          f.write(content)
#    colab.files.download(path)

try:
   import ipywidgets as widgets
except ImportError:
   widgets = None

def editor(problem=None,savefile=None):
    if widgets == None:
        print("!!! Cannot run editor --- requires ipywidgets to be imported.")
        return

    if problem:
      if not problem.endswith('.p9'):
        problem += ".p9"
      p9input = template(problem)
      if not savefile:
        savefile = os.path.basename(problem)
    else:
      p9input = "%% Enter p9 input file content"
      if not savefile: savefile = "save.p9"

    layout  = widgets.Layout(flex='0 1 auto', height='500px', min_height='200px', width='auto')
    textbox = widgets.Textarea( value=p9input, layout=layout )
    run  = widgets.Button(description="Run Prover9")
    save = widgets.Button(description="Save")
    def runP9ontext(click):
      input(textbox.value)

    # def saveP9(click):
    #   with open( savefile, 'w') as f:
    #     f.write(textbox.value)
    #   colab.files.download(savefile)

    def saveP9(click):
      with open(savefile, "w") as f:
        f.write(textbox.value)

      if colab_files is not None:
        colab_files.download(savefile)
      elif FileLink is not None and display is not None:
        display(FileLink(
          savefile,
          result_html_prefix="Download Prover9 file: "
        ))
      else:
        print(f"Prover9 file written to: {savefile}")

    run.on_click(runP9ontext)
    save.on_click(saveP9)
    buttons = widgets.HBox([run, save])
    vb = widgets.VBox([textbox, buttons])
    display(vb)
