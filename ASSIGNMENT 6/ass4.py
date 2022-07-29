import re
text = "Send me mail by abc@gmail.com"
email = re.findall('\S+@\S+', text)	
print(email)
