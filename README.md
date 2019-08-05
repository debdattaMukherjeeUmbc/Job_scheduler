# Job_scheduler

What does this api do?

This Api takes in a job_name, command and a schedule_time and triggers a downstream job that triggers the bash command in the time that it was scheduled for. 
You can also list all schedules that you had posted for till now.


Architecture

I have used django rest framework to build the rest api and used python Apscheduler that can schedule jobs dynamically, when a schedule is posted by a user. Other workflow managers that I considered were apache airflow and pinball. I used apscheduler should for this project.


Endpoints

Get /schedules -> Lists all the schedules that have been posted till now
Post /schedules -> Saves the schedule and creates a trigger to execute it.


Assumptions

This api can only trigger a bash command on a particular given time. Though it can be easily enhanced to support recurring execution of the bash commands as apscheduler have support for it.


Testing plan
Example:
1. Open postman
2. Choose Content-Type as application/json
3. Do a GET on /schedules
4. Now do a POST with the following json:
{
	"job_name": "job_new",
	"command": "echo hi user",
	"schedule_time": "2019-08-05T01:29:00Z" 
}
Note: The schedule time you enter needs to be in future. So schedule this task, one minute or two minute from current time.
Result: You should be able to see "hi user" written on the console.
5. You can also use:
{
	"job_name": "job_new",
	"command": "ls",
	"schedule_time": "2019-08-05T01:29:00Z" 
}
Result: This would show the list in the console.
