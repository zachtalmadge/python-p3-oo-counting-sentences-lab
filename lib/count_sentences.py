#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = value
    
    @property
    def value(self):
        return self._value
  
    @value.setter
    def value(self, newValue):
        if not isinstance(newValue, str):
            print('The value must be a string.')
            return
        else:
            self._value = newValue
    
    def is_sentence(self):
        return self.value.endswith('.')
      
    def is_question(self):
        return self.value.endswith('?')
      
    def is_exclamation(self):
        return self.value.endswith('!')
      
    def count_sentences(self):
        """this function turns exclamations and questions marks into periods, which then splits it into an array and returns the length of the array"""
        value = self.value
        for punc in ['!','?']:
            value = value.replace(punc, '.')
        
        sentences = [s for s in value.split('.') if s]
        
        return len(sentences)
