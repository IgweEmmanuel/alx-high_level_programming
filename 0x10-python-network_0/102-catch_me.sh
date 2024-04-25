#!/bin/bash
#Request and response
curl -sL -X PUT -H "Origint: You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
