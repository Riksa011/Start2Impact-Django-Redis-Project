# Start2Impact Django & Redis Project

<p align="center">
    <img src="Progetto/api/static/icons/logo1.png" alt="SecondChance logo">
</p>

### The main purpose of this project is to combine __Django__, __Redis__, and the __Ethereum Goerli testnet blockchain__ to build a website that allows customers of a second-hand clothing marketplace to track the history of an item through the blockchain.

SecondChance is a __Proof of Concept__, an exercise focused on determining if an idea can be turned into a reality or not. For this reason, it covers only the item transaction on-chain proof and should be connected to an online marketplace to be used in a real situation. 
<br>
If implemented correctly together with a second-hand marketplace, SecondChance could lead to several advantages such as __enhanced transparency__, __increased trust__ between buyers and sellers, and a more __sustainable fashion industry__.
<hr/>



## Main Features:

- A website homepage with a brief explanation of the project
<p align="center">
    <img src="images/1.png" alt="HOMEPAGE - IMAGE 1">
</p>


- A section where administrators can create a new account and log into the platform
<p align="center">
    <img src="images/2.png" alt="ADMIN AUTHENTICATION DROPDOWN - IMAGE 2">
    <img src="images/3.png" alt="ADMIN REGISTER - IMAGE 3">
    <img src="images/4.png" alt="ADMIN LOGIN - IMAGE 4">
    <img src="images/5.png" alt="ADMIN PROFILE - IMAGE 5">
</p>


- A page where administrators only can upload a new clothing item
<p align="center">
    <img src="images/6.png" alt="ADMIN ACTIONS DROPDOWN - IMAGE 6">
    <img src="images/7.png" alt="AUTHENTICATION ERROR: MUST BE LOGGED AS ADMIN - IMAGE 7">
    <img src="images/8.png" alt="ITEM UPLOAD - IMAGE 8">
    <img src="images/9.png" alt="ITEM UPLOADED SUCCESSFULLY - IMAGE 9">
</p>


- A page where anyone can see all the items uploaded on the website and their leading information
<p align="center">
    <img src="images/10.png" alt="USER ACTIONS DROPDOWN - IMAGE 10">
    <img src="images/11.png" alt="UPLOADED ITEMS - IMAGE 11">
</p>


- A page where anyone can enter an ID code of a specific item and see its past transactions provided with the blockchain proof 
<p align="center">
    <img src="images/12.png" alt="SEARCH ITEM - IMAGE 12">
    <img src="images/13.png" alt="ITEM INFO - IMAGE 13">
    <img src="images/14.png" alt="ON-CHAIN PROOF - IMAGE 14">
</p>


- A page where administrators can change an item's owner
<p align="center">
    <img src="images/15.png" alt="CHANGE ITEM OWNER - IMAGE 15">
    <img src="images/16.png" alt="OWNER CHANGED SUCCESSFULLY - IMAGE 16">
    <img src="images/17.png" alt="ITEM INFO - IMAGE 17">
    <img src="images/18.png" alt="ON-CHAIN PROOF - IMAGE 18">
</p>


- A function that alerts administrators when logging into the platform with a different IP address
<p align="center">
    <img src="images/19.png" alt="WARNING: YOUR CURRENT IP ADDRESS IS DIFFERENT FROM THE LAST ONE - IMAGE 19">
</p>


- The ability to adapt the website page and content to different types of devices to allow users to have always the best experience
<p align="center">
    <img src="images/20.png" alt="WEBSITE ADAPTATION EXAMPLE - IMAGE 20">
</p>



## How to deploy

- Download the repository file 
- Be sure to have Python installed on your device, for this project i used Python 3.10.6.
- Be sure to have a Python IDE on board (I recommend [PyCharm](https://www.jetbrains.com/pycharm/)).
- Open the program file in your IDE and create a virtual environment.
- Install program requirements by typing `pip install -r requirements.txt` in a new terminal window.
- Update the program database by typing `cd Progetto`, `python3 manage.py makemigrations` and `python3 manage.py migrate`.
- Run the program by typing `python3 manage.py runserver`.
- Check that Redis is correctly working by typing `redis-cli ping` in a new terminal window: if the response is something like `PONG`, you're ready to enjoy SeconChance, just open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
- Otherwise, if the response  looks something different from `PONG`, most times it's because Redis just didn't start automatically so do it manually by typing `redis-server`.



## Improved Skills
Python, Django, Redis, Etherum Goerli Testnet, HTML and Boostrap CSS
