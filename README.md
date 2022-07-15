# Meme-Generator
Python server and website using Flask and Handlebars templating.

Udacity sourced project as part of a nano-degree in Intermediate Python, utilising a Python backend with Bootstrap templating the HTML.

As part of the Udacity nano-degree in Python, I have created a web-based application that both creates random canine-based motivational memes, and allows the user to develop their own.

To get the app up and running, please install its requirements from the eponymous file by running

pip install -r requirements.txt

As part of the project, the command line utility using the app 'Xpdfreader' has been worked into the code as a subprocess method. To allow this to run, please download this app from https://www.xpdfreader.com/download.html and, if you are using Windows, set your system PATH variable to search for it using the environment commands in your Control Panel.

The entry point for the code is to run the command:

python app.py

The running application is viewable on Flask's (a requirement) internal server at http://127.0.0.1:5000/

Thanks for taking the time to read this, any feedback greatly appreciated.

Toby

ps, I have seen this code-base working on a Linux system, but have had a real issue with paths on my home Windows computer (using Visual Studio Community 2019). The issue for this is the subprocess command, which is seeking the XPDFReader, from the PDFImporter file. It is unable to find it, giving a 'FileNotFoundError: [WinError2]' message. I have set the environment path under the Control Panel to the folder in which the downloaded PDF reader is saved and even added the same reader to the paths used to run the installed Python files. It still isn't being picked up. Any help with this would be greatly appreciated.

Thanks,

Toby

Update - 

After further research, I have downloaded the Windows Command Line tool from XPDFReader and placed its pdftotext.exe file (from binaries) on the path, and the app is now working.

![](Meme-generator%20images/working.app.py)



