from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('myers-briggs-type-indicator-quiz/', quiz, name='Quiz1'),
    path('enneagram-quiz/', quiz, name='Quiz2'),
    path('big-five-personality-test-quiz/', quiz, name='Quiz3'),
    path('values-assessment-quiz/', quiz, name='Quiz4'),
    path('strengthsfinder-quiz/', quiz, name='Quiz5'),
    path('skills-assessment-quiz/', quiz, name='Quiz6'),
    path('career-interest-inventories-quiz/', quiz, name='Quiz7'),
    path('learning-style-quiz/', quiz, name='Quiz8'),
    path('hobby-leisure-quiz/', quiz, name='Quiz9'),
    path('motivational-needs-assessment-quiz/', quiz, name='Quiz10'),
    path('decision-making-style-quiz/', quiz, name='Quiz11'),
    path('worldview-quiz/', quiz, name='Quiz12'),
    path('love-language-quiz/', quiz, name='Quiz13'),
    path('relationship-style-quiz/', quiz, name='Quiz14'),
    path('leadership-style-quiz/', quiz, name='Quiz15'),
    path('financial-personality-quiz/', quiz, name='Quiz16'),

    path('ai-powered-mbti-quiz-self-discovery-app/', quiz_1_learn_more, name='Quiz1-Learn-More'),
    path('ai-enneagram-quiz-self-discovery/', quiz_2_learn_more, name='Quiz2-Learn-More'),
    path('big-five-test-understand-personality/', quiz_3_learn_more, name='Quiz3-Learn-More'),
    path('values-assessment-find-your-guiding-light/', quiz_4_learn_more, name='Quiz4-Learn-More'),
    path('unleash-strengths-strengthsfinder-test/', quiz_5_learn_more, name='Quiz5-Learn-More'),
    path('skills-assessment-reach-your-goals/', quiz_6_learn_more, name='Quiz6-Learn-More'),
    path('career-interest-test-find-dream-job/', quiz_7_learn_more, name='Quiz7-Learn-More'),
    path('learning-style-quiz-unlock-potential/', quiz_8_learn_more, name='Quiz8-Learn-More'),
    path('hobby-leisure-quiz-find-your-passion/', quiz_9_learn_more, name='Quiz9-Learn-More'),
    path('motivational-needs-assessment-fulfilling-life/', quiz_10_learn_more, name='Quiz310-Learn-More'),
    path('decision-making-quiz-choose-confidently/', quiz_11_learn_more, name='Quiz11-Learn-More'),
    path('worldview-quiz-understand-values/', quiz_12_learn_more, name='Quiz12-Learn-More'),
    path('love-language-quiz-stronger-relationships/', quiz_13_learn_more, name='Quiz13-Learn-More'),
    path('relationship-communication-quiz/', quiz_14_learn_more, name='Quiz14-Learn-More'),
    path('leadership-style-quiz-confident-leader/', quiz_15_learn_more, name='Quiz15-Learn-More'),
    path('financial-personality-quiz-healthy-money-mindset/', quiz_16_learn_more, name='Quiz16-Learn-More'),
    path('trigger-404/', trigger_404),
    path('trigger-500/', trigger_500),
    path('sitemap.xml', sitemap_view, name='sitemap'),
    path("ads.txt", ads_txt_view, name="ads_txt")
]
