from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='quotes/', null=True, blank=True)

    def __str__(self):
        return f"{self.text} - {self.author}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    volume = models.IntegerField()
    part = models.IntegerField()
    content = models.TextField()
    published_date = models.DateField()
    week = models.IntegerField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} (Volume {self.volume}, Part {self.part})"

class DepartmentPage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.employee_id}) - {self.department}"

class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.IntegerField()

    def __str__(self):
        return self.question_text

class QuizResult(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.score}"

    def user_employee_id(self):
        return self.user.employee_id

    def user_department(self):
        return self.user.department

    user_employee_id.short_description = 'Employee ID'
    user_department.short_description = 'Department'


