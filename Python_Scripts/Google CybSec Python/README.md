This was code made and modified after the Google CyberSecurity Specialist Certification Course. The Origial Scenario was to run a comparison against files of IPs to confirm if public IPv4 addresses found on the system match associated references to known good public IPv4 or create a list of public IPv4 addresses that need to be removed. 

This was completed on 3/16/2024. Original code per the assignment used an array of IPs and compared them to a test. I modified mine post-course to just take in two documents, "allow_list.txt" and "remove_list.txt". 

My thought process here was since the purpose of this module was to expose individuals to scripting manual-like review that having a script ready made to accept files better shows future usability instead of having to manually update an array of IPs. It's easier to pull a list of potentially bad IPs, put them in a CSV format within a txt file to review then modifying the array+formatting. 


The script was tested in a local linux VM I spun up to make sure the results were accurate to the original code that was submitted within Jupyter (used by the course). 