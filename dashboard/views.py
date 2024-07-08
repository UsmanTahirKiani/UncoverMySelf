import os

import requests
from django.shortcuts import render

from dashboard.gemini import MyGemini, to_markdown, convert_ipython_markdown_to_html
from dashboard.questions import *
from django.conf import settings

from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def quiz(request):
    meta = ""
    if "myers-briggs-type-indicator-quiz" in request.path:
        quiz_questions = quiz_1
        quiz_number = 1
        title = "Uncover Your Personality & Values"
        quiz_title = "Myers-Briggs Type Indicator (MBTI) Quiz"
        image = "quizes/quiz1.jpeg"
        meta = "Discover your MBTI personality type with our free AI-powered quiz. Explore your preferences in " \
               "Extraversion/Introversion, Sensing/Intuition, Thinking/Feeling, and Judging/Perceiving. Unlock your " \
               "potential now."
    elif "enneagram-quiz" in request.path:
        quiz_questions = quiz_2
        quiz_number = 2
        title = "Uncover Your Personality & Values"
        quiz_title = "The Enneagram Quiz"
        image = "quizes/quiz2.jpeg"
        meta = "Dive into the Enneagram with our free AI-powered quiz and uncover your core motivations, fears, and desires. Explore the nine personality types for deeper insights into your personality."
    elif "big-five-personality-test-quiz" in request.path:
        quiz_questions = quiz_3
        quiz_number = 3
        title = "Uncover Your Personality & Values"
        quiz_title = "Big Five Personality Test Quiz"
        image = "quizes/quiz3.jpeg"
        meta = "Take the Big Five Personality Test with our free AI-powered quiz to discover your OCEAN traits. Learn about your Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism."
    elif "values-assessment-quiz" in request.path:
        quiz_questions = quiz_4
        quiz_number = 4
        title = "Uncover Your Personality & Values"
        quiz_title = "Values Assessment Quiz"
        image = "quizes/quiz4.jpeg"
        meta = "Identify your core values with our free AI-powered Values Assessment quiz. Understand what drives your decisions and influences your goals."
    elif "strengthsfinder-quiz" in request.path:
        quiz_questions = quiz_5
        quiz_number = 5
        title = "Discover Your Strengths & Passions"
        quiz_title = "StrengthsFinder Quiz"
        image = "quizes/quiz5.jpeg"
        meta = "Uncover your top strengths with our free AI-powered StrengthsFinder quiz based on Gallup's CliftonStrengths assessment. Leverage your strengths for success."
    elif "skills-assessment-quiz" in request.path:
        quiz_questions = quiz_6
        quiz_number = 6
        title = "Discover Your Strengths & Passions"
        quiz_title = "Skills Assessment Quiz"
        image = "quizes/quiz6.jpeg"
        meta = "Hone in on specific skills like communication, problem-solving, or leadership with our free AI-powered Skills Assessment quiz. Identify your strengths and areas for growth."
    elif "career-interest-inventories-quiz" in request.path:
        quiz_questions = quiz_7
        quiz_number = 7
        title = "Explore Your Interests & Preferences"
        quiz_title = "Career Interest Inventories Quiz"
        image = "quizes/quiz7.jpeg"
        meta = "Align your interests and skills with potential career paths through our free AI-powered Career Interest Inventories quiz. Discover the best career matches for you."
    elif "learning-style-quiz" in request.path:
        quiz_questions = quiz_8
        quiz_number = 8
        title = "Explore Your Interests & Preferences"
        quiz_title = "Learning Style Quiz"
        image = "quizes/quiz8.jpeg"
        meta = "Discover your preferred learning style with our free AI-powered Learning Style quiz. Find out if you " \
               "learn best visually, auditorily, kinesthetically, or through a combination."
    elif "hobby-leisure-quiz" in request.path:
        quiz_questions = quiz_9
        quiz_number = 9
        title = "Explore Your Interests & Preferences"
        quiz_title = " Hobby & Leisure Quiz"
        image = "quizes/quiz9.jpeg"
        meta = "Explore new interests or connect with communities through our free AI-powered Hobby & Leisure quiz. " \
               "Find hobbies that align with your passions."
    elif "motivational-needs-assessment-quiz" in request.path:
        quiz_questions = quiz_10
        quiz_number = 10
        title = "Go Beyond the Basics"
        quiz_title = " Motivational Needs Assessment Quiz"
        image = "quizes/quiz10.jpeg"
        meta = "Understand what truly drives you with our free AI-powered Motivational Needs Assessment quiz. Explore your intrinsic vs. extrinsic motivators."
    elif "decision-making-style-quiz" in request.path:
        quiz_questions = quiz_11
        quiz_number = 11
        title = "Go Beyond the Basics"
        quiz_title = " Decision-Making Style Quiz"
        image = "quizes/quiz11.jpeg"
        meta = "Discover your preferred approach to decision-making with our free AI-powered Decision-Making Style quiz. Find out if you're data-driven, intuitive, or consensus-oriented."
    elif "worldview-quiz" in request.path:
        quiz_questions = quiz_12
        quiz_number = 12
        title = "Go Beyond the Basics"
        quiz_title = "Worldview Quiz"
        image = "quizes/quiz12.jpeg"
        meta = "Explore your perspective on life, society, and your place in the world with our free AI-powered Worldview quiz. Gain insights into your beliefs and values."
    elif "love-language-quiz" in request.path:
        quiz_questions = quiz_13
        quiz_number = 13
        title = " Relationship & Personal Growth"
        quiz_title = "Love Language Quiz"
        image = "quizes/quiz13.jpeg"
        meta = "Foster self-awareness in relationships with our free AI-powered Love Language quiz. Understand how you give and receive love for healthier connections."
    elif "relationship-style-quiz" in request.path:
        quiz_questions = quiz_14
        quiz_number = 14
        title = " Relationship & Personal Growth"
        quiz_title = "Relationship Style Quiz"
        image = "quizes/quiz14.jpeg"
        meta = "Identify your communication style and attachment patterns with our free AI-powered Relationship Style quiz. Build stronger relationships with personalized insights."
    elif "leadership-style-quiz" in request.path:
        quiz_questions = quiz_15
        quiz_number = 15
        title = " Relationship & Personal Growth"
        quiz_title = "Leadership Style Quiz"
        image = "quizes/quiz15.jpeg"
        meta = "Explore your natural leadership tendencies with our free AI-powered Leadership Style quiz. Discover how you motivate others and lead effectively."
    elif "financial-personality-quiz" in request.path:
        quiz_questions = quiz_16
        quiz_number = 16
        title = " Relationship & Personal Growth"
        quiz_title = "Financial Personality Quiz"
        image = "quizes/quiz16.jpeg"
        meta = "Gain insights into your attitude towards money, spending, and saving habits with our free AI-powered Financial Personality quiz. Make informed financial decisions."
    else:
        quiz_questions = []
        title = ""
        quiz_title = ""
        image = ""
        quiz_number = 0
    payload = {
        'quiz': quiz_questions,
        'title': title,
        'quiz_title': quiz_title,
        'image': image,
        'meta': meta,
        'quiz_number': quiz_number,
        'learn_more': "Quiz{num}-Learn-More".format(num=quiz_number)
    }
    if request.method == 'GET':
        # ai_answer = request.COOKIES.get('quiz'+str(quiz_number)+'ai_answer')
        # answers = request.COOKIES.get('quiz'+str(quiz_number)+'answer')
        # payload['ai_answer'] = ai_answer
        # payload['answers'] = answers
        return render(request, 'Quiz.html', payload)
    else:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        resp = r.json()

        if resp['success']:
            quiz_number = request.POST.get('quiz_number', None)
            q1 = request.POST.get('q1')
            q2 = request.POST.get('q2')
            q3 = request.POST.get('q3')
            q4 = request.POST.get('q4')
            q5 = request.POST.get('q5')
            q6 = request.POST.get('q6')
            q7 = request.POST.get('q7')
            q8 = request.POST.get('q8')
            q9 = request.POST.get('q9')
            q10 = request.POST.get('q10')
            q11 = request.POST.get('q11')
            q12 = request.POST.get('q12')
            q13 = request.POST.get('q13')
            q14 = request.POST.get('q14')
            q15 = request.POST.get('q15')
            answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

            quiz_number = int(quiz_number) if quiz_number is not None else 100
            my_quiz = quiz_list[quiz_number-1]
            my_answers = ""
            for i in range(0, len(answers)-1):
                ans_option = answers[i]
                options = my_quiz[i]['options']
                for option in options:
                    if option['option_index'] == ans_option:
                        my_answers = my_answers + "Question: " + my_quiz[i]['question'] + "   Answer: " + option['option'] + "\n"

            prompt = prompt_list[quiz_number-1]
            prompt = prompt + my_answers
            model = MyGemini()
            response = model.ask_gemini(prompt)
            response.resolve()
            result = to_markdown(response.text)
            result = convert_ipython_markdown_to_html(result)
            payload['ai_answer'] = result
            payload['answers'] = answers
            response = render(request, 'result-page.html', payload)
            # response.set_cookie('quiz'+str(quiz_number)+'ai_answer', result)
            # response.set_cookie('quiz'+str(quiz_number)+'answer', answers)
            if resp['success']:
                # Process form data
                return response
            else:
                return render(request, 'Quiz.html', payload)
        return render(request, 'Quiz.html', payload)


