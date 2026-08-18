# 6. Safe Calculator
# Concepts: Exception handling
# A calculator that handles division by zero and invalid (non-numeric) input using try/except, plus one custom
# exception.
# Hints:
# - Create class InvalidOperationError(Exception) for unsupported operators like '%%' or '^'.
# - Wrap the whole calculation in try/except ZeroDivisionError, except ValueError, except InvalidOperationError.
# - Use a finally block

class InvalidOperationError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def unsupport_operator(self):
        print('This operator not support buddy!')

class SafeCalculator:
    def __init__(self,num1,num2,operator):
        self.num1 = num1
        self.num2 = num2
        self.opeator = operator

    def calculation(self):
        try:
            self.num1 = float(self.num1)
            self.num2 = float(self.num2)
            if self.opeator in ['-','+','*','/']:
                if self.opeator == '-':
                    print(self.num1 - self.num2)

                elif self.opeator == '+':
                                    print(self.num1 + self.num2)

                elif self.opeator == '*':
                                    print(self.num1 * self.num2)

                else:
                       print(self.num1 / self.num2)

            else:
                   raise InvalidOperationError('Wrong operator')

        except ZeroDivisionError:
               print('Zero cannot divide any number')

        except ValueError:
               print('value have to integet or float')

        except InvalidOperationError as e:
               e.unsupport_operator()
               print(e)
        finally:
               print('Calculation attempt finished')

                


obj = SafeCalculator('a',23,'&')

obj.calculation()