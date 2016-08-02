import csv
import json
from enchant.checker import SpellChecker
from flask import Flask
from flask import request
from flask import jsonify
spellcheck = SpellChecker("en_US")
from lstm import *
sls=lstm("bestsem.p",load=True,training=False)
with open('retail_banking_t.csv', 'rb') as f:
    reader = csv.reader(f)
    corpus = list(reader)

def BankingAsk(input_string):
        scored_questions = []
        input =  input_string
        spellcheck.set_text(input)
        for err in spellcheck:
            print err.word
            sug = err.suggest()[0]
            err.replace(sug)
            input = spellcheck.get_text()
            print input
        for question in corpus: x = sls.predict_similarity(input,
                                                           "".join(question)) * 4.0 + 1.0; scored_questions.insert(0, [
            float(x), "".join(question)])
        sorted_questions = sorted(scored_questions, key=lambda score: score[0], reverse=True)
        return(json.dumps(sorted_questions[0:5]))

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json(force=True)
    input_string = request_data.get('input')
    return BankingAsk(input_string)


