Utility to convert most image/video formats to the format needed to add stickers via https://t.me/Stickers bot in Telegram.

At the beginning of the script execution, it asks the user for a name for the subfolder to be created inside the "result" directory. In this subfolder the results of processing will be saved. Next, the script checks the first file in the "data" directory and determines whether the file is supported for one of two types of processing: static or dynamic.

Static processing supports files with .jpg, .jpeg, and .png extensions, while dynamic processing applies to files with .webm, .mp4, .avi, .mkv, and .gif extensions. If the file is supported, the processing starts and its progress is displayed in the terminal.

During processing, the script performs several actions, including center cropping for dynamic stickers, setting the required resolution for Telegram stickers, and other file parameters.

Once the processing is complete, all files from the "data" directory are moved to a similar subfolder with the name the user entered at the beginning, but inside the "src/archive" directory. The user is advised to periodically clean this directory manually.


