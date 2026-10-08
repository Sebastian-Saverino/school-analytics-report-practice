The dataset I'm choosing for our first project is a student exam variables. The intent is to learn what could be the biggest causes of poor exam scores.

One row represents a student and the variables that surround the student when a student takes an exam.

### Analytical Questions

1. What is the primary driver for low and high exam scores?

2. How does gender affect an individuals exam score?

3. How does physical activity affect students?

4. How does family income effect students scores as well does it correlate with the other variables such as location or Access to resources


The source is rather clean, does need some slight cleaning but nothing major, this could also be great for ML as well for predicting negative or positive scores in the future. 




hours_studied	int64	41	0	0.64 discrete num
attendance	int64	41	0	0.64 discrete num
parental_involvement	object	3	0	0.05 Ordinal cat
access_to_resources	object	3	0	0.05 ordinal cat
extracurricular_activities	object	2	0	0.03 
sleep_hours	int64	7	0	0.11 discrete
previous_scores	int64	51	0	0.80 discrete 
motivation_level	object	3	0	0.05 ordinal
internet_access	object	2	0	0.03 bool
tutoring_sessions	int64	9	0	0.14 discrete
family_income	object	3	0	0.05 ordinal
teacher_quality	object	3	0	0.05 ordinal
school_type	object	2	0	0.03 ordinal
peer_influence	object	3	0	0.05 ordinal
physical_activity	int64	7	0	0.11 ordinal
learning_disabilities	object	2	0	0.03 ordinal
parental_education_level	object	3	0	0.05 ordinal
distance_from_home	object	3	0	0.05 ordinal
gender	object	2	0	0.03 bool
exam_score	int64	45	0	0.71 discrete

