from colorthief import ColorThief
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from PIL import Image, ImageFont, ImageDraw, ImageTk
from werkzeug.utils import secure_filename
import os

# color_thief = ColorThief('sample.jpg')
# # get the dominant color
# dominant_color = color_thief.get_color(quality=1)
# # build a color palette
# palette = color_thief.get_palette(color_count=11)
# print(palette)

UPLOAD_FOLDER = '/Users/maxwellwhite/Documents/PythonPractice/Final_Projects/color_pallete_generator/static/uploads/1.png'

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def all_tasks():
    color_thief = ColorThief(UPLOAD_FOLDER)
    # build a color palette
    palette = color_thief.get_palette(color_count=11)
    return render_template("index.html", palette=palette, hex=hex)

@app.route("/imagesubmit", methods=['GET', 'POST'])
def imagesubmit():
    if request.method == 'POST':
        file_from = request.files['file']
        file = Image.open(file_from)
        file.save(UPLOAD_FOLDER)
        return redirect(url_for('all_tasks'))

if __name__ == "__main__":
    app.run(debug=True, port=5002)