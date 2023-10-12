# Daz Assert ABFD (All In One)

This repo allows you to download and manage all Assert projects needed for 3D development of ABFD.

## Installation

Install [Git](https://git-scm.com/)


linux:
```shell
bash
sudo apt-get install git
```

Login   

github istruction: <https://docs.github.com/en/enterprise-cloud@latest/github-cli/github-cli/quickstart>   

Install [GitHub CLI](https://github.com/cli/cli#installation):

windows:

```shell
winget install --id GitHub.cli
# Use cmd and not powershell
gh auth login
```

linux:

```shell
sudo apt install gh -y
gh auth login
```

mac:

```shell
brew install gh
gh auth login
```

Download

```shell
# Download the parent project (a few MB)
git clone https://github.com/DRincs-Productions/daz-assert-ABFD-all-in-one 'DAZ_3D'
# Download child projects (>100GB)
# it will ask you for authentication for each project (sorry I couldn't make it automatic)
cd DAZ_3D
git submodule update --init --recursive
```

After that use [GitHub Desktop](https://desktop.github.com/) and [open the folder](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop).

## Install Mesh Grabber (Important)

1. [Download](https://raw.githubusercontent.com/DRincs-Productions/daz-assert-genesis-8-9-component-morphs/main/Mesh%20Grabber%20(Win%20%26%20Mac).rar)
2. extract file ![image](https://github.com/DRincs-Productions/daz-assert-ABFD-all-in-one/assets/67595890/dc784255-dbb2-4cc7-8b80-8cc4b6becbd9) into `***\DAZStudio4\scripts`

## Connect them to daz

1) In Daz Open `Edit/Preferences/Content/Content Dictionary Manager...`
 ![image](https://user-images.githubusercontent.com/67595890/187970556-73c7c9a1-7def-4efe-ab4e-24f6a12e0f1e.png)
 ![image](https://user-images.githubusercontent.com/67595890/215262986-ae27c921-87e4-48d1-9414-bdf3acad6625.png)
2) creates a working environment
3) select it
4) click on Daz Studio Format
5) Add all the assert paths you downloaded. (make sure they are all) + **'My DAZ 3D Library'** folder (the deafult folder of daz)
![image](https://user-images.githubusercontent.com/67595890/190847307-1c821678-2014-4d54-af2a-709c373c6abe.png)

## Test

Now in the folder 'Assert ABFD' open  MC
![image](https://user-images.githubusercontent.com/67595890/190847401-7fa7b8e8-d41e-4f5d-a0a0-c36b0027d59f.png)
it doesn't see give you errors otherwise you did something wrong.

## Request new material

If you need an Assert that is not included in this folder try checking in these bookmarks: [raindrop](https://raindrop.io/drincs)
in case you find what you needed or not, request to add a new Assert [here](https://github.com/DRincs-Productions/daz-assert-ABFD-all-in-one/issues/new/choose).

## For [Upload](https://github.com/orgs/DRincs-Productions/teams/upload)

### Add assert

```shell
git submodule add <link> '<Neme Folder>'
```

### Update assert

```shell
git submodule update --remote
```

### Remove assert

```shell
git rm '<Neme Folder>'
```
