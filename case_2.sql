select patients.name, patients.age, visits.visit_date, length(symptoms.symptom) - length(replace(symptoms.symptom, ",", "")) + 1 as symptom_count
from patients
inner join visits on patients.id = visits.patient_id
inner join symptoms on visits.id = symptoms.visit_id
where visits.department = 'Neurology' and patients.age > 50
having symptom_count >= 3
order by visits.visit_date desc limit 5;