def quiz_1_learn_more(request):
    return render(request, 'learn_more_pages/Quiz1-Learn-More.html')


def quiz_2_learn_more(request):
    return render(request, 'learn_more_pages/Quiz2-Learn-More.html')


def quiz_3_learn_more(request):
    return render(request, 'learn_more_pages/Quiz3-Learn-More.html')


def quiz_4_learn_more(request):
    return render(request, 'learn_more_pages/Quiz4-Learn-More.html')


def quiz_5_learn_more(request):
    return render(request, 'learn_more_pages/Quiz5-Learn-More.html')


def quiz_6_learn_more(request):
    return render(request, 'learn_more_pages/Quiz6-Learn-More.html')


def quiz_7_learn_more(request):
    return render(request, 'learn_more_pages/Quiz7-Learn-More.html')


def quiz_8_learn_more(request):
    return render(request, 'learn_more_pages/Quiz8-Learn-More.html')


def quiz_9_learn_more(request):
    return render(request, 'learn_more_pages/Quiz9-Learn-More.html')


def quiz_10_learn_more(request):
    return render(request, 'learn_more_pages/Quiz10-Learn-More.html')


def quiz_11_learn_more(request):
    return render(request, 'learn_more_pages/Quiz11-Learn-More.html')


def quiz_12_learn_more(request):
    return render(request, 'learn_more_pages/Quiz12-Learn-More.html')


def quiz_13_learn_more(request):
    return render(request, 'learn_more_pages/Quiz13-Learn-More.html')


def quiz_14_learn_more(request):
    return render(request, 'learn_more_pages/Quiz14-Learn-More.html')


def quiz_15_learn_more(request):
    return render(request, 'learn_more_pages/Quiz15-Learn-More.html')


def quiz_16_learn_more(request):
    return render(request, 'learn_more_pages/Quiz16-Learn-More.html')


def trigger_404(request):
    return HttpResponseNotFound()


def trigger_500(request):
    return HttpResponseServerError()


def sitemap_view(request):
    file_path = os.path.join('static', 'sitemap.xml')
    with open(file_path, 'r') as file:
        xml_content = file.read()
    return HttpResponse(xml_content, content_type='application/xml')


def ads_txt_view(request):
    with open(os.path.join(os.path.join('static', 'ads.txt'))) as file:
        file_content = file.readlines()
    return HttpResponse(file_content, content_type="text/plain")

