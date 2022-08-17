import json


def load_candidates_from_json():
    """Возвращает список всех кандидатов"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate



def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    result = []
    for candidate in load_candidates_from_json():
        if candidate["name"] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    arr = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower().split(', '):
            arr.append(candidate)
    return arr



# x = load_candidates_from_json()
#
# print(f'{x}')
#
# y = get_candidate(56)
# print(f'{y}')

# z = get_candidates_by_name("Sheri Torres")
# print(f'{z}')
#
# c = get_candidates_by_skill('delphi')
# print(f'{c}')
