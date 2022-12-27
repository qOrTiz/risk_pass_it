from django.db import models

class Probability_Impact(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Risk"
        verbose_name_plural = "Risks"


class Probability(models.Model):
    
    probability_impact = models.ForeignKey(Probability_Impact, verbose_name="Probability_Impact", help_text="Уровень", on_delete=models.CASCADE)
    
    text = models.TextField("Text", help_text="Текст", default="0")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Probability"
        verbose_name_plural = "Probability"


class Impact(models.Model):
    
    probability_impact = models.ForeignKey(Probability_Impact, verbose_name="Probability_Impact", help_text="Уровень", on_delete=models.CASCADE)
    
    text = models.TextField("Text", help_text="Текст", default="0")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Probability"
        verbose_name_plural = "Probability"


class Department_Objective(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Department_Objective"
        verbose_name_plural = "Department_Objective"


class Department_Goal(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Department_Goal"
        verbose_name_plural = "Department_Goal"
        

class Department_Object(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Department_Object"
        verbose_name_plural = "Department_Object"


class Risk(models.Model):
    risk_name = models.CharField("risk_name", max_length=200,
                            help_text="Название риска")
    risk_object = models.CharField("risk_object", max_length=200,
                            help_text="Объект риска")
    departament = models.ForeignKey(Department_Objective, verbose_name="departament", 
                            help_text="Цели отдела", on_delete=models.CASCADE)
    departament_goal = models.ForeignKey(Department_Goal, verbose_name="departament_goal", 
                            help_text="Доп цель отдела", on_delete=models.CASCADE)
    department_object = models.ForeignKey(Department_Object, verbose_name="departament_object", 
                            help_text="Доп цель отдела", on_delete=models.CASCADE)
    risk_description = models.TextField("risk_description",
                            help_text="Описание риска")
    probability_max = models.ForeignKey(Probability_Impact, verbose_name="probability_max", 
                            help_text="Макс вероятность появения причины", on_delete=models.CASCADE)
    risk_owner = models.TextField("probability_max",
                            help_text="Название подразделения")
    registration_date = models.CharField("registration_date", max_length=200,
                            help_text="Дата регистрации риска")
    
    probability = models.ManyToManyField(Probability, verbose_name="probability")
    impact = models.ManyToManyField(Impact, verbose_name="impact")
    
    def __str__(self):
        return self.Risk_Name

    class Meta:
        verbose_name = "Risk"
        verbose_name_plural = "Risks"
