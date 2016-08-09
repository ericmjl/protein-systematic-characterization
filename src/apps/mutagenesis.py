from calculators import mutagenesis as mt
from flask import Flask, render_template, request

import numpy as np
import math

app = Flask(__name__)

mut_freq_mass = dict(low=500, med=100, high=50)
mut_freq_fold = dict(low=5, med=100, high=5000)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compute', methods=['POST'])
def compute():
    # Access the form variables.
    target_len = float(request.form['target_len'])
    plasmid_len = float(request.form['plasmid_len'])
    mut_freq = request.form['mut_freq']
    input_conc = float(request.form['input_conc'])

    # Access the necessary variables.
    target_mass = mut_freq_mass[mut_freq]
    fold_amp = mut_freq_fold[mut_freq]

    # Compute what needs to be computed.
    input_mass = mt.input_plasmid_mass(target_len, plasmid_len, target_mass)
    input_volume = mt.input_volume(input_mass, input_conc)
    num_cycles = mt.num_cycles(fold_amp)
    cycle_time = math.ceil(target_len / 1000)


    # Pack things up in a tuple for ease of passing to template.
    return render_template('compute.html',
                           input_mass=np.around(input_mass, 2),
                           input_volume=np.around(input_volume, 2),
                           num_cycles=num_cycles,
                           cycle_time=cycle_time)

if __name__ == '__main__':
    app.run(port=5003, debug=True)
