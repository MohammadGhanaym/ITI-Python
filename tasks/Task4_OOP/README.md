```python
class Person:
    def __init__(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate

    def sleep(self, slept_hours):
        if slept_hours == 7:
            self.mood = 'happy'
        elif slept_hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def eat(self, n_meals):
        if n_meals >= 3:
            self.healthrate = 1
        elif n_meals == 2:
            self.healthrate = 0.75
        else:
            self.healthrate = 0.5
            
    def buy(self, items):
        # 1 item decrease money by 10L.E
        self._money -= 10 * items

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money_amt):
        if money_amt < 0:
            raise ValueError("Money is less than 0")
        else:
            self._money = money_amt
    
    def __str__(self):
        return "Person(name={}, money={}, mood={}, healthrate={})".format(self.name, self.money, self.mood, self.healthrate)
```


```python
class Employee(Person):
    def __init__(self, name, emp_id, car, salary, distance_to_work, money, mood, healthrate):
        super().__init__(name, money, mood, healthrate)
        self.employee_id = emp_id
        self.car = car
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours > 8:
            self.mood = 'tired'
        elif hours == 8:
            self.mood = 'happy'
        else:
            self.mood = 'lazy'

    def drive(self, velocity, distance):
        self.car.run(velocity, distance)

    def refuel(self, gas_amount=100):
        self.car.fuelrate += gas_amount

    def send_email(self, header, body, to):
        print('=' * 100)
        print('Send to: {}'.format(to))
        print('-' * 100)
        print(header)
        print(body)
        print('=' * 100)

    def __str__(self):
        return 'Employee(name={}, employee_id={}, car=Car(name={}, fuelrate={}, velocity={}),\n \
        salary={}, distance_to_work={}, money={}, mood={}, healthrate={})'.\
        format(self.name, self.employee_id, self.car.name, self.car.fuelrate, self.car.velocity,
               self.salary, self.distance_to_work, self.money, self.mood, self.healthrate)
            
```


```python
class Car:
    def __init__(self, name, fuelrate, velocity):
        self.name = name
        self.fuelrate = fuelrate
        self.velocity = velocity

    def run(self, velocity, distance):
        self.fuelrate -= 1
        self.velocity = velocity
        if not self.fuelrate:
            self.stop(distance)

    def stop(self, distance):
        self.velocity = 0
        if distance == 0:
            print('You arrived destination')
        else:
            print("Remaining distance is {}".format(distance))

    @property
    def fuelrate(self):
        return self._fuelrate
        
    @fuelrate.setter
    def fuelrate(self, fuelrate):
        if fuelrate >= 0 and fuelrate <= 100:
            self._fuelrate = fuelrate
        else:
            raise ValueError("Fuel Rate must be between 0 and 100")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        if velocity >= 0 and velocity <= 200:
            self._velocity = velocity
        else:
            raise ValueError("Velocity must be between 0 and 200")  
```


```python
class Office:
    employees_num = 0
    
    def __init__(self, name:str, employees:list[Employee]):
        self.name = name
        self.employees = employees
        Office.employees_num += len(self.employees)
        
    def get_all_employees(self):
        return self.employees

    def get_employee(self, employee_id) -> Employee:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
                

    def hire(self, hired_employee:Employee):
        self.employees.append(hired_employee)
        Office.employees_num += 1
        
    def fire(self, emp_id):
        for i, employee in enumerate(self.employees):
            if employee.employee_id == emp_id:
                Office.employees_num -= 1
                return self.employees.pop(i) 
                
    def deduct(self, emp_id, deduction):
        for i, employee in enumerate(self.employees):
            if employee.employee_id == emp_id:
                self.employees[i].salary -= deduction 

            
                
    def reward(self, emp_id, reward_amt):
        for i, employee in enumerate(self.employees):
            if employee.employee_id == emp_id:
               self.employees[i].salary += reward_amt 
        
    def check_lateness(self, empId, targethour, movehour):
        for i, employee in enumerate(self.employees):
            if employee.employee_id == empId:
                late_status = Office.calculate_lateness(targethour, movehour, employee.distance_to_work, employee.car.velocity)
                if late_status == 'late':
                    self.employees[i].salary -= 10 
                    
                else:
                    self.employees[i].salary += 10
                return late_status
                    
    @staticmethod
    def calculate_lateness(targethour, movehour, distance, velocity):
        time_taken = distance / velocity
        if time_taken + movehour > targethour:
            return 'late'
        else:
            return 'on time'


    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num += num

```


