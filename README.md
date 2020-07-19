# net_speed_alert
This python script checks your internet download and upload speed in backgorund by using Ookla Speedtest and if the speed is below the threshold set it will register a complain to your internet service provider by opening a ticket for you via email, which will have upload, download speed and image of result from SpeedTest by Ookla. Thus making sure you need to check and worry 

Tip: It maintains logs of your internet speed every one hour in my case and registers a complain to my ISP via email, if speed goes below the speed told by them.

# How to Run

* Install all the packages listed in requirements.txt
  * CMD : pip install -r requirement.txt
* Set the minimum upload and downlaod speed and schedule gap between your speed test
  * In my case it is set to 60 each.
* Finally run the script 'python net_speed_alert.py'
  * If you want to run in shell for mac use 'python net_speed_alert.py &'