# ga_deployment_firebase


Hi all, welcome to the repo for connecting your apps/games to the firebase database. This repo is mostly meant for the georgia deployment but you can take parts of it to develop other apps/games not relevant to the deployment. My hope is that this will become a living breathing repo over the next few months as we move towards the finish line!

**But Ishaan, what is firebase? Why should we use this?**

Great question! Think of firebase as a NoSQL database in the cloud that works in real-time. Very soon we’ll have a large number of robots and tablets working autonomously alongside humans. These devices will constantly will need to log data. We need read and write to any database we use to be **secure, real-time and avoid conflicts. Hence, firebase!** One of the coolest features of firebase is the ability to get callback notifications everytime the database is updated. Hopefully, things will become clearer once we start working with it.

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

## Overview of architecture

![Alt text](images/architecture.png?raw=true "Title")

We have clients (robots/tablets/phone’s, laptops, etc) that make requests to a REST API hosted on a server. The server then interacts with the database and returns the requested data. 

**Why do we have a server in the middle? Why not directly talk to the database?**

* **Security:** We don’t want the database private keys to live on all machines. In this case, only the server has access to the database keys and that’s all we need to protect.
* **Faster development cycles:** Having a server with a REST API encapsulates people working in different environments (javascript, python, Unity, etc) from having to learn how to interact with the firebase database in their language. 
* **Reduces errors and redundancy:** The same code to update session information implemented in different languages by different people can result in a very brittle system causing errors.


The idea is that, in the final deployment, we’ll deploy a server that will sit in a given school and accept connections from authenticated clients. We can brainstorm other ways of making this more secure. 

## Development

The following 3 files are the most important to work with:

* GA_database.py - Contains all the functions used to communicate with the firebase database. We use pyrebase (python library for firebase) to communicate with the database. 
* app.py - Contains a minimal flask server that uses the functions in GA_database.py to communicate with firebase
* sample_client.py - An example client that uses that makes GET and POST requests to the app to communicate with the database

The data we would like to store is given here in the “Georgia Deployment Tasks & Schedule” worksheet on PRG team drive. Please refer to the “Database” tab in it. 

Since, a large number of people are going to be using the system, we should come up with some rules to abide by. 

* As a start, I’ve created 4 endpoints. The endpoints always receive data in JSON format and return data in JSON format. We should continue this tradition! :) A sample json can be found in sample_client.py.
* Since, its a NoSQL database, we should ensure we’re using the same keys to index the data. I’ve used the exact names as given the worksheet on PRG team drive (I’ve talked about it in the next sentence!) 

## Current functionality

As mentioned earlier, there are 4 endpoints that are already implemented. 


* The first endpoint updates/adds data for a given subject to the database. If the data is not present, it adds the data sent to the database. The server accepts a json with subject information by default. 
* The second endpoint returns the “word_list” for a given subject. I obviously believe we’d want to request a lot of other entries from the database. This would really depend on what data you need for your app. Moving forward, I believe it should be fairly straightforward to request any kind of data following the given example.
* The third endpoint adds session data for a given subject.
* The last endpoint simply deletes all of the data for a given subject.

**How do I start diving into the code?**

I’d suggest first looking at app.py. See a given endpoint and check the functions its calling in GA_database.py. Once, you’re familiar with the flow, you can check example_client.py to see how I’ve made the request in python. A similar HTTP request can be made from any language.

Once you’re comfortable, you can start adding your own endpoints that talk to firebase using different functions in GA_database.py. Additional information on what can be done using pyrebase can be found in the pyrebase documentation. The most used functions would be "set", "push", "update" and "remove" in my opinion.

As you're running the code, you can check the database being updated in realtime. 

* Log in to personalrobotsmit@gmail.com. 
* Click on "Go to console" in the top right
* Click on "GA Deployment"
* Go to "Database" on the left side bar
* Scroll down to "realtime database" and click on "create database" (They have a UI bug, it won't actually create a new database, it'll take you to the one I created). 
* Select "start in locked mode" and hit enable. 

## Future work

* Make flask work over https
* Figure out the most secure way to deploy the server


Feel free to contact me with any questions. Happy coding!


