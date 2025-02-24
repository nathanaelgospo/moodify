"""from flask import Flask, render_template, url_for, redirect, request
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
files_in_upload_folder = os.listdir(UPLOAD_FOLDER)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form", methods=["POST", "GET"])
def formRetrieval():
    if request.method == "POST":
        # Retrieve the song name from the form
        song = request.form.get("song")
        # Process the song (example function, you may need to adjust)
        url = processData(song)

        # Handle file upload
        file = request.files.get("file")  # Assuming the file input field is named "file"
        
        if file and allowed_file(file.filename):  # Check if file is valid
            # Save the file to the upload folder
            filename = secure_filename(file.filename)
            print("lard" + filename)
            files_only = [f for f in files_in_upload_folder if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
            #rename the file to file + number of files
            num_files = len(files_only)
            filename = "file" + str(num_files) + ".mp3"
            print("lard" + filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Redirect to results page with the song URL and file path
            return redirect(url_for("results", song=url, mp3=filename))

        # If no valid file was uploaded, handle here (maybe flash a message)
        return redirect(url_for("results", song=url, mp3="no MP3 file"))


# Example processing function (you might want to adjust it)
def processData(song):
    return "url"


# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




# Define the results route
@app.route('/results')
def results():
    song_url = request.args.get("song")
    mp3_filename = request.args.get("mp3")
    return render_template('results.html', song=song_url, mp3=mp3_filename)



# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if __name__ == "__main__":
    app.run(debug=True)
"""