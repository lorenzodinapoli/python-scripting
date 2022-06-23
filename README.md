# python-scripting
Quick python scripting projects to play around and deepen python knowledge.

## File Management
> Automation project to automatically move downloaded PDFs, images, and videos to specific folders


Needs of the automation script:
	1. File should be always running 
	2. Script needs to be "listening" to changes in the downloads folder 
	3. Send download to appropriate folder based on file type

Requirements:
	- Python needs to have access to file ["os" library]
	- Do something when a new file appears ["Watchdog" library]

Further improvements:
	- Needs to be running all the time, right now the quick fix is a command line script that reduces the friction.
	- Changing the name to a unique understandable one