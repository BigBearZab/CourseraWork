#!/usr/bin/env python3

import socket
import psutil
from email.message import EmailMessage
from emails import send_message
sender = 'automation@example.com'
reciever = 'student-02-f909838ffa9b@example.com'

def generate_error_alert(sender, recipient, subject, body):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    return message

def send_error_alert(subject):
    msg =  generate_error_alert(sender, reciever, subject, 'Please check your system and resolve the issue as soon as possible.')
    send_message(msg)

def check_cpu():
    print(f'CPU usage is {psutil.cpu_percent()}')
    if psutil.cpu_percent() > 80:        
        send_error_alert('Error - CPU usage is over 80%')

def check_available_disk_space():
    hdd = psutil.disk_usage('/')
    free_hdd = hdd.free / hdd.total
    print(f'Free disk is {free_hdd}')
    if free_hdd < 0.2:
        send_error_alert('Error - Available disk space is less than 20%')

def check_available_memory():
    mem = psutil.virtual_memory()
    free_mem = mem.available >> 20
    print(f'Free memory is {free_mem} mb')
    if free_mem < 500:
        send_error_alert('Error - Available memory is less than 500MB')

def check_localhost():
    host = socket.gethostbyname(socket.gethostname())
    print(f'Hostname is: {host}')
    if host != '127.0.0.1':
        send_error_alert('Error - localhost cannot be resolved to 127.0.0.1')

if __name__ == "__main__":
    check_cpu()
    check_available_disk_space()
    check_available_memory()
    check_localhost()