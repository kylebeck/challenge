from flask import render_template, flash, redirect, session, url_for
from distance import levenshtein, sorensen, jaccard
from app import app
from .forms import CompareForm

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')


@app.route('/form',methods=['GET', 'POST'])

def compare():
    form = CompareForm()
    if form.validate_on_submit():
        session['string1'] = form.string1.data
        session['string2'] = form.string2.data
        session['metric'] = form.metric.data
        flash('Computing the requested metric.')
        return redirect(url_for('results'))
    return render_template('form.html', form=form)

@app.route('/results')

def results():
    metrics = {'Levenshtein' : levenshtein,
        'Jaccard' : jaccard,
        'Sorensen' : sorensen}
    return render_template('results.html', \
        metric=session['metric'], \
        string1=session['string1'], \
        string2=session['string2'], \
        result=metrics[session['metric']]( \
            session['string1'], \
            session['string2']))

