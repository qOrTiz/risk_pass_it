from django.db import models
from djmoney.models.fields import MoneyField

class Probability_Impact(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Probability_Impact"
        verbose_name_plural = "Probability_Impact"


class Probability(models.Model):
    
    probability_impact = models.ForeignKey(Probability_Impact, verbose_name="Probability_Impact", help_text="Уровень", on_delete=models.CASCADE)
    
    text = models.TextField("Text", help_text="Текст", default="0")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Probability"
        verbose_name_plural = "Probability"


class Impact(models.Model):
    
    probability_impact = models.ForeignKey(Probability_Impact, verbose_name="Probability_Impact", help_text="Уровень", on_delete=models.CASCADE)
    
    text = models.TextField("Text", help_text="Текст", default="0")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Impact"
        verbose_name_plural = "Impact"


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


    test = ""
    
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
    registration_date = models.DateField("registration_date", 
                            help_text="Дата регистрации риска") 
    
    probability = models.ManyToManyField(Probability, verbose_name="probability")
    impact = models.ManyToManyField(Impact, verbose_name="impact")
    
    def __str__(self):
        return f"{self.risk_name}" #{' '.join([Impact.objects.filter(id=i.id) for i in ])}"
    class Meta:
        verbose_name = "Risk"
        verbose_name_plural = "Risks"


    # def save(self, *args, **kwargs):

    #     super(Risk, self).save(*args, **kwargs)
    #     self.test = self.impact





class Final_assessment_of_effectiveness(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Final_assessment_of_effectiveness"
        verbose_name_plural = "Final_assessment_of_effectiveness"


class Reduce_Probability(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Reduce_Probability"
        verbose_name_plural = "Reduce_Probability"


class Precondition_Outcome(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Precondition_Outcome"
        verbose_name_plural = "Precondition_Outcome"


class Priority_Countermeasure(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Priority_Countermeasure"
        verbose_name_plural = "Priority_Countermeasure"


class Implementation_Status(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Implementation_Status"
        verbose_name_plural = "Implementation_Status"


class End_Countermeasure_Implementation(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")

    date = models.DateField("date", 
                            help_text="Дата") 
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "End_Countermeasure_Implementation"
        verbose_name_plural = "End_Countermeasure_Implementation"


class Countermeassures(models.Model):
    reduce_probability = models.ForeignKey(Reduce_Probability, verbose_name="reduce_probability", 
                            help_text="На что направлена мера", on_delete=models.CASCADE)
    precondition_outcome = models.ForeignKey(Risk, verbose_name="precondition_outcome", 
                            help_text="Причина риска для контрмеры", on_delete=models.CASCADE)
    name = models.TextField("name",
                            help_text="Название контрмеры")
    countermeasure_coordinator = models.CharField("сountermeasure_coordinator", max_length=200,
                           help_text="Владелец контрмеры")
    description = models.TextField("description",
                           help_text="Описание применяемой контрмеры")
    priority_countermeasure = models.ForeignKey(Priority_Countermeasure, verbose_name="priority_countermeasure", 
                            help_text="Приоритет контрмеры", on_delete=models.CASCADE)
    implementation_status = models.ForeignKey(Implementation_Status, verbose_name="implementation_status", 
                            help_text="Текущий статус контрмеры", on_delete=models.CASCADE)
    end_countermeasure_implementation = models.ForeignKey(End_Countermeasure_Implementation, verbose_name="end_countermeasure_implementation", 
                            help_text="Дата окончания внедрения контрмеры", on_delete=models.CASCADE)
    Budget = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    amount_specialists = models.BigIntegerField("amount_specialists",
                                     help_text="Количество специалистов")
    working_time = models.TimeField("working_time", 
                            help_text="Количество рабочего времени в часах")
    description_effectiveness = models.TextField("description_effectiveness",
                            help_text="Описание способа и порядка тестирования эффективности")
    generated_evidences = models.TextField("generated_evidences",
                            help_text="Подтверждение эффективности")
    repetition_test = models.BigIntegerField("repetition_test",
                                     help_text="Частота проверки эффективности")
    date_last_test = models.DateField("date_last_test", 
                            help_text="Дата последней проверки эффективности")
    final_assessment_of_effectiveness = models.ForeignKey(Final_assessment_of_effectiveness, verbose_name="final_assessment_of_effectiveness", 
                            help_text="Хз чо ето", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Countermeassures"
        verbose_name_plural = "Countermeassures"