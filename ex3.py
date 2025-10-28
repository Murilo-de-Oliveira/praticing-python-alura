def update_vogal_counter(text):
    vogals = ["a", "e", "i", "o", "u"]
    result = 0
    text = text.lower()
    for i in text:  
        if i in vogals:  
            result += 1 
            
    return result
    
text = input("Digite um texto: ")
print(f"O texto contém {update_vogal_counter(text)} vogais.")
