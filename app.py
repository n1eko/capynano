from fastai.vision.all import *
from fastbook import *
import gradio as gr
import pathlib

# Solution to make it work on Linux 
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

learn = load_learner('capynano-model.pkl', cpu=True)

title = "Welcome on your first sketch recognition app!"
head = (
  "<center>"
  "<img src='file/drivingcapy.jpg' width=400>"
  "The robot was trained to diff between capybaras and el nano. To test it, upload your image."
  "</center>"
)

categories = ('El nano', 'Capibara')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label()
examples = ['capy.jpg','nano.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, examples=examples, outputs=label, title=title, description=head)
intf.launch(inline=False, server_name="0.0.0.0", server_port=8080)