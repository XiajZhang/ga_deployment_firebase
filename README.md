# ga_deployment_firebase


Hi all, welcome to the repo for connecting your apps/games to the firebase database. This repo is mostly meant for the georgia deployment but you can take parts of it to develop other apps/games not relevant to the deployment. My hope is that this will become a living breathing repo over the next few months as we move towards the finish line!

**But Ishaan, what is firebase? Why should we use this?**
Great question! Think of firebase as a NoSQL database in the cloud that works in real-time. Very soon we’ll have a large number of robots and tablets working autonomously alongside humans. These devices will constantly will need to log data. We need read and write to any database we use to be **secure, real-time and avoid conflicts. Hence, firebase! **One of the coolest features of firebase is the ability to get callback notifications everytime the database is updated. Hopefully, things will become clearer once we start working with it.

## Installation and Setup

First install anaconda/miniconda for python 3.7 from here:
**Miniconda: https://docs.conda.io/en/latest/miniconda.html**
**Anaconda: https://www.anaconda.com/distribution/**

Now clone the repository from here and cd into it:

```
https://github.com/mitmedialab/ga_deployment_firebase.git
```

```
cd ga_deployment_firebase
```

Link pip with conda. A simple command to update pip with conda should do this:

```
conda update pip
```

Load the environment for this project

```
conda env create -f env.yml
```

Activate the environment

```
conda activate database
```

At this point, you should be running python 3.6 in the environment and have all dependencies installed. Check the python version:

```
python --version
```

Create a folder called cred:

```
mkdir cred
```

***Note: For the next step we’ll download a config file and private key. Keep these very very secret and NEVER share them with anyone. ***

Access to files: https://www.dropbox.com/sm/password?cont=https%3A%2F%2Fwww.dropbox.com%2Fsh%2Fqn7ocazff2o61gm%2FAACLdxDcy5e8FcqHvsi3eYnRa%3Fdl%3D0&content_id=AK3fNFdNkSePR0h6fDBwxG2P_pKEoHTQobk

Place both the files in the folder named “cred” that we just created.

We’re now ready to start interacting with the firebase database!








