# -*- coding: utf-8 -*-
# !flask/bin/python
from flask import Flask, render_template
import subprocess

music = Flask(__name__)


@music.route('/shutdown/<int:time>', methods=['GET', 'POST'])
def index(time):
    try:
        command = 'shutdown.exe /t %s /s' % time
        subprocess.run(command)
    except:
        print('test')
    return 'cool'

    # if os.geteuid() != 0:
    #     print('You need to be root to run this script', file=sys.stderr)
    #     sys.exit(1)


music.run(debug=True, host='0.0.0.0', port=8000)

