from googletrans  import Translator

def get_translation (inputtext, outputlanguage = 'fr', inputlanguage = 'nl' ):
    translator = Translator()
    return translator.translate(inputtext, outputlanguage, inputlanguage ).text
    

if __name__ == "__main__":
    inputtext = 'ik ben een man'
    print(inputtext)
    outputlanguage = 'fr'
    inputlanguage = 'nl'
    output = get_translation(inputtext,outputlanguage,inputlanguage)
    print(output)


