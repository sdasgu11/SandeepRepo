#CLI Commands
**CLI stands for Command Line Interface**
**This refers to Terminal on Macs, and Git Bash on PC**

**Navigating**
For a full list of CLI commands, see 
cd  -Change Directory (this can happen either forward 'cd Desktop/' or to navigate backwards, use 'cd ../')  

cd ../  -Move back 1 folder. This can be chained together. i.e. 'cd ../../../../' would move you back 4 folders.  

ls  -list the items in the current directory/folder  

pwd  -shows what directory/folder you are currently in.  

mkdir newFolderName/ -makes a directory called newFolderName/  

**Git Commands**
*These are the commands used to connect your local folder to your git repository on GitHub.*

git init - initializes an empty git repo in your local folder
git clone http://github.com/yourUserName/yourRepoName
git status - shows the status of your git repo
git add nameofFile.filetype
git commit -m "your message about what you did." 
***********ALWAYS PULL BEFORE YOU PUSH***********
git pull - pulls down the data from your repo to your local machine
***********ALWAYS PULL BEFORE YOU PUSH***********
git push - pushes data up from your local machine to your repo.
***********ALWAYS PULL BEFORE YOU PUSH***********



**Github Homework Submission Instructions**
*Steps to link an empy folder to your repository*

**Step 1.** 
Go to github.com, sign in, and navigate to your repositories page.
**Step 2.** 
Create a new repository.
-name your repository something you'll remember, soon you'll have a lot of repos.
-make sure you have it set to public access, not private. We can't see it to grade it if it's private.
-Be sure to initialize with a README.md (if you don't, you'll have to add one the hard way.)
**Step 3.** 
Open your CLI on your computer. (Terminal for Mac, Git Bash for Windows)
Navigate to your homework folder.
Create a new folder inside your homework folder called 'ExcelHomework' or called whatever fits for the current homework assignment.
Navigate into the newly created folder.
**Step 4.**
Still in the CLI, enter the command 'git init'
This will initialize a new repository in your folder named 'ExcelHomework'.
**Step 5**
Still in the CLI, enter the command 'git clone https://github.com/yourUserName/yourRepositoryName.git'
Note that the https address is an example of what you should input. The correct address can be found on github.com in your repository, by clicking the green button labeled 'clone or download'.
**Step 6**
Still in the CLI, enter the command ls
This will verify that you have the repository inside of your current folder.
**Step 7**
Still in the CLI, navigate into the new folder inside of 'ExcelHomework' called 'yourRepositoryName'.
*Step 8*
Still in the CLI, enter the command ls
If you see your README.md, congrats!! your folder and repo are linked!


Now, complete your homework in the folder on your local machine called 'yourRepositoryName'. 
Once you have completed the homework, or even better, as you make changes, you need to go through a few steps to push the new information on your local machine up to the repository.

*Step 9*
Reopen your CLI (Terminal/Git Bash)

*Step 10*
In your CLI, Navigate to the 'yourRepositoryName' folder.

*Step 11*
Still in your CLI, use the command 'git status'
This will list out the status of all of the files in the linked folder. Anything that shows up in red text will need to be added and committed to be pushed up to the repo from your local folder.

*Step 12*
Still in your CLI, use the command 'git add fileName.fileType' to add the files that were colored red in your git status. Mac users, please note, ignore any files that are named .DS_Store 

Note - You can add multiple files at once by seperating them with a space.
Example: 'git add test1.txt test2.txt test3.txt index.html assets/'
In the above example, using a single command, we are adding three text files named test1, test2, and test3. we are also adding a html file named index.html, and a folder called assets.

*Step 13*
Once you have added all of the necessary files, its time to commit them.
Still in your CLI, use the command 'git commit -m "your message goes here"'
Inside the quotes, enter a message for yourself letting you know what you did. 
This is mostly so that you can look back at your log and see what you did.
An example, based off of the git add example in step 12, would be
'git commit -m "added test1.txt, test2.txt, test3.txt, index.html, and assets folder."'

*Step 14*
Still in your CLI, run git status again. 
It should say that your branch is one commit ahead of the master branch.

*Step 15*
Still in your CLI, run the command 'git pull'
This will pull all of the information down from your repo to your local machine, this way will help you avoid merge conflicts!

*Step 16*
Once you've successfully run your git pull, 
Still in your CLI, run the command 'git push'

*Step 17*
Back in chrome, on the github site, refresh the page, and look at your repository. 
Everything should be in there, and you deserve a pat on the back! Great Job!!

**Setting Up A Local Version of the Class Repo**
Step 1. Open your CLI
Step 2. Create an empty folder called DataVizClassRepo
Step 3. Navigate into that folder.
Step 4. enter the command 'git init'
Step 5. enter the command 'git clone git@github.com:RutgersCodingBootcamp/RUTSOM201810DATA5.git'
Step 6. cd into the new 'RUTSO201801DATA5-Class-Repository-Data' folder
Step 7. run the command ls, you should see all of the class materials.

To Update your local repo at the start of class, 
Step 1. Open your CLI
Step 2. Navigate to the 'RUTSO201801DATA5-Class-Repository-Data' folder
Step 3. enter the command 'git pull'



