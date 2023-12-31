from subprocess import run
from flask import Flask, render_template, request, redirect, make_response
from bma.session import Session, U, time
from bma.task import get_task, BMAIL_PATH

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    print(request.form)
    if (request.method == 'POST'):
        uuid = request.cookies.get('uuid')
        if (uuid in U.data):
            action = str(request.form["action"])
            text = get_task(uuid, action).split("\n")
            return render_template('play.html', uuid=uuid, text=text)
        else:
            s = None
            try:
                data = dict(request.form.lists())
                b, u, t = str(request.form["dom_type"]).split(',')
                b = int(b)
                u = int(u)
                t = (float(t) * 60 * 60) + time()
                k = " ".join(data["kinks"])
                p = " ".join(data["punishments"])
                l = str(request.form["hard_limits"])
                d = int(request.form["dificulty"])
                bmt = str(request.form["bm_type"])
                bmd = str(request.form["b_data"])
                if (bmt == "post"):
                    u_data = ""
                    b_data = bmd
                elif (bmt == "unlock"):
                    u_data = bmd
                    b_data = ""
                else: 
                    u_data = ""
                    b_data = ""
                s = Session(b=b, u=u, time_end=t, kinks=k, punishments=p,
                            hard_limits=l, difficulty=d, u_data=u_data, b_data=b_data)
                print(s)
            except Exception as e:
                print(e)
                return render_template('start.html')
            U.data[s.uuid] = s
            U.update()
            ret = make_response(render_template('new.html', uuid=s.uuid))
            ret.set_cookie('uuid', s.uuid)
            return ret
    else:
        uuid = request.cookies.get('uuid')
        if (uuid in U.data):
            text = get_task(uuid, "reload").split("\n")
            return render_template('play.html', uuid=uuid, text=text)
        else:
            return render_template('start.html')

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    print(request.form)
    if (request.method == 'POST'):
        uuid = str(request.form["uuid"])
        if (uuid in U.data):
            ret = make_response(render_template('new.html', uuid=uuid))
            ret.set_cookie('uuid', uuid)
            return ret
    else:
        uuid = request.cookies.get('uuid')
        if (uuid in U.data):
            ret = render_template('new.html', uuid=uuid)
            return ret
        else:
            return render_template('resume.html')

@app.route('/wall-of-shame', methods=['GET', 'POST'])
def wos():
    with open(BMAIL_PATH, "r") as f:
        dat = f.readlines()
        ret = make_response(render_template('wos.html', text=dat))
        return ret

@app.route('/tos', methods=['GET', 'POST'])
def tos():
    ret = make_response(render_template('tos.html'))
    return ret

@app.route('/wiki', methods=['GET', 'POST'])
def wiki():
    ret = make_response(render_template('wiki.html'))
    return ret

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    ret = make_response(render_template('logout.html'))
    ret.set_cookie('uuid', "------")
    return ret
