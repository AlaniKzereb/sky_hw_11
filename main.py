from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidates_by_name, get_candidate, get_candidates_by_skill

app = Flask(__name__)

@app.route('/')
def page_index():
    """Главная страница"""
    candidates = load_candidates_from_json()
    page = render_template("list.html", candidates=candidates)
    return page

@app.route('/candidate/<int:id>')
def page_card(id):
    """Карточка кандидата"""
    candidate = get_candidate(id)
    if candidate:
        page = render_template('card.html', candidate=candidate)
        return page
    else:
        return "NOT FOUND"


@app.route('/search/<candidate_name>')
def page_name(candidate_name):
    """Вывод кандидатов по имени"""
    candidates = get_candidates_by_name(candidate_name)
    page = render_template("search.html", candidates=candidates)
    return page


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    """Вывод кандидатов по навыку"""
    candidates = get_candidates_by_skill(skill_name)
    page = render_template("skill.html", candidates=candidates, skill=skill_name)
    return page

if __name__ == '__main__':
    app.run(port=5000)
