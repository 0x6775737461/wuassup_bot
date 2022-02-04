#!/usr/bin/env bash

declare -a tokens
tokens=('twilio_token' 'twilio_sid' 'twilio_num' 'my_num')

for i in {0..3}; do
	actual_token="${tokens[${i}]^^}"

	read -p "[Insert] ${actual_token}: " data

	echo "${actual_token}='${data}'" >> .env
done
