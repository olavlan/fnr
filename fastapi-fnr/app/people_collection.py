from app.person import Person, MALE, FEMALE

DEFAULT_AGE_STEPS = [17, 24, 34, 44, 54, 64]

def get_age_groups(p):
    """
    Finds age groups defined by a list or comma-separated string
    Example 1: 
        - Input: [17, 24, 34, 35, 24, "hei", 0]
        - Output: [17, 24, 34, 35], ["0-17", "18-24", "25-34", "35", "36-"]
    Example 2:
        - Input: "15, 70, hei"
        - Output: [15, 70], ["0-15", "16-70", "71-"]
    Example 3 (get default age groups):
        - Input: False
        - Output:   [17, 24, 34, 44, 54, 64], 
                    ["0-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65-"]
    """
    if not p:
        age_steps = DEFAULT_AGE_STEPS
    else: 
        if isinstance(p, str):
            p = [e for e in p.split(",")]
        age_steps = []
        for e in p: 
            try:
                z = int(e)
                if z >= 0:
                    age_steps.append(z)
            except: 
                pass

    if len(age_steps) < 1:
        age_steps = DEFAULT_AGE_STEPS
    else:
        age_steps = list(set(age_steps)) #remove duplicates
        age_steps.sort() #sort integers
    
    age_groups = []
    previous_age_step = 0
    for i in range(len(age_steps)):
        age_step = age_steps[i]
        if age_step > previous_age_step:
            s = f"{previous_age_step}-{age_step}" 
        else:
            s = f"{age_step}"
        age_groups.append(s)
        previous_age_step = age_step + 1
    age_groups.append(f"{previous_age_step}-")
    
    return age_steps, age_groups

class PeopleCollection:
    def __init__(self, dataset_filepath):
        self.people = []
        self.n = 0
        with open(dataset_filepath, 'r') as file:
            for line in file:
                try:
                    p = Person(line.strip())
                    self.people.append(p)
                    self.n += 1
                except:
                    pass
        
    def __len__(self):
        return self.n
    
    def get_people(self):
        return self.people

    def set_age_groups(self, age_steps):
        """
        Sets the age_group attribute for each person, based on the age steps list
        """
        age_steps, age_groups = get_age_groups(age_steps)
        for p in self.people:
            p.set_age_group(age_steps, age_groups)
        return age_groups

    def get_counts(self):
        female_count = 0
        male_count = 0
        for p in self.people:
            if p.is_female():
                female_count += 1
            else:
                male_count += 1
        keys = [f"{FEMALE}", f"{MALE}", "total"]
        values = [female_count, male_count, female_count+ male_count]
        data = {} 
        for k,v in zip(keys, values):
            data[k] = v
        return data
    
    def get_detailed_counts(self, age_steps): 
        data = {}
        sorted_age_groups = self.set_age_groups(age_steps)
        for s in sorted_age_groups:
            data[s] = {MALE: 0, FEMALE: 0}
        for p in self.people: 
            data[p.get_age_group()][p.get_gender()] += 1
        return data