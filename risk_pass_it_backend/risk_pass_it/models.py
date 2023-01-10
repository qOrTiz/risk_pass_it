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


class Countermeasures(models.Model):
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
    budget = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    amount_specialists = models.BigIntegerField("amount_specialists",
                                     help_text="Количество специалистов")
    working_time = models.IntegerField("working_time", 
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
        verbose_name = "Countermeasures"
        verbose_name_plural = "Countermeasures"
    

    









class Material_Damage(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Material_Damage"
        verbose_name_plural = "Material_Damage"


class Immaterial_Damage(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Immaterial_Damage"
        verbose_name_plural = "Immaterial_Damage"

class Legal_Relevance(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Legal_Relevance"
        verbose_name_plural = "Legal_Relevance"


class Risk_response_strategie(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Risk_response_strategie"
        verbose_name_plural = "Risk_response_strategie"


class Risk_manager(models.Model):
    
    text = models.TextField("Text", help_text="Текст", default="0")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Risk_manager"
        verbose_name_plural = "Risk_manager"




class Assessment(models.Model):
    risk_id = models.ForeignKey(Risk, verbose_name="risk_id", 
                            help_text="Probabi", on_delete=models.CASCADE)
    material_damage = models.ForeignKey(Material_Damage, verbose_name="material_damage", 
                            help_text="Материальный ущерб", on_delete=models.CASCADE)
    immaterial_damage = models.ForeignKey(Immaterial_Damage, verbose_name="immaterial_damage", 
                            help_text="Отрицательное влияние", on_delete=models.CASCADE)
    legal_relevance = models.ForeignKey(Legal_Relevance, verbose_name="legal_relevance", 
                            help_text="Уровни требований внешнего законодательства", on_delete=models.CASCADE)
    risk_assessment_score = models.FloatField("risk_assessment_score",
                            help_text="Тут ВПР :)")
    comments = models.TextField("comments",
                           help_text="Описание способа оценки и т.д.")
    risk_response_strategie = models.ForeignKey(Risk_response_strategie, verbose_name="risk_response_strategie", 
                            help_text="Уровни риска", on_delete=models.CASCADE)
    risk_raiting = models.BigIntegerField("risk_raiting",
                                     help_text="Рейтинг риска")
    assessment_date = models.DateField("assessment_date", 
                            help_text="Дата регистрации риска")
    review_date = models.DateField("review_date", 
                            help_text="Дата следующей проверки риска")
    risk_manager = models.ForeignKey(Risk_manager, verbose_name="risk_manager", 
                            help_text="Риск менеджер", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id} {self.risk_id}"

    class Meta:
        verbose_name = "Assessment"
        verbose_name_plural = "Assessments"

    def save(self, *args, **kwargs):
        #super(Assessment, self).save(*args, **kwargs)
        #risk_mark[]
        risk_data = Risk.objects.filter(id=int(self.risk_id_id))
        #print(risk_data)
        
        probability_impact_max = Probability_Impact.objects.filter(id=int(risk_data[0].probability_max_id))

        material_damage_data = Material_Damage.objects.filter(id=int(self.material_damage_id))
        immaterial_damage_data = Immaterial_Damage.objects.filter(id=int(self.immaterial_damage_id))
        legal_relevance_data = Legal_Relevance.objects.filter(id=int(self.legal_relevance_id))

        
        risk_mark = { '-' : 0, 'low' : 2, 'middle' : 3, 'high' : 5, 'very high' : 10}

        material_damage_mark = {'< 25.000 €' : 0.05, '< 50.000 €' : 0.06, '< 100.000 €': 0.07, '< 250.000 €' : 0.09, '< 500.000 €' : 0.1, '< 1 Mio €' : 0.15,
                            '< 2,5 Mio €' : 0.17, '< 5 Mio €' : 0.2, '< 10 Mio €' : 0.5, '< 25 Mio €' : 0.6, '< 50 Mio €' : 0.8, '< 100 Mio €' : 1,
                            '< 250 Mio €' : 3, '< 500 Mio €' : 5, '< 1.000 Mio €' : 8, '>= 1.000 Mio €' : 10}
    
        immaterial_damage_mark = {'нет' : 0, 'кратковременная потеря доверия' : 0.1, 'длительная потеря доверия' : 1, 'потеря репутации (региональная)' : 5,
                        'потеря репутации (международная)' : 10}
                        
        legal_relevance_mark = {'нет' : 0, 'небольшая' : 0.1, 'умеренная' : 1, 'сильная' : 5, 'очень сильная' : 10}
        
        risk_mark_value = risk_mark[str(probability_impact_max[0].text).lower().strip()]
        material_damage_mark_value = material_damage_mark[str(material_damage_data[0].text).lower().strip()]
        immaterial_damage_mark_value = immaterial_damage_mark[str(immaterial_damage_data[0].text).lower().strip()]
        legal_relevance_mark_value = legal_relevance_mark[str(legal_relevance_data[0].text).lower().strip()]

        general_value = risk_mark_value * (material_damage_mark_value + (immaterial_damage_mark_value + legal_relevance_mark_value) / 2)
        
        self.risk_assessment_score = round(general_value, 2)
        super(Assessment, self).save(*args, **kwargs)

    




class Dashboard(models.Model):
    risk_id = models.ForeignKey(Risk, verbose_name="risk_id", 
                            help_text="Цель и описание риска из таблицы Risk", on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessment, verbose_name="assessment_id", 
                            help_text="Оценка риска и потерь из таблицы Assessment", on_delete=models.CASCADE)
    # countermeasures_id = models.ForeignKey(Countermeasures, verbose_name="countermeasures_id", 
    #                         help_text="Затраты на контрмеры из таблицы Countermeasures", on_delete=models.CASCADE)

    countermeasures_ids = models.ManyToManyField(Countermeasures, verbose_name="countermeasures_id", 
                            help_text="Затраты на контрмеры из таблицы Countermeasures")
    budgets_countermeasures_new = models.FloatField("budget_countermeasures",
                            help_text="Общий бюджет", default=0)
    specialists_countermeasures = models.FloatField("specialist_countermeasures", #amount_specialists
                            help_text="Общее число людей", default=0) 
    time_countermeasures = models.FloatField("time_countermeasures", #working_time
                            help_text="Общее количество чел*час", default=0)

    
    def __str__(self):
        return f"{self.id} {self.risk_id}"

    class Meta:
        verbose_name = "Dashboard"
        verbose_name_plural = "Dashboard"


    def save(self, *args, **kwargs):
        #super(Dashboard, self).save(*args, **kwargs)
        result = Dashboard.objects.filter(id=self.id)
        res = result.values_list('countermeasures_ids__id', flat=True)
        budgets_countermeasures_list = []
        specialists_countermeasures_list = []
        time_countermeasures_list = []
        for i in res:
            result = Countermeasures.objects.filter(id=i)
            from .serializers import CountermeasuresSerializer
            serializer = CountermeasuresSerializer(result[0])
            serializer = serializer.data
            budgets_countermeasures_list.append(float(serializer["budget"]))
            specialists_countermeasures_list.append(serializer["amount_specialists"])
            time_countermeasures_list.append(serializer["working_time"])
        
        self.budgets_countermeasures_new = sum(budgets_countermeasures_list)
        self.specialists_countermeasures = sum(specialists_countermeasures_list)
        self.time_countermeasures = sum(time_countermeasures_list)
        super(Dashboard, self).save(*args, **kwargs)