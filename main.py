from flask import Flask, render_template, request, redirect, send_file
from stack import extract_stack
from wework import extract_wework
from remote import extract_remote
from save import save_to_file
"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
db = {}
app = Flask("remote jobs")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    term = request.args.get("term")

    if term:
        term = term.lower()
        fakeDb = db.get(term)
        if fakeDb:
            result = fakeDb
        else:
            try:
                result = extract_stack(
                    term)+extract_wework(term)+extract_remote(term)
                db[term] = result
            except:
                return render_template("error.html")
    else:
        return redirect("/")
    number = int(len(result))
    return render_template("search.html", result=result, term=term, number=number)


@app.route("/export")
def export():
    term = request.args.get("term")
    term = term.lower()
    result_db = db.get(term)
    save_to_file(term, result_db)

    return send_file(f"{term}.csv", as_attachment=True)


app.run(host="0.0.0.0")
