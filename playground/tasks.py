from time import sleep
# from storefront.celery import celery # Traditional way to create task and become dependent on storefront app
from celery import shared_task # new independent way to create tasks

@shared_task
def notify_customers(message):
    print('Sending 10k emails...')
    print(message)
    print('Emails were successfully sent!!!')