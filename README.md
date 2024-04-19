# Remove Audio From Videos In All Subfolders
The script "RemoveAudioFromAllVideos.py" removes the Audio from all videos found in the directory and all subfolders. 
It ignores all previously processed files. 

> :warning: **IMPORTANT:** Before use, you need to change the base directory according to your needs! <br/>
If you want a Video in the selcted directorys to be excluded, add the prefix "WA_" (with Audio) to the file name.

## The process of the script
	1. Look for all Videos in directory and subfolders (Not starting with "WOA_" (Without Audio) and "WA_" (with Audio)
	2. If Videos are found:
	   - convert video to .mp4
	   - remove audio
	   - create new file (With Prefix "WOA_" (Without Audio))
	   - remove old file
	3. Display count of processed videos.




## My personal use case
In addition to my other roles, I work as a sailing coach and frequently capture videos of sailors in action. 
This provides them with visual feedback to complement the skills they're learning. 
However, due to factors such as wind, water, fluttering sails, and large distances, I often need to raise my voice for the sailors to hear me.
Holding the camera close can create the impression that I'm shouting at them. 
To avoid this and protect both my privacy and that of the participants, I remove the audio from the videos. 
I have integrated a script into our shared folder that allows me to trigger this process repeatedly, ensuring that already processed videos are not altered again.
