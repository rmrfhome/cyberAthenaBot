from enum import Enum
import random


# lib for pattern matching - pampy
# add unit tests


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
    Secunda = 2
    Tertia = 3
    Quarta = 4
    Quinta = 5


class Numerus(Enum):
    Singularis = 1
    Pluralis = 2


declension_rules = {}
declension_rules[Declinatio.Pirma] = {}
declension_rules[Declinatio.Pirma][Numerus.Singularis] = {
    Casus.Nominativus: 'a',
    Casus.Accusativus: 'am',
    Casus.Genitivus: 'ae',
    Casus.Dativus: 'ae',
    Casus.Ablativus: 'ā',
}
declension_rules[Declinatio.Pirma][Numerus.Pluralis] = {
    Casus.Nominativus: 'ae',
    Casus.Accusativus: 'ās',
    Casus.Genitivus: 'ārum',
    Casus.Dativus: 'īs',
    Casus.Ablativus: 'īs',
}
declension_rules[Declinatio.Secunda] = {}
declension_rules[Declinatio.Secunda][Numerus.Singularis] = {
    Casus.Nominativus: 'us',
    Casus.Accusativus: 'um',
    Casus.Genitivus: 'ī',
    Casus.Dativus: 'ō',
    Casus.Ablativus: 'ō',
}
declension_rules[Declinatio.Secunda][Numerus.Pluralis] = {
    Casus.Nominativus: 'ī',
    Casus.Accusativus: 'ōs',
    Casus.Genitivus: 'ōrum',
    Casus.Dativus: 'īs',
    Casus.Ablativus: 'īs',
}
declension_rules[Declinatio.Tertia] = {}
declension_rules[Declinatio.Tertia][Numerus.Singularis] = {
    Casus.Nominativus: '',
    Casus.Accusativus: 'em',
    Casus.Genitivus: 'is',
    Casus.Dativus: 'ī',
    Casus.Ablativus: 'e',
}
declension_rules[Declinatio.Tertia][Numerus.Pluralis] = {
    Casus.Nominativus: 'ēs',
    Casus.Accusativus: 'ēs',
    Casus.Genitivus: 'um',
    Casus.Dativus: 'ibus',
    Casus.Ablativus: 'ibus',
}
declension_rules[Declinatio.Quarta] = {}
declension_rules[Declinatio.Quarta][Numerus.Singularis] = {  # TODO add second variant, add irregular forms
    Casus.Nominativus: 'us',
    Casus.Accusativus: 'um',
    Casus.Genitivus: 'ūs',
    Casus.Dativus: 'uī',
    Casus.Ablativus: 'ū',
}
declension_rules[Declinatio.Quarta][Numerus.Pluralis] = {
    Casus.Nominativus: 'ūs',
    Casus.Accusativus: 'ūs',
    Casus.Genitivus: 'uum',
    Casus.Dativus: 'ibus',
    Casus.Ablativus: 'ibus',
}
declension_rules[Declinatio.Quinta] = {}
declension_rules[Declinatio.Quinta][Numerus.Singularis] = {
    Casus.Nominativus: 'ēs',
    Casus.Accusativus: 'em',
    Casus.Genitivus: 'eī',
    Casus.Dativus: 'eī',
    Casus.Ablativus: 'ē',
}
declension_rules[Declinatio.Quinta][Numerus.Pluralis] = {
    Casus.Nominativus: 'ēs',
    Casus.Accusativus: 'ēs',
    Casus.Genitivus: 'ērum',
    Casus.Dativus: 'ēbus',
    Casus.Ablativus: 'ēbus',
}


def conjugate(verbum: tuple, numerus: Numerus, casus: Casus):
    return verbum[0] + declension_rules[Declinatio.Pirma][numerus][casus]


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
    Casus.Nominativus: 'nomintivō',
    Casus.Accusativus: 'accusativō',
    Casus.Genitivus: 'genitivō',
    Casus.Dativus: 'dativō',
    Casus.Ablativus: 'ablativō',
}

abl_num_names = {
    Numerus.Singularis: 'singularō',
    Numerus.Pluralis: 'pluralō'
}


def prepare_guestion(verbum: tuple):
    new_numerus = get_random_numerus()
    new_casus = get_random_casus()
    base_form = conjugate(verbum, Numerus.Singularis, Casus.Nominativus)
    question = f'Quid {base_form} in numerō {abl_num_names[new_numerus]} et casō {abl_cases_names[new_casus]} est?'
    return (question, prepare_answers(verbum, new_numerus, new_casus))
