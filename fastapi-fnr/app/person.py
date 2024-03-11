from datetime import date
FIRST_CONTROL_SEQUENCE = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1]
SECOND_CONTROL_SEQUENCE = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
MALE = "male"
FEMALE = "female"

def control_checks(seq):
    seq = [int(d) for d in seq]
    s1 = sum(x*y for x,y in zip(seq, FIRST_CONTROL_SEQUENCE))
    s2 = sum(x*y for x,y in zip(seq, SECOND_CONTROL_SEQUENCE))
    return (s1 % 11 == 0) and (s2 % 11 == 0)  

def to_date(seq):
    d, m, y = seq[0:2], seq[2:4], seq[4:6]
    if int(seq[6]) < 5:
        y = "19" + y
    else:
        y = "20" + y
    d, m, y = [int(e) for e in [d, m, y]]
    try:
        birth_date = date(y, m, d)
        #Don't allow future dates:
        #if birth_date > date.today():
        #    return False
        return birth_date
    except:
        return False

def is_valid(seq):

    if len(seq) != 11:
        return False
    
    birth_date = to_date(seq)
    if not birth_date:
        return False
    
    if not control_checks(seq):
        return False

    return birth_date

class Person:
    def __init__(self, p):
        seq = str(p)
        test_result = is_valid(seq)
        if test_result:
            self.birth_date = test_result
            self.fnr = seq
            self.age_group = "0-150"
        else: 
            raise ValueError("Invalid number provided.")

    def is_female(self):
        if int(self.fnr[8]) % 2 == 0:
            return True
        else: 
            return False
    
    def is_male(self):
        return not is_female(self)
    
    def get_gender(self):
        if self.is_female():
            return FEMALE
        else:
            return MALE
        
    def get_age(self):
        diff = date.today().year - self.birth_date.year
        if diff < 0:
            diff = 0
        return diff
    
    def set_age_group(self, sorted_age_steps, sorted_age_groups):
        age = self.get_age()
        for i in range(len(sorted_age_steps)):
            age_step = sorted_age_steps[i]
            if age <= age_step: 
                self.age_group = sorted_age_groups[i]
                return self.age_group
        self.age_group = sorted_age_groups[-1]
    
    def get_age_group(self):
        return self.age_group

    def exists_in_dataset(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == self.fnr:
                    return True
        return False


#fnr = 31129956789
#fnr = 25119538540
#fnr = 25119433714

#p = Person(fnr)
#print(p.exists_in_dataset("data/fnr.txt"))