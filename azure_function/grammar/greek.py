from enum import Enum
import random
import pampy


class Case(Enum):
    Nominative = 1
    Accusative = 2
    Genitive = 3
    Dative = 4


class Gender(Enum):
    Female = 1
    Masculine = 2
    Neutral = 3


class Declension(Enum):
    First = 1
    Second = 2
    Third = 3


class Number(Enum):
    Single = 1
    Dual = 2
    Plural = 3


def decline_noun(stem: str, genitiveEnding: str, declension: Declension, gender: Gender, number: Number, case: Case) -> str:
    input = [declension, gender, number]
    return pampy.match(
        input,
        [Declension.First, Gender.Female, Number.Single], 
            decline_first_decl_female_singular(stem, genitiveEnding, case),
        [Declension.First, Gender.Female, Number.Dual],
            decline_first_decl_female_dual(stem, case),
        [Declension.First, Gender.Female, Number.Plural],
            decline_first_decl_female_dual(stem, case),
        [str, str, Declension, Gender, Number, Case], ''
    )


def decline_first_decl_female_singular(stem: str, genitiveEnding: str, case: Case):
    return pampy.match(
        case,
        Case.Nominative, stem + 'α',
        Case.Accusative, stem + 'αν',
        Case.Genitive, stem + 'ᾱς', 
        Case.Dative, stem + 'ᾳ'
    )


def decline_first_decl_female_plural(stem: str, case: Case):
    return pampy.match(
        case,
        Case.Nominative, stem + 'αι',
        Case.Accusative, stem + 'ᾱς',
        Case.Genitive, stem + 'ων', 
        Case.Dative, stem + 'αις'
    )


def decline_first_decl_female_dual(stem: str, case: Case):
    return pampy.match(
        case,
        Case.Nominative, stem + 'ᾱ',
        Case.Accusative, stem + 'ᾱ',
        Case.Genitive, stem + 'αιν', 
        Case.Dative, stem + 'αιν'
    )


all_cases = list(set(Case))
all_non_nominative_cases = list(set(all_cases) - set([Case.Nominative]))
all_genders = list(set(Gender))
all_declensions = list(set(Declension))
all_numbers = list(set(Number))


class Noun:
    def __init__(self, stem: str, genitiveEnding: str, declension: Declension, gender: Gender):
        self.stem = stem
        self.genitiveEnding = genitiveEnding
        self.declension = declension
        self.gender = gender

    def decline(self, number: Number, case: Case) -> str:
        return decline_noun(self.stem, self.genitiveEnding, self.declension, self.gender, number, case)

    def create_initial_form(self) -> str:
        return self.decline(Number.Single, Case.Nominative)

    def create_random_form(self) -> (str, Number, Case):
        random_number = random.choice(all_numbers)
        random_case = random.choice(all_non_nominative_cases)
        declined_word = self.decline(random_number, random_case)
        return (declined_word, random_number, random_case)


class Answer:
    def __init__(self, value: str, isValid: bool) -> None:
        self.value = value
        self.isValid = isValid


class Question:
    def __init__(self, question: str, answers: list) -> None:
        self.question = question
        self.answers = answers

def strNum(number: Number) -> str:
    return pampy.match(number, 
        Number.Plural, 'множественном числе',
        Number.Dual, 'двойственном числе',
        Number.Single, 'единственном числе',
    )

def strCase(c: Case) -> str:
    return pampy.match(c, 
        Case.Nominative, 'номинативе',
        Case.Accusative, 'аккузативе',
        Case.Genitive, 'генитиве',
        Case.Dative, 'дативе',
    )

def create_question(word: Noun) -> Question:
    (correct_form, number, case) = word.create_random_form()
    forms = [correct_form]
    while len(forms) < 4:
        (new_answer, _, _) = word.create_random_form()
        if new_answer not in forms:
            forms.append(new_answer)
    random.shuffle(forms)
    answers = list(map(lambda x: Answer(x, x == correct_form), forms))
    return Question(
        question = f'{word.create_initial_form().capitalize()} в {strNum(number)} {strCase(case)}?',
        answers = answers
    )

