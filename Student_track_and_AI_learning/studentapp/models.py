from django.db import models

class login_table(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class staff_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    pin=models.BigIntegerField()
    ph_no=models.BigIntegerField()
    email=models.CharField(max_length=100)
    Class=models.IntegerField()
    photo=models.FileField()

class parent_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    ph_no = models.BigIntegerField()
    email=models.CharField(max_length=100)
    parent_name=models.CharField(max_length=20)
    Class=models.IntegerField()
    DOB=models.DateField()
    gender=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    pin=models.BigIntegerField()
    photo=models.FileField()


class expert_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    pin=models.BigIntegerField()
    ph_no=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()


class daily_activities(models.Model):
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    date=models.DateField()
    activity=models.CharField(max_length=100)
    details=models.CharField(max_length=100)


class attendence_table(models.Model):
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    PARENT=models.ForeignKey(parent_table,on_delete=models.CASCADE)
    date=models.DateField()
    attendence=models.BigIntegerField()


class leave(models.Model):
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    PARENT=models.ForeignKey(parent_table,on_delete=models.CASCADE)
    date=models.DateField()
    reason=models.CharField(max_length=100)


class doubt_table(models.Model):
    EXPERT=models.ForeignKey(expert_table,on_delete=models.CASCADE)
    PARENT=models.ForeignKey(parent_table,on_delete=models.CASCADE)
    date=models.DateField()
    doubt=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)


class study_material(models.Model):
    EXPERT=models.ForeignKey(expert_table,on_delete=models.CASCADE)
    date=models.DateField()

    name=models.CharField(max_length=20)
    study_material=models.FileField()
    Class=models.CharField(max_length=20)

class chat_table(models.Model):
    date=models.DateField()
    from_id=models.ForeignKey(login_table,on_delete=models.CASCADE,related_name='from_id')
    to_id=models.ForeignKey(login_table,on_delete=models.CASCADE,related_name='to_id')
    message=models.CharField(max_length=100)

class suggestion_table(models.Model):
    EXPERT=models.ForeignKey(expert_table,on_delete=models.CASCADE)
    mark=models.IntegerField()
    suggestion=models.CharField(max_length=500)
    type=models.CharField(max_length=100)

class dataset(models.Model):
    STUDYMATERIAL=models.ForeignKey(study_material,on_delete=models.CASCADE)
    question=models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000)
    type=models.CharField(max_length=100)

class chatbot(models.Model):
    PARENT=models.ForeignKey(parent_table,on_delete=models.CASCADE)
    DATASET=models.ForeignKey(dataset,on_delete=models.CASCADE)
    answer=models.CharField(max_length=1000)
    date=models.DateField()



