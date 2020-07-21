# Internet Speed Alert
This python script checks your internet download and upload speed in backgorund by using Ookla Speedtest and if the speed is below the threshold set it will register a complain to your internet service provider by opening a ticket for you via email, which will have upload, download speed and image of result from SpeedTest by Ookla. Thus giving them a proof about downlaod and upload speed

Tip: It maintains logs of your internet speed every 'one hour' in my case and registers a complain to my ISP via email, if speed goes below the speed told by them.

Note: Many other ways to do the same thing, but wanted to learn about subprocess so this is what I came up with

# How to Run

* Install all the packages listed in requirements.txt

.. code-block:: python
       pip install -r requirement.txt
* Set the minimum upload and downlaod speed and schedule gap between your speed test
  * In my case it is set to 60 Mbits each.
* Set your email address and password, also your sender email ID i.e ISP helpdesk email
* Finally run the script 'python net_speed_alert.py'
  * If you want to run in shell for mac use 'python net_speed_alert.py &'
