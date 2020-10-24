print("Please enter the number of males in your class:");
male_num = int(input());
print("Please enter the number of females in your class:");
female_num = int(input());

total_students = (male_num + female_num);
male_percentage = ((male_num / total_students)*100);
female_percentage = ((female_num / total_students)*100);

print('The class population is ', male_percentage,'%', 'male and ', female_percentage,'%', 'female');
