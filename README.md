# fsds_070620_FT_cohort_notes

## STUDY GROUP RECORDINGS & NOTES REPOS

  - 📺[YOUTUBE STUDY GROUP PLAYLIST: online-ds-ft-070620](https://www.youtube.com/playlist?list=PLFknVelSJiSw5mJOlowsVjwQM_iu1OROt)

  - 📓[STUDY GROUP NOTES REPO: online-ds-ft-070620](https://github.com/jirvingphd/fsds_070620_FT_cohort_notes)

  - 📆[GOOGLE CALENDAR LINK - online-ds-ft-070620](https://calendar.google.com/calendar?cid=ZmxhdGlyb25zY2hvb2wuY29tXzRqc2xvdGkwZ3VsNGkza3AzMzA4ZHJsZnBrQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20)

- **NOTE RE NOTES REPOS:**

  - 🚨**DO NOT FORK NOTES REPO BEFORE CLONING** (to easily get all new notebooks.)

  - Just clone directly and run `git pull` from inside the repo's folder in your terminal to get the new notebooks.

## RESOURCES FOLDER

- 🗂[STUDENT RESOURCES GOOGLE DRIVE FOLDER](https://drive.google.com/drive/folders/1E3JBOl0uhLMRKvl9R5vpl6xaxchiJ6JA?usp=sharing)
  - See  Student Resources Section farther down the page for details.



## How to sync a fork of this repo
- While it is recommended to clone this repo directly to get updates easily, below are excerpts from the official GitHub documentation on the steps required to sync a fork so that it receives changes made to the upstream repo (the one you forked). 

### 1. [Configure a remote for the forked repo](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)
1. Open Terminal.
    - cd into repo
2. List the current configured remote repository for your fork.
`$ git remote -v`
3. Specify a new remote upstream repository that will be synced with the fork.
`$ git remote add upstream https://github.com/jirvingphd/online-dtsc-pt-041320-cohort-notes.git`

4. Verify the new upstream repository you've specified for your fork.
`$ git remote -v`

### 2. [Syncing a fork]( https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

1. Open Terminal.

2. cd into repo's folder
    
3. Fetch the branches and their respective commits from the upstream repository. Commits to master will be stored in a local branch, `upstream/master`.

`$ git fetch upstream`


4. Check out your fork's local master branch.

`$ git checkout master`

5. Merge the changes from upstream/master into your local master branch. This brings your fork's master branch into sync with the upstream repository, without losing your local changes.
`$ git merge upstream/master`

If your local branch didn't have any unique commits, Git will instead perform a "fast-forward":


> Tip: Syncing your fork only updates your local copy of the repository. To update your fork on GitHub, you must push your changes.

