from enum import Enum
import random


class Casus(Enum):
    Nominativus = 1
    Accusativus = 2
    Genitivus = 3
    Dativus = 4
    Ablativus = 5


class Gender(Enum):
    Feminine = 1
    Masculine = 2
    Neuter = 3


class Declinatio(Enum):
    Pirma = 1


class Numerus(Enum):
    Singularis = 1
    Pluralis = 2


declention_rules = {}
declention_rules[Declinatio.Pirma] = {}
declention_rules[Declinatio.Pirma][Numerus.Singularis] = {
    Casus.Nominativus : 'a',
    Casus.Accusativus : 'am',
    Casus.Genitivus : 'ae',
    Casus.Dativus : 'ae',
    Casus.Ablativus : 'ā',
}
declention_rules[Declinatio.Pirma][Numerus.Pluralis] = {
    Casus.Nominativus: 'ae',
    Casus.Accusativus: 'ās',
    Casus.Genitivus: 'ārum',
    Casus.Dativus: 'īs',
    Casus.Ablativus: 'īs',
}


def conjugate(verbum: tuple, numerus: Numerus, casus: Casus):
    return verbum[0] + declention_rules[Declinatio.Pirma][numerus][casus]


def get_random_casus():
    return random.choice(list(set(list(Casus)) - set([Casus.Nominativus])))

def get_random_numerus():
    return random.choice(list(Numerus))

def prepare_answers(verbum: tuple, numerus: Numerus, casus: Casus):
    correct_answer = conjugate(verbum, numerus, casus)
    answers = [correct_answer]
    while len(answers) < 4:
        new_numerus = get_random_numerus()
        new_casus = get_random_casus()
        new_answer = conjugate(verbum, new_numerus, new_casus)
        if new_answer not in answers:
            answers.append(new_answer)
    random.shuffle(answers)
    return list(map(
        lambda x: (x, f'{x.capitalize()} vērus rēsponsus est!' 
            if x == correct_answer 
            else 'Non vērus rēsponsus est!'),
        answers))

abl_cases_names = {
    Casus.Nominativus : 'nomintivō',
    Casus.Accusativus : 'accusativō',
    Casus.Genitivus : 'genitivō',
    Casus.Dativus : 'dativō',
    Casus.Ablativus : 'ablativō',
}

abl_num_names = {
    Numerus.Singularis : 'singularō',
    Numerus.Pluralis : 'pluralō'
}

def prepare_guestion(verbum: tuple):
    new_numerus = get_random_numerus()
    new_casus = get_random_casus()
    base_form = conjugate(verbum, Numerus.Singularis, Casus.Nominativus)
    question = f'Quid {base_form} in numerō {abl_num_names[new_numerus]} et casō {abl_cases_names[new_casus]} est?'
    return (question, prepare_answers(verbum, new_numerus, new_casus))

