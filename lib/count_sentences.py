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
        # Splitting the string at '.', '!', and '?'
        sentences = [sentence for sentence in self.value.split('.')]
        sentences += [sentence for sentence in self.value.split('!')]
        sentences += [sentence for sentence in self.value.split('?')]
        return len(sentences)