```python
if __name__ == '__main__':
    print("Test Person Class")
    ahmed = Person("Ahmed", 5000, 'Happy', 0.75)
    print(ahmed)
    
    try:
        ahmed.money = -1
    except Exception as e:
        print(e)
    
    print('-' * 40)
    print("Test Employee Class")
    nour = Employee(name="Nour", emp_id='123', 
                    car=Car('fiat', 17, 120), 
                    salary=10000, distance_to_work=5, 
                    money=30000, mood='Happy', healthrate=0.75)
    print(nour)
    try:
        nour.car.velocity = 220
    except Exception as e:
        print(e)
        
    nour.work(9)
    nour.refuel(10)
    nour.send_email('Hello, World', 'This is Python', 'omar@gmail.com')
    nour.drive(200, 10)
    print(nour)
      
    ali = Employee(name='Ali', emp_id='456', car=Car('BMW', 50, 95),
                   salary=15000, distance_to_work=100, 
                   money=50000, mood='Tired', healthrate=0.5)

    print('-' * 40)
    iti_smart_village = Office('Smart Village', [nour, ali])

    print("Get employee with ID 456")
    print(iti_smart_village.get_employee('456'))
    
    print('-' * 40)
    print("Number of All Employees: ", Office.employees_num)
    omar = Employee(name='Omar', emp_id='789', 
                    car=Car('Mercedes', 70, 100),
                    salary=12000, distance_to_work=20, money=100000, mood='Tired', healthrate=0.5)
    iti_smart_village.hire(omar)
    smart_emps = iti_smart_village.get_all_employees()
    print('Smart Village Employees: ')
    for emp in smart_emps:
        print(emp)
    
    print('-' * 40) 
    fired_emp = iti_smart_village.fire('123')
    print('Fired Employee: ', fired_emp.name)
    print('-' * 40) 
    print("Deduct")
    iti_smart_village.deduct('456', 100)
    print(iti_smart_village.get_employee('456'))
    print('-' * 40) 
    print("Reward")
    iti_smart_village.reward('789', 100)
    print(iti_smart_village.get_employee('789'))
    print('-' * 40) 
    print('Check Lateness')
    late_status = iti_smart_village.check_lateness('456', 8, 7)
    print(late_status)
    print(iti_smart_village.get_employee('456'))
```

    Test Person Class
    Person(name=Ahmed, money=5000, mood=Happy, healthrate=0.75)
    Money is less than 0
    ----------------------------------------
    Test Employee Class
    Employee(name=Nour, employee_id=123, car=Car(name=fiat, fuelrate=17, velocity=120),
             salary=10000, distance_to_work=5, money=30000, mood=Happy, healthrate=0.75)
    Velocity must be between 0 and 200
    ====================================================================================================
    Send to: omar@gmail.com
    ----------------------------------------------------------------------------------------------------
    Hello, World
    This is Python
    ====================================================================================================
    Employee(name=Nour, employee_id=123, car=Car(name=fiat, fuelrate=26, velocity=200),
             salary=10000, distance_to_work=5, money=30000, mood=tired, healthrate=0.75)
    ----------------------------------------
    Get employee with ID 456
    Employee(name=Ali, employee_id=456, car=Car(name=BMW, fuelrate=50, velocity=95),
             salary=15000, distance_to_work=100, money=50000, mood=Tired, healthrate=0.5)
    ----------------------------------------
    Number of All Employees:  2
    Smart Village Employees: 
    Employee(name=Nour, employee_id=123, car=Car(name=fiat, fuelrate=26, velocity=200),
             salary=10000, distance_to_work=5, money=30000, mood=tired, healthrate=0.75)
    Employee(name=Ali, employee_id=456, car=Car(name=BMW, fuelrate=50, velocity=95),
             salary=15000, distance_to_work=100, money=50000, mood=Tired, healthrate=0.5)
    Employee(name=Omar, employee_id=789, car=Car(name=Mercedes, fuelrate=70, velocity=100),
             salary=12000, distance_to_work=20, money=100000, mood=Tired, healthrate=0.5)
    ----------------------------------------
    Fired Employee:  Nour
    ----------------------------------------
    Deduct
    Employee(name=Ali, employee_id=456, car=Car(name=BMW, fuelrate=50, velocity=95),
             salary=14900, distance_to_work=100, money=50000, mood=Tired, healthrate=0.5)
    ----------------------------------------
    Reward
    Employee(name=Omar, employee_id=789, car=Car(name=Mercedes, fuelrate=70, velocity=100),
             salary=12100, distance_to_work=20, money=100000, mood=Tired, healthrate=0.5)
    ----------------------------------------
    Check Lateness
    late
    Employee(name=Ali, employee_id=456, car=Car(name=BMW, fuelrate=50, velocity=95),
             salary=14890, distance_to_work=100, money=50000, mood=Tired, healthrate=0.5)
    


```python

```
