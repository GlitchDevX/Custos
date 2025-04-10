def snake_to_camel_case(text: str):
        result = ""
        for index, word in enumerate(text.split('_')):
            if index == 0:
                result += word
                continue
            
            result += word.title()
        
        return result
