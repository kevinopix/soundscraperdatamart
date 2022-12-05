from django.core.management.base import BaseCommand
from subprocess import Popen
from sys import stdout, stdin, stderr
import time
import os
import signal
import subprocess,logging
from threading import Thread
import shlex

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Run all commands'
    commands = [
        'python manage.py 1_upload_band_initial',
        'python manage.py 2_upload_band_profile',
        'python manage.py 3_upload_band_members',
        'python manage.py 4_upload_album_categories',
        'python manage.py 5_upload_band_albums',
        'python manage.py 6_upload_album_profiles',
        'python manage.py 7_upload_soundcloudalbumsong',
    ]

    def handle(self, *args, **options):
        proc_list = []

        for command in self.commands:
            print("Starting $ " + command)
            proc = Popen(command, shell=True, stdin=stdin,
                         stdout=stdout, stderr=stderr)
            # proc = Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            try:
                proc.wait()
                print("Processing functionality....... ")
                time.sleep(5)
                print("Finished $ " + command +" Successful Run")
            except KeyboardInterrupt:
                os.kill(proc.pid, signal.SIGKILL)