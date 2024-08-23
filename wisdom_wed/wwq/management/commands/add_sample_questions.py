from django.core.management.base import BaseCommand
from wwq.models import QuizQuestion

class Command(BaseCommand):
    help = 'Add sample quiz questions to the database'

    def handle(self, *args, **kwargs):
        sample_questions = [
            {
                'question_text': 'What does CPU stand for?',
                'option1': 'Central Processing Unit',
                'option2': 'Central Process Unit',
                'option3': 'Computer Personal Unit',
                'option4': 'Central Processor Unit',
                'correct_option': 1
            },
            {
                'question_text': 'Which programming language is known as the backbone of web development?',
                'option1': 'Java',
                'option2': 'Python',
                'option3': 'JavaScript',
                'option4': 'C++',
                'correct_option': 3
            },
            {
                'question_text': 'What does HTML stand for?',
                'option1': 'Hyper Text Markup Language',
                'option2': 'High Text Markup Language',
                'option3': 'Hyper Tabular Markup Language',
                'option4': 'None of these',
                'correct_option': 1
            },
            {
                'question_text': 'Which company developed the Java programming language?',
                'option1': 'Microsoft',
                'option2': 'Google',
                'option3': 'Sun Microsystems',
                'option4': 'Apple',
                'correct_option': 3
            },
            {
                'question_text': 'What does HTTP stand for?',
                'option1': 'Hypertext Transfer Protocol',
                'option2': 'Hypertext Transfer Plot',
                'option3': 'Hyper Transfer Protocol',
                'option4': 'High Transfer Protocol',
                'correct_option': 1
            },
            {
                'question_text': 'Which programming language is used for AI and Machine Learning?',
                'option1': 'Python',
                'option2': 'C++',
                'option3': 'Java',
                'option4': 'JavaScript',
                'correct_option': 1
            },
            {
                'question_text': 'What does SQL stand for?',
                'option1': 'Structured Query Language',
                'option2': 'Structured Question Language',
                'option3': 'Sequential Query Language',
                'option4': 'None of these',
                'correct_option': 1
            },
            {
                'question_text': 'Which technology is used to make telephone calls over the Internet possible?',
                'option1': 'Bluetooth',
                'option2': 'VoIP',
                'option3': 'Wi-Fi',
                'option4': 'Ethernet',
                'correct_option': 2
            },
            {
                'question_text': 'Which company developed the C programming language?',
                'option1': 'Microsoft',
                'option2': 'Apple',
                'option3': 'AT&T Bell Labs',
                'option4': 'IBM',
                'correct_option': 3
            },
            {
                'question_text': 'What is the full form of CSS?',
                'option1': 'Cascading Style Sheets',
                'option2': 'Cascading Style Script',
                'option3': 'Cascading Sheet Style',
                'option4': 'None of these',
                'correct_option': 1
            },
            {
                'question_text': 'Which of the following is not a database management system?',
                'option1': 'MySQL',
                'option2': 'Oracle',
                'option3': 'Microsoft SQL Server',
                'option4': 'COBOL',
                'correct_option': 4
            },
            {
                'question_text': 'What is the main component of a computer that executes instructions?',
                'option1': 'Motherboard',
                'option2': 'Hard Disk',
                'option3': 'CPU',
                'option4': 'RAM',
                'correct_option': 3
            },
            {
                'question_text': 'Which of the following is a version control system?',
                'option1': 'Git',
                'option2': 'Docker',
                'option3': 'Kubernetes',
                'option4': 'Jenkins',
                'correct_option': 1
            },
            {
                'question_text': 'What is the primary purpose of DNS in networking?',
                'option1': 'To assign IP addresses to devices',
                'option2': 'To translate domain names to IP addresses',
                'option3': 'To route data packets',
                'option4': 'To secure network communications',
                'correct_option': 2
            },
            {
                'question_text': 'What does RAM stand for?',
                'option1': 'Read Access Memory',
                'option2': 'Random Access Memory',
                'option3': 'Readily Available Memory',
                'option4': 'Randomly Available Memory',
                'correct_option': 2
            },
        ]

        for question in sample_questions:
            QuizQuestion.objects.create(**question)

        self.stdout.write(self.style.SUCCESS('Sample quiz questions added successfully.'))
